#Write a program which accept number from user and print that number of “*” on screen. 
#Input : 5 Output : * * * * *

def DisplayPattern(iNo):
    iCnt = 0
    while iCnt < iNo:
        print("*", end = " ")
        iCnt += 1

def main():
    Number = int(input("Enter a Number : "))
    DisplayPattern(Number)

if __name__ == "__main__":
    main()