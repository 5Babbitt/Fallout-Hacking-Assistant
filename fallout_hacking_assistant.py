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

def display_list(given_list: list) -> None:
    for count, item in enumerate(given_list):
        count += 1
        print(f'{count}: {item}')

def list_options(list_options: list[str] = None) -> list[str]:
    word_list: list[str] = []
    global password_length
    
    print("Enter new list: ")

    # Get each option and word length
    while True:
        option: str = input("Enter option (leave blank to finish): ")
        
        if not option:
            break

        if password_length == 0:
            con: str = input(f"Confirm {len(option)} is the correct length (y/n)?: ")
            
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
    global password_length
    
    print("Enter the option you selected")
    display_list(options)

    index: int = int(input("Selection (-1 to end): ")) - 1
    if index == -2:
        sys.exit()
    
    if index > len(options) or index < 0:
        # Error message
        ...

    similarity: int = input(f"Enter the similarity of {options[index]} out of {password_length}: ")
    similarites[options[index]] = int(similarity)

    print(similarites)

    #recommend_options()

def recommend_options() -> list[str]:
    global options
    global similarites

    if not similarites:
        recommend_first_options()
        return
    
    recommendation_list: list[str] = options

    for i, j in similarites.items():
        old_list: list[str] = recommendation_list
        new_list: list[str] = []

        for name in options:
            if name == i:
                continue

            score: int = 0
            for x, char in enumerate(name):
                if char == i[x]:
                    score += 1

            if score == j:
                new_list.append(name)

        recommendation_list = [value for value in new_list if value in old_list]

    print("These are your recommendations:")
    display_list(recommendation_list)
    con = input("\nPress Enter to continue...")

def recommend_first_options() -> None:
    global options
    scores: dict = {}

    for name in options:
        score: int = 0
        for comparison in options:
            if name == comparison:
                continue
            for i, char in enumerate(name):
                if char == comparison[i]:
                    score += 1
        scores[name] = score
    
    # loop through dictionary and find the 5 highest scores
    recommendations: list[str] = [''] * 5

    for i, j in enumerate(recommendations):
        candidate: str = j

        for x, y in scores.items():
            if x in recommendations:
                continue

            if candidate not in scores:
                candidate = x
                continue

            if scores[candidate] < y:
                candidate = x
    
        recommendations[i] = candidate

    print("\nRecommended first guesses:")
    display_list(recommendations)
    con = input("\nPress Enter to continue...")

def edit_list() -> None:
    global options

    ...

def main() -> None:
    global options
    global similarites
    global password_length

    print("Welcome to the Fallout Hacking Assistant")
    print("1. Use test list")
    run: int = input("Enter (leave empty to operate as normal): ")

    # get list and print options
    if run == 1:
        options = test_list_valid
        password_length = len(options[0])
    elif run == -1:
        sys.exit()
    else:
        options = list_options()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Get Recommendations")
        print("2. Make a selection")
        print("3. Edit list")
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
                print("\nInvalid selection! Try again")
                continue

    # enter similarity number for specific target

    # recommend new choices based on similarity

if __name__ == "__main__":
    main()
