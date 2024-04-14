#Write a program which accept one number and display below pattern. 
#Input : 5 
#Output : 
# * * * * * 
# * * * * *
# * * * * * 
# * * * * * 
# * * * * * 

def Display(iNo):
    for i in range(iNo):
        for j in range(iNo):
            print(" * ",end = " ")
        print()

def main():
    No = int(input("Enter a Number : "))
    Display(No)


if __name__ == "__main__":
    main()