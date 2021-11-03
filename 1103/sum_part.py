input1=int(input("数字1:"))
input2=int(input("数字2:"))
num_sum=0
work=0
if(input1>input2):
    work=input1
    input1=input2
    input2=work

for i in range(input1,input2+1):
    num_sum+=i

print("{}から{}までの合計は{}".format(input1,input2,num_sum))