from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from tools.math_tool import calculate
from memory.vector_memory import CustomerMemory
import config


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=config.OPENAI_API_KEY,
)

tools = [calculate]
memory = CustomerMemory()

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content="You are a helpful customer-support agent. "
                "Use the `calculate` tool for any math. "
                "Incorporate retrieved user facts to personalize answers."
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def run_query(user_id: str, user_query: str) -> str:
    """Retrieve facts → inject → execute."""
    facts = memory.retrieve_relevant_facts(user_id, user_query)
    context = "Known user facts: " + "; ".join(facts) if facts else "No known facts."

    full_input = f"{context}\n\nCustomer query: {user_query}"
    result = executor.invoke({"input": full_input, "chat_history": []})
    return result["output"]
