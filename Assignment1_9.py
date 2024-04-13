#Write a program which display first 10 even numbers on screen. 
#Output : 2 4 6 8 10 12 14 16 18 20 

def DisplayTable(iNo):
    for i in range(iNo ,(iNo*10)+1 , iNo):
        print(i , end = " ")

def main():
    Number = int(input("Enter a Number : "))
    DisplayTable(Number)

if __name__ == "__main__":
    main()