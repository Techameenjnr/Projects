with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()
# print(words)
for index, word in enumerate(words):
    # print(f"{index}: {word}")
    if word == "(hex)":
        a = words[index - 1]  
        words[index - 1] = str(int(a, 16))
        words.pop(index)

    if word == "(bin)":
        b = words[index - 1]
        words[index - 1] = str(int(b, 2))
        words.pop(index)
    if word == "(up)":
        u = words[index - 1]
        words[index - 1] = u.upper()
        words.pop(index)
    if word == "(low)":
        l = words[index - 1]
        words[index - 1] = l.lower()
        words.pop(index)


print(words)
text = " ".join(words)



with open("result.txt", "w") as file:
    file.write(text)
