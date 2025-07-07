# core/brain.py

def load_personality(file_path="data/personality.txt"):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

