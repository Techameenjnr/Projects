with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()
for index, word in enumerate(words):
    if word == "(hex)":
        a = words[index - 1]  
        words[index - 1] = str(int(a, 16))
        words.pop(index)
        text = " ".join(words)
















with open("result.txt", "w") as file:
    file.write(text)
