from spellchecker import SpellChecker

def check_spelling(text):
    spell = SpellChecker()

    paragraphs = text.split('\n')

    for i, paragraph in enumerate(paragraphs, start=1):
        words = paragraph.split()
        misspelled_words = spell.unknown(words)

        if misspelled_words:
            print(f"Oops! Looks like we found some spelling errors in paragraph {i}:")
            for word in misspelled_words:
                suggestions = spell.candidates(word)
                print(f"{word}: Possible corrections - {suggestions}")

                replace_option = input(f"Do you want to fix '{word}'? (yes/no): ").lower()
                if replace_option == 'yes':
                    corrected_word = suggestions[0] if suggestions else word
                    paragraph = paragraph.replace(word, corrected_word)

            paragraphs[i - 1] = paragraph
        else:
            print(f"Great news! No spelling errors found in paragraph {i}.")

    corrected_text = '\n'.join(paragraphs)
    print("\nAwesome! Here's your corrected text:")
    print(corrected_text)

if __name__ == "__main__":
    print("Welcome to the Spell Checker Script!")
    
    user_input = input("Please enter the text you'd like us to check for spelling errors:\n")
    check_spelling(user_input)
