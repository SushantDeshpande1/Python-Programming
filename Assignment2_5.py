#Write a program which accept one number for user and check whether number is prime or not. 
#Input : 5 Output : It is Prime Number

def CheckPrime(iNo):
    if iNo < 2 :
        print("Number is Not Prime...")
        return

    for i in range(2 , (iNo//2)+1 ):
        if (iNo % i) == 0 :
            print("Number is Not Prime")
            return
    print("Number is Prime")

def main():
    No = int(input("Enter a Number: "))
    CheckPrime(No)

if __name__ == "__main__":
    main()