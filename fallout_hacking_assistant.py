# START
# Get a list of the possible passwords

# UPDATE
# Calculate a good first guess
# let user input number of correct characters
# highlight other words similarites
# crossout words with no similarities
# recommend best choices


options: list[str] = []
password_length: int = 0

def main() -> None:
    # Get each option and word length
    while True:
        option: str = input("Enter option (leave blank to finish):")
        if not option:
            break

        if len(password_length) <= 2:
            con: str = input(f"Confirm {password_length} is the correct length (y/n)?:")
            
            if con.lower() != 'y':
                print("Please Retry!")
                continue

            password_length = len(option)
        elif len(option) != password_length:
            print("Incorrect word length")
            continue

        options.append(option)

    # print list
    ...

if __name__ == "__main__":
    main()
