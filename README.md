#  The Multi-Agent Investor

Welcome to the **The Multi-Agent Investor**, an intelligent multi-agent system built with **LangGraph**, **LangChain**, and **Streamlit**. This project simulates a professional hedge fund meeting where three specialized agents with conflicting personalities debate a stock's potential before a "Chief Investment Officer" delivers the final verdict.

---

![WhatsApp Image 2026-01-07 at 11 07 16 PM](https://github.com/user-attachments/assets/655a3163-986b-416f-844b-7d4a6781d3ce)

The system runs three agents in **parallel** to ensure a balanced and thorough analysis:

1.  **🟢 The Optimistic Investor:** Scours the web for growth catalysts, expansion plans, and positive market trends.
2.  **🔴 The Pessimistic Investor:** Digs deep into risks, debts, lawsuits, and competitive threats.
3.  **📊 The Analytical Researcher:** Focuses strictly on the numbers—fetching real-time market data, P/E ratios, and price trends.
4.  **⚖️ The Aggregator (CIO):** A "nasty" but fair Chief Investment Officer who critiques the analysts, resolves conflicts, and provides a bold final verdict.

---

## 🛠️ Tech Stack

* **Framework:** [LangGraph](https://github.com/langchain-ai/langgraph) (for stateful, multi-agent orchestration).
* **LLM:** [Llama-3.3-70B-Versatile](https://groq.com/) via Groq for high-speed reasoning.
* **Tools:** * `TavilySearch` for real-time web intelligence.
    * `yfinance` for live stock market data.
* **UI:** [Streamlit](https://streamlit.io/) for an interactive dashboard.
* **Observability:** [Langfuse](https://langfuse.com/) for tracing and monitoring agent performance.

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python 3.9+ installed.
![Uploading WhatsApp Image 2026-01-07 at 11.55.10 PM.jpeg…]()
![WhatsApp Image 2026-01-07 at 11 55 41 PM](https://github.com/user-attachments/assets/588d4dfb-6cc5-4ac1-a7de-9afbfd5d5ede)

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install langchain-tavily langchain-groq langgraph yfinance streamlit python-dotenv langfuse
3. Environment Variables

Create a .env file in the root directory and add your API keys:
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST="[https://cloud.langfuse.com](https://cloud.langfuse.com)"
4. Running the App

Launch the Streamlit dashboard
streamlit run app.py
📋 Project Structure

tools.py: Contains the logic for web searching and financial data fetching.
agent.py: Defines the LangGraph architecture, agent nodes, and the decision-making flow.\
app.py: The frontend UI that manages session states and displays the debate.
💡 How it Works

User Input: You enter a stock ticker (e.g., NVDA, TSLA).
Parallel Execution: The Optimist, Pessimist, and Researcher start working simultaneously.
Tool Usage: Agents use Tavily and yfinance to gather evidence.

The Debate: The Aggregator receives all reports, calls out biases, and generates a structured report with a clear Buy/Hold/Sell reality check.
