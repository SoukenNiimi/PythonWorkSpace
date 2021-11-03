while True:
    inp = input("好きな文字を入力してください")
    if inp == '':
        break
    if inp.isnumeric():
        print('数字')
    elif inp.isalpha():
        print("アルファベット")
    elif inp.isalnum():
        print("英数字")
    else:
        print("その他")
1
