text = input("Enter a string: ")

# Normalize (optional: to ignore case and spaces)
text = text.lower().replace(" ", "")

is_palindrome = True

for i in range(len(text)):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

print("Palindrome") if is_palindrome else print("Not a palindrome")
