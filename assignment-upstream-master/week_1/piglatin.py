# Write a script that translates names into a (simplified) Pig Latin.
# Have your script ask the user for his or her name.
# Move the first letter to the end of the name and add the letters "ay".
# Make sure that only the first letter of your output is capitalized.
# Your script should re-create the following behavior exactly:
# Enter your name: Paul Laskowski
# Aulpay Askowskilay


name = raw_input("Enter a Name: ")
name_list = name.lower().split(' ')
translation = [n[1:] + n[0] + 'ay' for n in name_list]
print(' '.join(translation))

