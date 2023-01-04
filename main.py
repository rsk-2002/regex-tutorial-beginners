# Import the module
import re

# text to search
sentence = "This is and amazing world and I like it"

# what to search for
pattern = re.compile(r'..d')

# methods

# findall() - return list

match_list = re.findall(pattern, sentence)

# print(match_list)


# search() - first match
first_match = re.search(pattern, sentence)
# print(first_match)

# match() - beginning

word = re.match(pattern, sentence)
# print(word)


# sub()

new_str = re.sub(pattern, 'mad', sentence)

# print(new_str)
# print(sentence)

# finditer()

matches = pattern.finditer(sentence)

# print(matches)

for match in matches:
    print(match)