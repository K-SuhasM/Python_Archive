ques= ["What is the capital of France? ", 
       "Which planet is known as the Red Planet? ", 
       "How many days are there in a leap year? ", 
       "Which animal is known as the King of the Jungle? "]
ans1= ['1. Madrid ', "2. Berlin ", "3. Paris ", "4. Rome "]
ans2= ["1. Venus ", "2. Jupiter ", "3. Saturn ", "4. Mars "]
ans3= ["1. 365 ", "2. 364 ", "3. 360 ", "4. 366 "]
ans4= ["1. Tiger ", "2. Elephant ", "3. Bear ", "4. Lion "]

prize=[]
answers=[]

#Question 1
print("Question 1. ", ques[0])
for i in ans1:
    print(i)

inp1=int(input("Enter your answer: "))
if inp1==3:
    answers.append(1)
    prize.append(500)
    print("correct!!", "You won ", "Rs.", prize[0] )
else:
    prize.append(00)
    print("Sorry, you lost", "Your winning amount is Rs.", prize[0]),

#Question 2
if 1 in answers:
    print("Question 2. ", ques[1])
    for i in ans2:
      print(i)

    inp2=int(input("Enter your answer: "))
    if inp2==4:
        answers.append(1)
        prize.append(500)
        print("correct!!", "You won ", "Rs.", sum(prize))
    else:
        answers.pop()
        prize.append(00)
        print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))

#Question 3
if 1 in answers:
    print("Question 3. ", ques[2])
    for i in ans3:
      print(i)

    inp3=int(input("Enter your answer: "))
    if inp3==4:
        answers.append(1)
        prize.append(500)
        print("correct!!", "You won ", "Rs.", sum(prize))
    else:
        answers.pop()
        answers.pop()
        prize.append(00)
        print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))

#Question 4
if 1 in answers:
    print("Question 4. ", ques[3])
    for i in ans4:
      print(i)

    inp4=int(input("Enter your answer: "))
    if inp4==4:
        answers.append(1)
        prize.append(500)
        print("correct!!", "You won ", "Rs.", sum(prize))
    else:
        answers.pop()
        answers.pop()
        answers.pop()
        prize.append(00)
        print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))
