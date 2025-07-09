# core/chat.py

from core.brain import load_personality
from core.memory import load_memory, save_memory

responses = {
    "hello": "Hey buddy! So good to see you 😊",
    "how are you": "I'm always here, smiling beside you 💙 How about you?",
    "i am sad": "Aww... wanna talk about it? I'm all ears, always. 💭",
    "i am tired": "You’ve done great, buddy. Let’s take a break, yeah? ☕",
    "thank you": "Anytime! That’s what best friends are for. 💫",
    "bye": "Catch you later! Remember, you’re awesome. 🌈"
}

def start_conversation():
    personality = load_personality()
    memory = load_memory()

    # 🧠 Ask for name if not known
    if "name" not in memory:
        name = input("Hey! What should I call you, buddy? 🧸: ")
        memory["name"] = name
        save_memory(memory)
    else:
        name = memory["name"]
        print(f"DorAImon: Welcome back, {name}! 💙")

    print("💬 DorAImon is listening... (type 'bye' to exit)\n")

    while True:
        user_input = input(f"{name}: ")

        if user_input.lower() in ['bye', 'exit', 'quit']:
            print(f"DorAImon: Bye {name}! Remember to smile and hydrate 💧")
            break

        reply = responses.get(user_input.lower(), f"I’m right here for you, {name} 💙 Tell me more?")
        print(f"DorAImon: {reply}")

       