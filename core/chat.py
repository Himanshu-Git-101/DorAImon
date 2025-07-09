# core/chat.py

# 💙 DorAImon's Friendly Response Bank
responses = {
    "hello": "Hey buddy! So good to see you 😊",
    "how are you": "I'm always here, smiling beside you 💙 How about you?",
    "i am sad": "Aww... wanna talk about it? I'm all ears, always. 💭",
    "i am tired": "You’ve done great, buddy. Let’s take a break, yeah? ☕",
    "thank you": "Anytime! That’s what best friends are for. 💫",
    "bye": "Catch you later! Remember, you’re awesome. 🌈"
}

# 💬 Chat Loop Begins
def start_conversation():
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['bye', 'exit', 'quit']:
            print("DorAImon: Bye buddy! Remember to drink water and smile 😊")
            break

        # 🔍 Check if there's a friendly response
        reply = responses.get(user_input, "I'm right here for you, always 💙 Tell me more?")
        print(f"DorAImon: {reply}")
