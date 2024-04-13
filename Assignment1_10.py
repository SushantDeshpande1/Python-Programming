#Write a program which accept name from user and display length of its name. 
#Input : Marvellous Output : 10

def StringLength(name):
    length = 0
    for char in name:
        length += 1
    return length

def main():
    string1 = input("Enter Word to count length : ")
    Result = StringLength(string1)

    print(Result)

if __name__ == "__main__":
    main()