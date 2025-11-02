# Challenge: Control Flow Practice
# Write a program that asks the user for a number between 1-100.
# If the number is less than 30, print "The number is small."
# If the number is between 30 and 70 (inclusive), print "The number is medium."
# If the number is greater than 70, print "The number is large."        


# Set function to categorize number size
def size_checker():
    """
    Asks the user for a number between 1-100 and categorizes it
    as small, medium, or large. Keeps asking until a valid number is entered.
    """
    while True:
        try:
            number = int(input("Enter a number between 1-100: "))
            if 1 <= number <= 100:
                if number < 30:
                    print("The number is small.")
                elif 30 <= number <= 70:
                    print("The number is medium.")
                else:
                    print("The number is large.")
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Run the size checker function
if __name__ == "__main__":
    size_checker()  