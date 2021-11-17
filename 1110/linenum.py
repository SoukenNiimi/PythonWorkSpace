import os
file=open('word.txt',"r+")
line=file.readline()
word =[]
i=0
for i in line:
    st1=str(file.readline())
    word.append(st1)

while True:
    inp = str(input("単語を入力してください"))

    if inp == "":
        f = open('word.txt', 'w')
        x=0
        for x in word:
            f.write(str(x) + "\n")
        break
    if inp in word:
        print("既に登録済みです")
    elif inp == "list":
        print(word)
    else:
        word.append(inp)
