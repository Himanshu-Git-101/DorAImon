from core.brain import load_personality

personality = load_personality()

print("🧠 DorAImon is now active!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("DorAImon: Bye! Talk to you soon 💙")
        break

    # Respond with friendly preset tone
    response = f"DorAImon: I hear you! But remember, {personality[0]}"
    print(response)
