#creating dictonary project\
balance = 500

while True:
    user_input=int(input("""
1.check balance
2.deposite money
3.withdraw money
4.close program\n\t"""))
    
    
    if user_input==1:
        print(f"THE CURRENT AMOUNT OF YOUR BANK IS {balance}")
    
    elif user_input==2:
       money=float(input("enter the money deposite\n"))
       balance+=money
       print(f"THE CURRENT AMOUNT OF YOUR BANK IS {balance}")
    elif user_input==3:
        money=float(input("enter the money to withdraw\n "))
        
       
        if balance<=money:
            print("INVALIAD BANK BALANCE")
            continue
        balance-=money
        print(f"THE CURRENT AMOUNT OF YOUR BANK IS {balance}")
    elif user_input==4:
       break
    