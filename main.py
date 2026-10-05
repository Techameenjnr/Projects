with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()
# print(words)
    for index, word in enumerate(words):
    # print(f"{index}: {word}")
     if word == "(hex)":
        a = words[index - 1]  
        words[index - 1] = str(int(a, 16))
   

    if word == "(bin)":
        b = words[index - 1]
        words[index - 1] = str(int(b, 2))

    if word == "(up)":
        u = words[index - 1]
        words[index - 1] = u.upper()
    
    if word == "(low)":
        l = words[index - 1]
        words[index - 1] = l.lower()
       

words.pop(index)
print(words)
text = " ".join(words)




with open("result.txt", "w") as file:
    file.write(text)

    with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()

for index, word in enumerate(words):
    if word == "(hex)":
        a = words[index - 1]
        words[index - 1] = str(int(a, 16))

    if word == "(bin)":
        b = words[index - 1]
        words[index - 1] = str(int(b, 2))

    if word == "(up)":
        u = words[index - 1]
        words[index - 1] = u.upper()

    if word == "(low)":
        l = words[index - 1]
        words[index - 1] = l.lower()

words = [word for word in words if word not in ["(hex)", "(bin)", "(up)", "(low)"]]

print(words)

text = " ".join(words)

with open("result.txt", "w") as file:
    file.write(text)
