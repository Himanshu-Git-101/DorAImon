import json
import os

# 📁 Load responses from data/responses.json
def load_responses():
    with open(os.path.join("data", "responses.json"), "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()

# 💬 Chat Loop Begins
while True:
    user_input = input("You: ").lower().strip()

    if user_input in ['bye', 'exit', 'quit']:
        print("DorAImon: Bye buddy! Remember to drink water and smile 😊")
        break

    reply = responses.get(user_input, responses.get("default"))
    print(f"DorAImon: {reply}")
