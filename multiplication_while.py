n=int(input("숫자를 입력해주세요:"))
i=0
while i<=n+1:
    i=i+1
    if i%2==0 and i%3== 0 :
        continue
    elif i==n+1:
        break
    print(i)
