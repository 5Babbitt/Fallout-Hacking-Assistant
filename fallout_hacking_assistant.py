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
password_length: int = 0

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

    for count, item in enumerate(word_list):
        count += 1
        print(f'{count}: {item}')

    return word_list

def select_option() -> str:
    
    ...

def recommend_options() -> list[str]:
    
    ...

def main() -> None:
    print("Welcome to the Fallout Hacking Assistant")
    # get list
    options = list_options()
    # get list and print options

    print("\nWhat would you like to do?")
    print("1. Get Recommendations")
    print("2. Make a selection")
    print("3. Edit list")
    
    while True:
        ans: int = input("Enter (-1 to exit): ")

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
