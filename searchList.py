number=[]

while True:
    print("Enter numbers.(To finish press 'Enter' key)")
    n=input()
    if len(n)==0:
        break
    number.append(float(n))

number.sort()
number_len=len(number)
print("You entered")
print(number)



print("\nmax:"+str(max(number)))
print("min:"+str(min(number)))
number_center=int(number_len/2)
if number_center%2==0:
    print("median: %4.2f"%number[number_center])
else:
     print("median: %4.2f"%float((number[number_center-1]+number[number_center])/2))
