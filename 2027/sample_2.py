fruits = ['バナナ','リンゴ','オレンジ']
while True:
    instr =str(input("果物をカタカナで入力してください"))
    if instr=='':
        break
    if instr in fruits :
        print("{}は、知っています！" .format(instr))
    else :
        print("{}は、知りませんでした。覚えておきます" .format(instr))
        fruits.append(instr)

print('知っている果物')
print(fruits)