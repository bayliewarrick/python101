letters_reversed = []
word_letters = []
def is_palindrome():
    word = input("Enter a word to determine whether or not the given word is a palindrome.").lower()
    for letter in word:
        word_letters.append([letter])
    for letter in word:
        letters_reversed.insert(0,[letter])
    if letters_reversed == word_letters:
        print("This word IS a palindrome!")
    else:
        print("Not a palindrome. Try again!")
is_palindrome()