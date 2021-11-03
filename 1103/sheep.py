import time
while True:
    inp=int(input("何匹数えますか？"))
    cou = 1
    if inp>100:
        print("100匹まででお願いしますm(_ _)m")
    else:
        break

while True:
    print("羊が{}匹".format(cou))
    time.sleep(2)
    cou+=1
    if cou>=inp+1 :
        break