#Simple Calculator for practice

num1= int(input("Enter your first number: "))
num2= int(input("Enter Your Secound Number: "))

opr= input ("enter Your Oprator: ")

#conditions for Opration

if opr == "+":
    output=num1+num2
    
if opr == "-":
    output=num1-num2

if opr =="*":
    output=num1*num2

if opr =="/":
    output=num1/num2
    
print ("Your Answer is: ", output )
