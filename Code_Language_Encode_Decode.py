print("Do you want to encode or decode?\n" "Press 1 to encode__.\n" "Press 2 to decode__.")
choice = int(input("Your choice is:  "))
if choice not in (1,2):
    raise ValueError("Please enter 1 for Encode and 2 for Decode.")
#Encode
if choice ==1:
    eng = input("Enter your word:   ")
    print(f"Your entered word is \"{eng}\".")
#If more than three letter word
    if len(eng)>=3:
        ran1=input("Enter first three random letters for encoding: ")
        if len(ran1)!=3:
            raise ValueError("Enter three letters.")
        ran2=input("Enter second three random letters for encoding: ")
        if len(ran2)!=3:
            raise ValueError("Enter three letters.")
        for i in eng:
            a= eng[0]
            b= eng[1:]
            word= ran1+b+a+ran2
        print(f"Your encoded word is \"{word}\".")
#If two letter word
    elif len(eng)==2:
        eng=eng[::-1]
        print(eng)
#If one lettered word
    elif len(eng)==1:
        print(f"Your word is too short to encode, your word is \"{eng}\".")
    if " " in eng:
        raise ValueError("Please enter a single word, your word cannot have spaces. ")
elif choice ==2:
#Decode
    cod= input("Enter encoded word:   ")
    cod_ran = cod[3:-3]
    for i in cod_ran:
        final_word= cod_ran[-1] + cod_ran[0:-1]
    print(f"Your decoded word is \"{final_word}\".")
    
