from string import ascii_lowercase

let = {letter: str(index) for index, letter in enumerate(ascii_lowercase,
                                                         start=1)}


def alphabet_position(text):
    text = text.lower()
    numbers = [let[character] for character in text if character in let]
    return ' '.join(numbers)


print(alphabet_position(input()))
