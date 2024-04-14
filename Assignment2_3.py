#Write a program which accept one number from user and return its factorial. 
#Input : 5 Output : 120

def FindFactorial(iNo):
    result = 1
    for i in range(1 , iNo +1):
        result = result * i
    return result

def main():
    No = int(input("Enter a Number: "))
    Answer = FindFactorial(No)
    
    print("Factorial of", No , "is", Answer)

if __name__ == "__main__":
    main()