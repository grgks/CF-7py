s = "Factory"

# print(s[0] * 1 + "*" * 6)
# print(s[1] * 2 + "*" * 5)
# print(s[2] * 3 + "*" * 4)
# print(s[3] * 4 + "*" * 3)
# print(s[4] * 5 + "*" * 2)
# print(s[5] * 6 + "*" * 1)
# print(s[6] * 7 + "*" * 0)


length = len(s)

for i in range(length):
    char = s[i]
    chars = char * (i + 1)
    stars = '*' * (length - i - 1)
    print(chars + stars)