print("======Sookmyung Cafe======")
print("   1. 아메리카노 1800원   ")
print("   2. 카페라떼 2200원   ")
print("   3. 카페모카 2800원   ")
print("==========================\n\n")
menu=0
load=0
order_total=0
a_price=0
b_price=0
c_price=0
a_order=0
b_order=0
c_order=0
menu_list=[]
while load!='N' or load!= 'n':
      menu=int(input("메뉴를 선택해주세요>>>"))
      if menu==1:
            a_order=a_order+int(input("몇잔을 주문하시겠습니까?>>>"))
            a_price=a_price+(1800*a_order)
            menu_list.append(('아메리카노',a_price,a_order))
            if load!='N' or load!= 'n':
               load=input("주문을 계속 하시겠습니까?(Y/N)>>>")
               print("\n\n")
               if load=='Y' or load=='y':
                   continue
               elif load=='N' or load== 'n':
                     break

      elif menu==2:
            b_order=b_order+int(input("몇잔을 주문하시겠습니까?>>>"))
            b_price=b_price+(2200*b_order)
            menu_list.append(('카페라떼',b_price,b_order))
            if load!='N' or load== 'n':
               load=input("주문을 계속 하시겠습니까?(Y/N)>>>")
               print("\n\n")
               if load=='Y' or load== 'y':
                    continue
               elif load=='N' or load== 'n':
                    break


      elif menu==3:
            c_order=c_order+int(input("몇잔을 주문하시겠습니까?>>>"))
            c_price=c_price+(2800*c_order)
            menu_list.append(('카페모카',c_price,c_order))
            if load!='N' or load!= 'n':
               load=input("주문을 계속 하시겠습니까?(Y/N)>>>")
               print("\n\n")
               if load=='Y' or load== 'y':
                    continue
               elif load=='N' or load== 'n':
                     break                  

      else:
            print("메뉴를 다시 선택해주세요")

print("====주 문 내 역====")

for(name,price,count)in menu_list:
      if count!=0:
            print(" ",name,count,"잔")
print("\n\n==총 "+str(a_order+b_order+c_order)+" 잔,"+str(a_price+b_price+c_price)+" 원==")
print("\n\n이용해주셔서 감사합니다")
            




         



