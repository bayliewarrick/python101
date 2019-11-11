"""
a = [1,2,3,4,5]
sum = 0

for index in range(0,len(a)):
    sum += a[index]
print(sum)
"""

word = "a e tg"
vowels = ['a','e','i','o','u']
vowel_count = 0

for index in range(0,len(word)):
    if word[index] in vowels:
        print(f'the Vowel: {word[index]} was found!')
        vowel_count += 1
print (f"Total number of vowels fonnd: {vowel_count}")