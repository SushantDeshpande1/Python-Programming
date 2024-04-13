#Write a program which display 5 times Marvellous on screen. 
#Output : 
#Marvellous 
#Marvellous 
#Marvellous 
#Marvellous 
#Marvellous 

def Display(iNo):
    for iCnt in range(iNo):
        print("Marvellous")

def main():
    No = int(input("Enter a Number to Display Marvellous 'No' times on screen : "))
    Display(No)

if __name__ == "__main__":
    main()