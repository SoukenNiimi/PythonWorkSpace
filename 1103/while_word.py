import os
word=[]
file=open('word.txt',w)
word=[file]

while True:
    inp = str(input("単語を入力してください"))

    if inp == "":
        break
    if inp in word:
        print("既に登録済みです")
    elif inp == "list":
        print(word)
    else:
        word.append(inp)
