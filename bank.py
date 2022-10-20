selection=0
balance=100000
deposit=0
withdraw=0
print("====================================================================")
print("                      은행 ATM                                      ")
print("====================================================================")
name=input("계좌 소유자의 이름을 입력해주세요:")
print("1.입금")
print("2.출금")
print("3.잔액확인")
print("4.종료")
print("====================================================================")
selection=int(input("메뉴선택:"))
if selection == 1:
   deposit=int(input("입금할 금액을 입력해주세요:"))
   balance=balance+deposit
   print("\n\n"+str(deposit)+"원이 성공적으로 입금되었습니다.\n\n")
               
elif selection ==2:
     withdraw=int(input("출금할 금액을 입력해주세요:"))
     if withdraw>0 and withdraw<balance:
        balance=balance-withdraw
        print("\n\n"+str(withdraw)+"원이 성공적으로 인출되었습니다.\n\n")
           
     elif withdraw<=0:
          print("\n\n정확한 금액을 입력해주세요.\n\n")

             
     else:
         print("\n\n잔액 부족. 거래 거절되었습니다.\n\n")
elif selection ==3:
   print("\n\n"+name+"님의 현재 잔액은"+str(balance)+"원입니다.\n\n")
else:
   print("이용해주셔서 감사합니다.")
          
while selection !=4:
    print("====================================================================")
    print("                      은행 ATM                                      ")
    print("====================================================================")
    print("1.입금")
    print("2.출금")
    print("3.잔액확인")
    print("4.종료")
    print("====================================================================")
    selection=int(input("메뉴선택:"))
    if selection == 1:
        deposit=int(input("입금할 금액을 입력해주세요:"))
        balance=balance+deposit
        print("\n\n"+str(deposit)+"원이 성공적으로 입금되었습니다.\n\n")
        
    
        
    elif selection ==2:
        withdraw=int(input("출금할 금액을 입력해주세요:"))
        if withdraw>0 and withdraw<balance:
            balance=balance-withdraw
            print("\n\n"+str(withdraw)+"원이 성공적으로 인출되었습니다.\n\n")
           
        elif withdraw<=0:
            print("\n\n정확한 금액을 입력해주세요.\n\n")

             
        else:
            print("\n\n잔액 부족. 거래 거절되었습니다.\n\n")
        
    elif selection ==3:
        print("\n\n"+name+"님의 현재 잔액은"+str(balance)+"원입니다.\n\n")
    else:
        print("이용해주셔서 감사합니다.")
