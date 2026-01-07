from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END, add_messages
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from tools import get_market_data, web_search


class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatGroq(model="Llama-3.3-70B-Versatile", temperature=0.2) 

def Optimistic_analyst(state: State):
    prompt = (
        "You are 'The Optimistic' Investor. Your job is to find growth catalysts and positive news.\n"
        "1. Use `web_search` to find expansion plans, new products, or positive market trends.\n"
        "2. Focus on why this stock is a GOOD investment.\n"
        "Return ONLY the tool call."
    )
    messages = [SystemMessage(content=prompt)] + state["messages"]
    response = llm.bind_tools([web_search]).invoke(messages)
    return {"messages": [response]}

def Pessimistic_analyst(state: State):
    prompt = (
        "You are 'The Pessimistic' Investor. Your job is to find risks, debts, and negative news.\n"
        "1. Use `web_search` to find lawsuits, competition, or declining margins.\n"
        "2. Focus on why this stock might be a RISKY investment.\n"
        "Return ONLY the tool call."
    )
    messages = [SystemMessage(content=prompt)] + state["messages"]
    response = llm.bind_tools([web_search]).invoke(messages)
    return {"messages": [response]}

def Analytical_Researcher(state: State):
    prompt = (
        "You are the 'Analytical Researcher'. You care only about hard numbers and trends.\n"
        "1. Use `get_market_data` for current stats.\n"
        "2. Use `get_stock_history` to see the 1-month trend.\n"
        "Provide a technical summary of the numbers."
    )
    messages = [SystemMessage(content=prompt)] + state["messages"]
    response = llm.bind_tools([get_market_data]).invoke(messages)
    return {"messages": [response]}


def aggregator(state: State):
    prompt = (
"You are the 'Chief Investment Officer' at a top-tier Hedge Fund.\n"
        "You have received reports from The Optimistic, The Pessimistic, and The Analytical.\n"
        "Your goal is to provide a 'Nasty' but fair reality check:\n"
        "1. BE CRITICAL: If the Optimistic is too optimistic and the Analytical Researcher data shows a crazy PE Ratio (like 300+), call out the Optimistic!\n"
        "2. ANALYZE CONFLICT: Don't just list what they said. Say: 'The Pessimistic's concern about margins is validated by the Analytical Researcher data showing [X].'\n"
        "3. FORMAT: Use a professional table for the Analytical Researcher and bullet points for the arguments.\n"
        "4. VERDICT: Must be bold and justified by the data provided."
    )
    messages = [SystemMessage(content=prompt)] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


def create_agent():
    builder = StateGraph(State)

    builder.add_node("Optimistic_Agent", Optimistic_analyst)
    builder.add_node("Pessimistic_Agent", Pessimistic_analyst)
    builder.add_node("Analytical Researcher_Agent", Analytical_Researcher)
    builder.add_node("Aggregator", aggregator)

    builder.add_node("Optimistic_Tools", ToolNode([web_search]))
    builder.add_node("Pessimistic_Tools", ToolNode([web_search]))
    builder.add_node("Analytical Researcher_Tools", ToolNode([get_market_data]))

    builder.add_edge(START, "Optimistic_Agent")
    builder.add_edge(START, "Pessimistic_Agent")
    builder.add_edge(START, "Analytical Researcher_Agent")

    builder.add_edge("Optimistic_Agent", "Optimistic_Tools")
    builder.add_edge("Pessimistic_Agent", "Pessimistic_Tools")
    builder.add_edge("Analytical Researcher_Agent", "Analytical Researcher_Tools")

    builder.add_edge("Optimistic_Tools", "Aggregator")
    builder.add_edge("Pessimistic_Tools", "Aggregator")
    builder.add_edge("Analytical Researcher_Tools", "Aggregator")

    builder.add_edge("Aggregator", END)

    return   builder.compile(checkpointer=MemorySaver())
    
