import streamlit as st
from agent import create_agent
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langfuse.langchain import CallbackHandler
from dotenv import load_dotenv
import uuid

load_dotenv(".env")

def clean_message_content(content):
    """Extracts plain text from complex model responses."""
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and item.get('type') == 'text':
                return item.get('text')
        return str(content)
    return content

st.set_page_config(page_title="AI Investor With Multiple Agents", page_icon="⚖️", layout="wide")

st.title(" AI Investor With Multiple Agents")
st.markdown("""
This system simulates a high-level investment meeting with three conflicting perspectives:
1. 🟢 **The Optimistic**: Searches for growth and catalysts.
2. 🔴 **The Pessimistic**: Digs for risks and pitfalls.
3. 📊 **The Analytical Researcher**: Analyzes hard market data and trends.
""")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())

st.sidebar.title("System Status")
st.sidebar.info(f"**Architecture:** Parallel Investment Committee\n\n**Thread ID:** `{st.session_state.thread_id}`")
if st.sidebar.button("Reset Session"):
    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4())
    st.rerun()

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
        with st.chat_message("assistant"):
            st.markdown(clean_message_content(msg.content))

if prompt := st.chat_input("Enter stock symbol (e.g., TSLA, AAPL, NVDA)..."):
    
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("The Committee is debating (Optimistic vs Pessimistic vs Analytical Researcher)..."):
            try:
                langfuse_handler = CallbackHandler()
                config = {
                    "configurable": {"thread_id": st.session_state.thread_id},
                    "callbacks": [langfuse_handler]
                }

                response = st.session_state.agent.invoke({"messages": st.session_state.messages}, config)
                st.session_state.messages = response["messages"]
                

                final_verdict = response["messages"][-1].content
                
                tab1, tab2 = st.tabs(["🎯 Final Verdict", "🔍 Inside the Debate"])
                
                with tab1:
                    st.markdown("### The Agents Decision")
                    st.markdown(clean_message_content(final_verdict))
                
                with tab2:
                    st.info("Below is the raw data gathered by each specialist during the parallel execution.")
                    st.markdown("**Role-Play Summary:**")
                    st.write("The Optimistic and Pessimistic agents performed deep-dives into recent filings and news to find conflicting signals.")
                    
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")