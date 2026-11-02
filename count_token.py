import sys
import tiktoken


def get_encoding(model: str):
    """Get the tokenizer for a model, with a fallback."""
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Return the number of tokens in a string."""
    enc = get_encoding(model)
    return len(enc.encode(text))


def count_file(path: str, model: str = "gpt-4o") -> int:
    """Return the number of tokens in a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return count_tokens(f.read(), model)


if __name__ == "__main__":
    # Works with the green Run button (uses notes.txt)
    # or from the terminal: python count_tokens.py myfile.txt gpt-4o
    path = sys.argv[1] if len(sys.argv) > 1 else "notes.txt"
    model = sys.argv[2] if len(sys.argv) > 2 else "gpt-4o"

    try:
        total = count_file(path, model)
        print(f"File  : {path}")
        print(f"Model : {model}")
        print(f"Tokens: {total}")
    except FileNotFoundError:
        print(f"Error: '{path}' not found. Create it in the project folder.")