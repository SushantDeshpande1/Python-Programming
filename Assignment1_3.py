#Write a program which contains one function named as Add() which accepts two numbers from user and 
#return addition of that two numbers. 
#Input : 11 5 Output : 16

def Add(iNo1,iNo2):
    Sum = iNo1 + iNo2
    return Sum

def main():
    print("Addition Of 2 Numbers...")

    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Addition = Add(No1,No2)

    print("Addition is : ",Addition)

if __name__ == "__main__":
    main()