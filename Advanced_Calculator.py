print("Please choose a number for options: \n1. Addition \n2. Subtraction \n3. Division \n4. Float division " \
"\n5. Multiplication \n6. Power of \n7. Modulus")
choice=int(input("Your choice is: "))
if choice not in (1,2,3,4,5,6,7): 
    raise ValueError("Please choose a number from fiven choices")

numsum=[]
numsub=[]
nummul=[]

#Addition
if choice==1:
    while True:
        add=input("Please enter a number to add, press \"Done\" when finished: ")
        if add.lower()=="done": break
        add=int(add)
        numsum.append(add)

    total=sum(numsum)
    print(f"Your total is {total}.")

#Subtraction
if choice==2:
    while True:
        sub=input("Please enter numbers to subtract, press \"Done\" when finished: ")
        if sub.lower()=="done": break
        sub=int(sub)
        numsub.append(sub)

    minus=min(numsub)
    print(f"Your subtraction is {minus}.")

#Division
if choice==3:
    while True:
        a=input("Enter first number to Divide, press \"Done\" to cancel: ")
        if a.lower()=="done": break
        b=input("Enter second number to Divide, press \"Done\" when finished: ")
        if b.lower()=="done": break
        div=int(a)
        div2=int(b)
        divide=div/div2
        print(f"Division of {a} with {b} ({a}/{b}) is, {divide}.")

#Float division
if choice==4:
    while True:
        c=input("Enter first number to Float Divide, press \"Done\" to cancel: ")
        if c.lower()=="done": break
        d=input("Enter second number to Float Divide, press \"Done\" when finished: ")
        if d.lower()=="done": break
        fdiv=int(c)
        fdiv2=int(d)
        fdivide=fdiv//fdiv2
        print(f"Float Division of {c} with {d} ({c}//{d}) is, {fdivide}.")

#Multiplication
if choice==5:
    while True:
        mul=input("Please enter numbers to multiply, press \"Done\" when finished: ")
        if mul.lower()=="done": break
        mul=int(mul)
        nummul.append(mul)
    result=1
    for num in nummul:
        result= result*num
    print(f"Multiplication of numbers is {result}.")

# Power of
if choice==6:
    while True:
        a=input("Enter the Base number, press \"Done\" to cancel: ")
        if a.lower()=="done": break
        b=input("Enter the power, press \"Done\" when finished: ")
        if b.lower()=="done": break
        numm=int(a)
        pow=int(b)
        power=numm**pow
        print(f"The value of {a} raised to the power {b} is, {power}.")

# Modulus
if choice==7:
    while True:
        a=input("Enter the first number, press \"Done\" to cancel: ")
        if a.lower()=="done": break
        b=input("Enter the second number, press \"Done\" when finished: ")
        if b.lower()=="done": break
        mod1=int(a)
        mod2=int(b)
        modulus=mod1%mod2
        print(f"The modulus of {a} with {b} ({a}%{b}) is, {modulus}.")
