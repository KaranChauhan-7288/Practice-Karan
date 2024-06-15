#  Find input number is odd or even

# print("Enter your number and find out that it's odd or even :   ")
# num= int(input())

# if num % 2 == 0:
#     # Input : Even
#     print("Even") 
# else:
#     print("Odd")
# # Output: Odd



#  BMI 2.0 


# weight= float(input("Enter your weight in KG:   "))
# height= float(input("Enter your height in Meter:    "))
# method 1
# height2= 2*height
# BMI = weight/height2
# if BMI < 18.5 :
#     print("You are underweight")
# elif BMI > 18.5 and BMI <= 25 :
#     print("You are normal in weight:")
# elif BMI > 25 and BMI <= 30:
#     print("You are over wight:")
# elif BMI >30 and BMI <=35:
#     print("You are obese in weight")
# elif BMI >35 :
#     print("Sorry, You are clinically obese in weight:")
# print("Thanks")

# Method 2
# BMI= round(weight/height**2)

# if BMI < 18.5 :
#     print("You are underweight")
# elif BMI > 18.5 and BMI <= 25 :
#     print("You are normal in weight:")
# elif BMI > 25 and BMI <= 30:
#     print("You are over wight:")
# elif BMI >30 and BMI <=35:
#     print("You are obese in weight")
# elif BMI >35 :
#     print("Sorry, You are clinically obese in weight:")
# print("Thanks")


#  Findout input year is leap year or Not
# Check if the year is evenly divisible by 4.
# If true, check if the year is evenly divisible by 100.
# If true, check if the year is evenly divisible by 400.
# Based on these checks, determine if the year is a leap year or not.

# year=int(input("Enter year: "))

# if year % 4 == 0:    # Here % is modulo, if it divided by 4 gives 0 else 1
#      print("Leap year")   #"Number is divided by 4 "
# elif year% 100 == 0:
#      print("Leap year")   # Number is divided by 100
# elif year % 400== 0:
#      print("Leap year")     #   Number is divided by 400
    
# else:
#      print("Not a Leap year")   #number is not divided by 4,100 & 400
     

    # 3.4 Pizza Order
# size=str(input("Select your size of pizza in S/M/B  form:    "))
# bill=0
# toppings=str(input("Want toppings of pepperoni then enter Y / N :   "))
# extra_cheese=str(input("You want extra cheese Y/N : "))
# if size == "S":
#     bill=15 
#     if toppings == "Y":
#         bill += 2  
#     if extra_cheese == "Y":
#             bill += 1
#     print(f"Your totoal bill is {bill}") 
# if size == "M":
#     bill=20 
#     if toppings == "Y":
#         bill += 3  
#     if extra_cheese == "Y":
#             bill += 1
#     print(f"Your totoal bill is {bill}") 
# if size == "B":
#     bill=25 
#     if toppings == "Y":
#         bill += 3  
#     if extra_cheese == "Y":
#             bill += 1
#     print(f"Your totoal bill is {bill}") 



# Logical operator AND , OR , & Not :
# height=int(input("Enter your height to check :  "))

# if height >120 :
#     print("Congrats you are eligable for ride:") 
#     age= int(input("Enter your age to get tickets: "))
    
#     if age <12:
#         ticket = 5
#         print(f"Tour ticket is ${ticket}.")
#     if age>12 and age<18:
#         ticket = 7
#         print(f"Tour ticket is ${ticket}.")
#     if age >18 and age<45:
#         ticket=12
#         print(f"Tour ticket is ${ticket}.")
#     if age >45 and age<55:
#         ticket=0
#         print(f"Tour ticket is ${ticket}.")
#     else:
#         print("Your are not allowerd due to health restiction.")
    
#     photos=str(input("Want photos ans in Y/N :  "))
#     if photos== "Y":
#      ticket+= 3
#      print(f"your final ticket is {ticket}$")
                                                         
# else:
#     print("Sorry, you are not allowed in this ride.")



# Love calculator
