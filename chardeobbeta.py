# This little program will take a list of char codes and convert to ASCII.
# Natively compatible with Python3.
# Input should appear like the following: char(108)+char(119) or char(118)&char(148). Spaces are acceptable.
import re

print ("For pasting the char string, the input needs to appear as char(118)+char(14) or char(65)&char(59) etc...")

# This takes the users char string and assigns it to a variable, first_list.
first_list = input("Please paste your char string: ")

# This splits up all of the individual chars into a list by separating at the + and the &. Expandable as needed.
second_list = re.split('\&+|\++', first_list)

# This removes all of the non-digit characters with regex, converts to ASCII and rebuilds the line.
def convert_code():
    for line in second_list:
        line = re.sub(r'\D', "", line)
        line = chr(int(line))
        print(line, end="")

# Run the function.
convert_code()
