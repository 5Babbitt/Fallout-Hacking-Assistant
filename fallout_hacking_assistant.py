# START
# Get a list of the possible passwords

# UPDATE
# Calculate a good first guess
# let user input number of correct characters
# highlight other words similarites
# crossout words with no similarities
# recommend best choices

# test variables
test_list_valid: list[str] = ['protecting', 'productive', 'consisting', 'procession', 'aggressive',
                            'prosperity', 'production', 'commission', 'philosophy', 'population',
                            'possession', 'disturbing', 'protection', 'schematics', 'undergoing',
                            'projection', 'initiation']
test_list_invalid: list[str] = ['protecting', 'productive', 'consisted', 'procession', 'aggressively',
                            'prosperity', 'production', 'commission', 'philosopher', 'population',
                            'possession', 'disturbing', 'protection', 'schematics', 'underground',
                            'projection', 'initiation']

test_choice_one: int = 1
test_choice_two: int = 2
test_choice_three: int = 7

test_answer: str = 'production' # if all recommendations contain this then pass

options: list[str] = []
password_length: int = 0

def list_options() -> list[str]:
    word_list: list[str] = []
    
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

        print(f'{option} added')
        word_list.append(option)

    return word_list

def main() -> None:
    # get list
    options = list_options()

    # print list and options

    # recommend first choices

    # enter similarity number for specific target

    # recommend new choices based on similarity
    ...

if __name__ == "__main__":
    main()
