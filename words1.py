def print_menu():
    print("\n*********************************************************")
    print("*                Sookmyung Dictionary                   *")
    print("*********************************************************")
    print("                    1. Save words                        ")
    print("                    2. Delete words                      ")
    print("                    3. Print all words                   ")
    print("                    4. Exit                              ")
    print("=========================================================")
    print("select>>", end='')

def save_words():
    global words
    print("Enter word to save(Press 'enter' key to finish)\n")
    while True:
        word=input("Word: ")
        if len(word)==0:
            break
        
        elif word in words:
            word=True
            print("Already Exist")
            
        else:
            words.append(str(word))
            

        

def delete_words():
    global words
    print("Enter word to delete")
    while True:
        word=input("Word: ")
        if word in words:
            words.remove(word)
            print("Deletion complete")
            break
        else:
            print("No Exist")
    

def print_words():
    print()
    for (name)in words:
        print(name)

select=0
print_menu()
words=[]
while(select !=4):
    select=int(input())
    if select==1:
        save_words()
    elif select==2:
        delete_words()
    elif select==3:
        print_words()
    elif select ==4:
        break
    else:
        print("You entered wrong menu")
    print_menu()


    
        
