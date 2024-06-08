# START
# Get a list of the possible passwords

# UPDATE
# Calculate a good first guess
# let user input number of correct characters
# highlight other words similarites
# crossout words with no similarities
# recommend best choices

import sys

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
similarites: dict = {}
password_length: int = 0

def display_list() -> None:
    global options

    for count, item in enumerate(options):
        count += 1
        print(f'{count}: {item}')

def list_options() -> list[str]:
    word_list: list[str] = []
    global password_length
    
    # Get each option and word length
    while True:
        option: str = input("Enter option (leave blank to finish):")
        
        if not option:
            break

        if password_length == 0:
            con: str = input(f"Confirm {len(option)} is the correct length (y/n)?:")
            
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

def select_option() -> None:
    global options
    global similarites
    
    print("Enter the option you selected")
    display_list()

    index: int = int(input("Selection (-1 to end): ")) - 1
    if index == -2:
        sys.exit()
    
    if index > len(options) or index < 0:
        ...

    similarity: int = input(f"Enter the similarity of {options[index]} out of {password_length}: ")
    similarites[index] = similarity

    print(similarites)

    recommend_options()
    ...

def recommend_options() -> list[str]:
    global options
    global similarites

    if len(similarites) <= 0:
        ...
        return
    
    compare_words: list[str]
    ...

def edit_list() -> None:
    global options

    ...

def main() -> None:
    global options
    global similarites

    print("Welcome to the Fallout Hacking Assistant")
    # get list
    options = list_options()
    # get list and print options

    print("\nWhat would you like to do?")
    print("1. Get Recommendations")
    print("2. Make a selection")
    print("3. Edit list")
    
    while True:
        ans: int = int(input("Enter (-1 to exit): "))

        match ans:
            case 1:
                recommend_options()
            case 2: 
                select_option()
            case 3:
                ...
            case -1:
                sys.exit()
            case _:
                print("Invalid selection! Try again")
                continue


    # recommend first choices

    # enter similarity number for specific target

    # recommend new choices based on similarity

if __name__ == "__main__":
    main()
