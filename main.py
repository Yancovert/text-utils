from text_utils.cleaner import remove_extra_spaces
from text_utils.converter import to_uppercase, to_lowercase, reverse_text
from text_utils.counter import count_words, count_characters, count_lines

def run():
    print("Welcome to Text Utils CLI")
    sample = input("Enter text: ")

    print("\n--- Results ---")
    print("Cleaned: ", remove_extra_spaces(sample))
    print("Uppercase: ", to_uppercase(sample))
    print("Lowercase: ", to_lowercase(sample))
    print("Reversed: ", reverse_text(sample))
    print("Word count:", count_words(sample))
    print("Char count:", count_characters(sample))
    print("Line count:", count_lines(sample))

if __name__ == "__main__":
    run()
