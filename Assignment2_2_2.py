def Display(iNo):
    # Construct a string of iNo asterisks separated by spaces
    asterisk_row = "* " * iNo
    
    # Print the constructed row iNo times
    for i in range(iNo):
        print(asterisk_row)

def main():
    No = int(input("Enter a Number: "))
    Display(No)

if __name__ == "__main__":
    main()
