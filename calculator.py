print("-----------------------------------CALCULATOR---------------------------------")

def add(x,y):
       return x+y

def sub(x,y):
       return x-y

def mul(x,y):
       return x*y

def div(x,y):
       return x/y


Num1=float(input("enter first number "))
Num2=float(input("enter second number "))

print('Enter Choice of operation 1/2/3/4')

ops=int(input('''1)Addition
2)Substraction
3)Multiplication
4)Division \n'''))


if ops==1:
        print(Num1 ,"+" ,Num2 ,"=",add(Num1,Num2))
elif ops==2:
        print(Num1 ,"-" ,Num2 ,"=",sub(Num1,Num2))
elif ops==3:
            print(Num1 ,"*" ,Num2 ,"=",mul(Num1,Num2))
elif ops==4:
            print(Num1 ,"/" ,Num2 ,"=",div(Num1,Num2))
           
else:
     print("Invalid Operation")

  