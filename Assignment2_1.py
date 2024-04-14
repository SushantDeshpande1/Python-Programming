#Create on module named as Arithmetic which contains 4 functions as 
#Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.
#All functions accepts two parameters as number and perform the operation.
#Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    iNo1 = int(input("Enter 1st Number : "))
    iNo2 = int(input("Enter 2nd Number : "))

    Addition = Arithmetic.AdditionX(iNo1,iNo2)
    print("Addition Of Above 2 Numbers is : ",Addition)

    Substraction = Arithmetic.SubstractionX(iNo1,iNo2)
    print("Substraction Of Above 2 Numbers is : ",Substraction)
    
    Multiplication = Arithmetic.MultiplicationX(iNo1,iNo2)
    print("Multiplication Of Above 2 Numbers is : ",Multiplication)
    
    Division = Arithmetic.DivisionX(iNo1,iNo2)
    print("Division Of Above 2 Numbers is : ",Division)
    
if __name__ == "__main__":
    main()