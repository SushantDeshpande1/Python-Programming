#Write a program which display 10 to 1 on screen. 
#Output : 10 9 8 7 6 5 4 3 2 1

def DisplayReverse(iNo):
    iCnt = iNo
    while iCnt > 0:
        print(iCnt , end =" ")
        iCnt -= 1

def main():
    Number = int(input("Enter a Number : "))
    DisplayReverse(Number)

if __name__ == "__main__":
    main()