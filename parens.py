print("Enter some text with parentheses located somewhere inside.")
print()

print("Valid input example:")
print("  JSON (JavaScript Object Notation) is an open file format to organize and structure data.")
print()

print("Invalid input examples:")
print("  Wrong order )WRONG( of parentheses.")
print("  Unmatched ) parenthesis.")
print("  Unmatched ( parenthesis.")
print()

user_data = input("Enter text: ")

if "(" not in user_data or ")" not in user_data:
    print("Error, invalid user data. You must provide a pair of parenthesis grouping some text as input. Exiting.")
    exit(0)

# Check if the parentheses are in the wrong order
if user_data.index(")") < user_data.index("("):
    print("Error, the parentheses are not in the right order. Exiting.")
    exit(0)

# Find where ( starts and ) ends / Add 1 to not include include (
beginParen = user_data.index("(") + 1
endParen = user_data.index(")")

# Get the text between ( and )
insideText = user_data[beginParen:endParen]

# Print text from between parens
print(insideText)

# Collect and print the text with parentheses included
text_with_brackets = user_data[beginParen - 1:endParen + 1]
print(text_with_brackets)




