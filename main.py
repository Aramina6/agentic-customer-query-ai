from agent.customer_agent import run_query, memory

def main():
    print("Agentic Customer Query AI")
    user_id = input("\nEnter user ID: ").strip() or "guest"

    # Optional: add a fact on start
    if input("Add an initial fact? (y/n): ").lower().startswith("y"):
        fact = input("Fact text: ").strip()
        memory.add_fact(user_id, fact)
        print("Fact saved.\n")

    print("\nStart chatting (type 'quit' to exit)\n")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"quit", "exit"}:
            break
        if not query:
            continue
        answer = run_query(user_id, query)
        print(f"Agent: {answer}\n")

if __name__ == "__main__":
    main()
