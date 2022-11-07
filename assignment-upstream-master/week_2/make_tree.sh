#!/usr/bin/env bash

mkdir s1
cd s1
mkdir s3
mkdir s2
mkdir s2/Advanced

touch s3/conf.txt
touch s2/text_analyzer1.py
touch s2/Advanced/text_analyzer2.py

# Write conf.text file
file="s3/conf.txt"
echo "I love bash scripting" > $file
cat $file


# Write text_analyzer1.py file
# text analyzer1.py should prompt the user for a text string.
# It should then output:
# (1) the number of vowels (aeiou),
# (2) the first vowel,
# (3) the character immediately after the first vowel.

file="s2/text_analyzer1.py"
{
    echo "import re"
    echo "text = raw_input(\"Enter a text string: \").lower()"
    echo "vowels = ['a', 'e', 'i', 'o', 'u']"
    echo "vowels_in_str = [letter for letter in text if letter in vowels]"
    echo "m = re.search(\"a|e|i|o|u\", text)"
    echo "if m is None:"
    echo "  print(\"No Vowels Found\")"
    echo "  exit()"
    echo "si = m.start()"
    echo "ei = m.end()"
    echo "first_vowel = text[si:ei]"
    echo "next_character = text[si+1:ei+1]"
    echo "print(\"vowels: \", len(vowels_in_str))"
    echo "print(\"first vowel: \", first_vowel)"
    echo "print(\"character immediately after first vowel: \", next_character)"
} >> $file



# Write text_analyzer2.py file
# text analyzer2.py should also prompt the use for a text string.
# It should then create a dictionary in which the keys are the five vowels,
# and the values are the number of times each vowel occurs in the text.
# Print the dictionary.

file="s2/Advanced/text_analyzer2.py"
{
    echo "import re"
    echo "text = raw_input(\"Enter a text string: \").lower()"
    echo "vowel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}"
    echo "vowels_in_str = [letter for letter in text if letter in vowel_dict.keys()]"
    echo "for v in vowels_in_str: vowel_dict[v] += 1"
    echo "print(vowel_dict)"
} >> $file

