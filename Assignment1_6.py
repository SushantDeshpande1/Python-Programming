#Write a program which accept number from user and check whether that number is 
#positive or negative or zero. 
#Input : 11 Output : Positive Number 
#Input : -8 Output : Negative Number 
#Input : 0 Output : Zero

def CheckPositiveNegativeZero(iNo):
    if(iNo == 0):
        print("Number is Zero")
    elif(iNo > 0):
        print("Number is Positive")
    elif(iNo < 0):
        print("Number is Negative")
    
def main():
    Number = int(input("Enter a Number : "))
    CheckPositiveNegativeZero(Number)

if __name__ == "__main__":
    main()