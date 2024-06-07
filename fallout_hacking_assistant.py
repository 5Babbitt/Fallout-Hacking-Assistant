# START
# Get a list of the possible passwords

# UPDATE
# Calculate a good first guess
# let user input number of correct characters
# highlight other words similarites
# crossout words with no similarities
# recommend best choices

options: list[str]
password_length: int

def main() -> None:
    while True:
        option: str = input("Enter option (leave blank to finish):")
        if len(option) <= 0 or option is None:
            break

        if len(password_length) <= 0 or password_length is None:
            password_length = len(option)
        elif len(option) != password_length:
            print("Incorrect word length")
            continue

    ...

if __name__ == "__main__":
    main()
