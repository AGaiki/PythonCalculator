import math
print("Welcome to my calculator! Input two numbers and a sign, and this program will compute it!") #Instructions
print('\n\n') 

userInput = input("Want to calculate? C to begin!\n")
if(userInput == "C" or userInput == "c"):
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    sign = input("Sign: ")

  
    if(sign == "+" or sign == "plus"):
      print(num1, "+",  num2, '=', num1+num2)
    if(sign == "-" or sign == "minus"):
      print(num1, "-",  num2, '=', num1-num2)
    if(sign == "*" or sign == "X" or sign == "times" or sign == "x"):
      print(num1, "X",  num2, '=', num1*num2)
    if(sign == "/" or sign == "divide"):
      if(num2 == 0):
        print(num1, "÷",  num2, '= undefined') 
      else:
        print(num1, "÷",  num2, '=', num1/num2)
    if(sign == "%" or sign == "percentage"):
      if(num2 == 0):
        print('undefined') 
      else:
        print(num1, "÷",  num2, '=', num1/num2*100, "%")
else:
  print("Goodbye! Have a nice day!")
