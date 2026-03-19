name = input("Text: ")

for c in name:
    if c not in "aeiouAEIOU":
        print(c, end="")

print()
