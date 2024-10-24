from pathlib import Path

def count_words(text: str) -> int:
    return len(text.split())

def count_chars_frequency(text: str) -> list[tuple[str, int]]:
    text = text.lower()

    chars_frequencies: dict[str, int] = {}

    for char in text:
        if char.isalpha():
            if char not in chars_frequencies:
                chars_frequencies[char] = 0
            chars_frequencies[char] += 1

    sorted_frequencies = sorted(
        chars_frequencies.items(), 
        key=lambda item: item[1], 
        reverse=True
    )

    return sorted_frequencies


def main():

    books_path = Path("books")
    file_path = books_path / "frankenstein.txt"

    with open(file_path) as file:
        content = file.read()

        print(f"--- Begin report of {file_path} ---")

        word_count = count_words(content)
        print(f"{word_count} words found in the document")
        print()

        chars_frequency = count_chars_frequency(content)
        for char, frequency in chars_frequency:
            print(f"The '{char}' character was found {frequency} times")

        print("--- End report ---")



if __name__ == "__main__":
    main()
