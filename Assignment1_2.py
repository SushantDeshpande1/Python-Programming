#Write a program which contains one function named as ChkNum() 
#which accept one parameter as number. If number is even then it should display “Even number” 
#otherwise display “Odd number” on console. 
#Input : 11 Output : Odd Number 
#Input : 8 Output : Even Number

def ChkNum(iNo):
    if (iNo == 0):
        print("Number is Zero")
    elif (iNo % 2 == 0):
        print("Even Number...")
    elif(iNo % 2 != 0):
        print("Odd Number...")
    
def main():
    Number = int(input("Enter a Number : "))
    ChkNum(Number)

if __name__ == "__main__":
    main()