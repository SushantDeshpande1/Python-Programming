#Write a program which contains one function that accept one number from user and 
#returns true if number is divisible by 5 otherwise return false. 
#Input : 8 Output : False 
#Input : 25 Output : True

def DivByFive(iNo):
    if (iNo % 5 == 0):
        return True
    else:
        return False

def main():
    Number = int(input("Enter a Number to check if Divisible by 5 : "))
    Result = DivByFive(Number)

    print(Result)

if __name__ == "__main__":
    main()