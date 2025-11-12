# Agentic Customer Query AI

An autonomous LangChain agent that:

* **Reasons** over customer queries  
* **Calculates** (discounts, totals, etc.) with a safe math tool  
* **Remembers** key facts/preferences via OpenAI embeddings + FAISS  

Inspired by the embedding query pattern in  
[campusx-official/langchain-models](https://github.com/campusx-official/langchain-models/).

---

## Quick Start

```bash
# 1. Clone & cd
git clone https://github.com/<YOU>/agentic-customer-query-ai.git
cd agentic-customer-query-ai

# 2. Install
pip install -r requirements.txt

# 3. Add your OpenAI key
cp .env.example .env
# edit .env → OPENAI_API_KEY=sk-...

# 4. Run
python main.py
