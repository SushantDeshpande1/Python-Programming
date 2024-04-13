#Write a program which display first 10 even numbers on screen. 
#Output : 2 4 6 8 10 12 14 16 18 20 

def DisplayTable(iNo):
    iVar = iNo
    iCnt = iNo * 10
    while (iNo <= iCnt):
        print(iNo ,end = " ")
        iNo += iVar

def main():
    Number = int(input("Enter a Number : "))
    DisplayTable(Number)

if __name__ == "__main__":
    main()