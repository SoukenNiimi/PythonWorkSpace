while True:
    inp = input("好きな文字を入力してください")
    if inp == '':
        break
    if inp.isnumeric():
        print('数字')
    elif inp.isalpha():
        print("アルファベット")
    else:
        print("その他")
1