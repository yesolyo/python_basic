n=int(input("숫자를 입력해주세요:"))
      
for i in range(1,n+1):      
    if i%2==0 and i%3== 0 :
        continue
    elif i ==n+1 :
        break
    print(i)
