
# x= int(input("Enter the number: "))
# print("You chose the number ", x)
# if x not in (1,2,3,4,5,6,7,8,9,10,11,12):
#     raise ValueError("Enter a number between 1 to 12")
# match x:
#     case 1:
#         print("The first month of an year is January.")
#     case 2:
#         print("The second month of an year is February.")
#     case 3:
#         print("The third month of an year is March.")
#     case 4:
#         print("The fourth month of an year is April.")
#     case 5:
#         print("The fifth month of an year is May.")
#     case 6:
#         print("The sixth month of an year is June.")
#     case 7:
#         print("The seventh month of an year is July.")
#     case 8:
#         print("The eighth month of an year is August.")
#     case 9:
#         print("The ninth month of an year is September.")
#     case 10:
#         print("The tenth month of an year is October.")
#     case 11:
#         print("The eleventh month of an year is November.")
#     case 12:
#         print("The twelfth month of an year is December.")
#     # case _:
#     #     print("Please enter a number from 1-12.")


# ########################################################################


# #########################################################

# ##########################################################

# #########################################################

# # x=int(input("Enter the number you want the * table of: "))
# # def multiplication(z,x):
# #         z=x*(i+1)
# #         print(z)
# # x=5
# # multiplication(x)

# # for i in range(10):    
# #     z=x*(i+1)
# #     print(z)



def add():
    x=int(input("Enter your number:     "))
    for i in range(1,11):
        multiply=x*i
        print(multiply)
add()
