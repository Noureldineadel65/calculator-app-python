logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
DEFAULT = object()


def calculate(first_number=DEFAULT):
    '''The first number is optional since it checks whether to continue calculation with
    previous calculation or start a new one
    '''
    num_1 = 0
    if first_number is DEFAULT:
        num_1 = input("What's the first number?: ")

    else:
        num_1 = first_number
    print('''
            +
            -
            *
            /
            ''')
    op = input("Pick an operation: ")
    num_2 = input("What's the next number?: ")
    # print(type(num_1), type(num_2), type(op))
    evaluated = eval(str(num_1) + op + num_2)
    print(f"{num_1} {op} {num_2} = {evaluated}")
    return evaluated


continue_calc = "n"
calculated = 0
while True:
    if continue_calc == "y":
        calculated = calculate(calculated)
    else:
        calculated = calculate()
    continue_calc = input(
            f"Type 'y' to continue calculation with {calculated}, or 'n' to start with a new calculation: ")