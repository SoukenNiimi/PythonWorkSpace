num=input("整数を入力してください")
n=int(num)
a=sum(range(n+1))
print("1~{}までの合計:{}".format(n,a))
avg=a/n
print("平均:{}".format(avg))
