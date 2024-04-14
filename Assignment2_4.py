#Write a program which accept one number form user and return addition of its factors. 
#Input : 12 Output : 16 (1+2+3+4+6)

def AddFactors(iNo):
    result = 0
    for i in range(1 , (iNo//2)+1):
        if (iNo % i) == 0 :
            result = result + i
    print(result)


def main():
    No = int(input("Enter a Number: "))
    AddFactors(No)

if __name__ == "__main__":
    main()