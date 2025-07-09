# core/brain.py

def load_personality():
    with open("personality.txt", "r") as file:
        return file.read()

def generate_response(user_input):
    personality = load_personality()
    # Placeholder logic
    return f"{personality.splitlines()[0]} I'm here to help you with '{user_input}'!"
