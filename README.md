# Token Counter

A simple Python script that counts the number of tokens in a text file using OpenAI's `tiktoken` library.

## Why tokens matter
- LLMs have a context window limit measured in tokens
- API cost depends on the number of tokens
- Useful for deciding chunk size in RAG applications

## Requirements
- Python 3.13
- tiktoken

## Installation
```bash
pip install tiktoken
```

## Usage
1. Put your text in `notes.txt`
2. Run:
```bash
python count_token.py notes.txt gpt-4o
```

## Example Output
```
File  : notes.txt
Model : gpt-4o
Tokens: 12
```

## Author
Ashwini Dhomne
GitHub: [Ashwini028](https://github.com/Ashwini028)