#Write a program which accept one number from user and return its factorial. 
#Input : 5 Output : 120

def FindFactorial(iNo):
    result = 1
    while iNo > 1:
        result = result * iNo
        iNo = iNo - 1
    return result

def main():
    No = int(input("Enter a Number: "))
    Answer = FindFactorial(No)
    
    print("Factorial of", No , "is", Answer)

if __name__ == "__main__":
    main()