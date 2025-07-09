# core/brain.py

def load_personality():
    """
    Loads personality traits from the data/personality.txt file.

    Returns:
        list: A list of personality trait strings.
    """
    try:
        with open("data/personality.txt", "r", encoding="utf-8") as file:
            traits = file.readlines()
            return [trait.strip() for trait in traits if trait.strip()]
    except FileNotFoundError:
        print("⚠️ personality.txt not found. Make sure it exists in the 'data/' folder.")
        return []
