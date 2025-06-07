def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> int:
    return len(text)

def count_lines(text: str) -> int:
    return text.count("\n") + 1 if text else 0
