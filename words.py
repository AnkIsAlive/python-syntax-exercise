# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)
def print_upper_words(words):
    """Prints words all uppcase"""
    for word in words:
        print(word.upper())


# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def print_upper_e(words):
    """
    Prints words uppcase that start with e or E
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
def print_upper_specific(words, must_start_with):
    """
    Print words uppcase that start with given letters
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
