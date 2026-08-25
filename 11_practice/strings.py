# Strings
# Count vowels in a string.
input_string = input('Enter a string: ')
vowels = "aeiouAEIOU"
count =0
for char in input_string:
    if char in vowels:
        count +=1
    else:
        pass
print(f'The number of vowels in the string is {count}')

# Reverse a string.
reversed_string = input_string[::-1]
print(f'The reversed string is {reversed_string}')

# Check if a string is a palindrome.


if input_string == input_string[::-1]:
    print(f"Yes the string {input_string} is a palindrome")
else:
    print(f"No the string {input_string} is not a palindrome")

# Count the occurrences of a character.
character = input('Enter a character to count its occurrences: ')
count= input_string.count(character)
print(f'The character {character} occurs {count} times in the string {input_string}')

# Replace all spaces with _.

new_string = input_string.replace(' ', '_')
print(f"The string with spaces replaced by underscores is: {new_string}")

# Find the longest word in a sentence.

words = input_string.split()
longest_word = max(words, key=len) # this line checks the length of each word and returns the longest one
print(f'The longest word in the string is: {longest_word}')

# Count the number of words in a string.
words = input_string.split()
word_count = len(words)
print(f'The number of words in the string is: {word_count}')


# Capitalize the first letter of every word.
capitalized_string = input_string.title()
print(f'The string with the first letter of each word capitalized is: {capitalized_string}')

# Remove duplicate characters.
unique_characters = list(set(input_string))
print(f'The unique characters in the string are: {unique_characters}')

# Check whether one string is a substring of another

sub_string = (input("enter the substring: "))
if sub_string in input_string:
        print(f"yes {sub_string} is present")
else:
        print(f"yes {sub_string} is not present")
