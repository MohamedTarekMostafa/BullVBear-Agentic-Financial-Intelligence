# ⚖️ 🤖 BullVBear: Agentic Financial Intelligence
A Multi-Agent ecosystem where specialized Bulls and Bears clash to deliver data-driven investment verdicts.
<img width="1600" height="640" alt="image" src="https://github.com/user-attachments/assets/74d24ae4-27bf-4fd6-b2bf-a18efcb554a8" />
<img width="1600" height="480" alt="image" src="https://github.com/user-attachments/assets/c8ff3ab3-29f0-46f8-ab25-ffc90f5810f7" />
<img width="1600" height="601" alt="image" src="https://github.com/user-attachments/assets/543d2ea9-8eaa-4b82-a388-d3a7493961ce" />
(![WhatsApp Image 2026-01-02 at 3 14 40 PM](https://github.com/user-attachments/assets/32872c2c-17b4-46cb-8bf7-16c30fe1341b)

This is a production-grade **Multi-Agent Financial Intelligence System**. Instead of a simple chatbot, it uses a **Parallel Fan-out/Fan-in Architecture** to simulate a professional investment committee, where conflicting perspectives (Bullish vs. Bearish) are synthesized to provide a data-driven, non-biased investment verdict.

## 🌟 The Innovation: "Conflict-Driven Reasoning"
Most AI financial tools suffer from **Confirmation Bias**. This system solves this by forcing a "clash" between specialized agents:
* **🟢 The Bull Agent**: Programmed to find catalysts, growth, and optimism.
* **🔴 The Bear Agent**: Programmed to find risks, debts, and market threats.
* **📊 The Quant Agent**: Provides the "Ground Truth" using hard market data (P/E, Dividends, Volatility).
* **⚖️ The Aggregator (Chief Investment Officer)**: Acts as the judge, resolving conflicts and tailoring the verdict to the user's specific **Memory-stored Risk Profile**.

---

## 🏗️ Architecture
The system is built on a **Directed Acyclic Graph (DAG)** using `LangGraph`:

* **Parallel Execution**: Research and Data Fetching nodes run concurrently, drastically reducing latency.
* **Stateful Persistence**: Uses `MemorySaver` to track user financial profiles (e.g., age, risk tolerance) across sessions.
* **Decoupled Tools**: Each agent has its own tool node, ensuring clean data context and preventing "hallucination contamination."

---

## 🛠️ Tech Stack
* **Orchestration**: `LangGraph` (for complex agentic workflows).
* **Brain**: `Llama-3.3-70B-Versatile` (via Groq for ultra-fast inference).
* **Real-time Data**: `yfinance` (Market stats) & `Tavily Search` (Financial news).
* **UI**: `Streamlit` (Interactive Dashboard with Multi-tab views).
* **Observability**: `Langfuse` (Tracing & Monitoring).

---

## 🧪 Real-World Test Case (Reasoning in Action)
**User Profile Stored in Memory:** "65-year-old retiree, low risk tolerance."
**Question:** "Analyze AMD vs Intel."

**The Result:** Even though AMD is showing massive growth potential (The Bull's view), the **Aggregator** issues a verdict favoring **Intel**. 
**Reason:** The system identifies that Intel's stable dividends and lower valuation (Quant data) align better with a **Retiree's Risk Profile**, proving the system doesn't just "chat"—it thinks and remembers.

---



