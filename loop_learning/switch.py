"""
match subject:
    case pattern 1:
        <action>

    case pattern 2:
        <action>

    case _:
        <action wildcard>

"""

# input_num = int(input("Please input a day: "))
#
# match input_num:
#     case 2 | 3 | 4 | 5 | 6:
#         print("weekdays")
#     case 7 | 8:
#         print("weekends")
#     case _:
#         print(f"{input_num} has no definitions")


def print_menu():
    print("\n=== Menu options ===")
    print("1. Check even/odd num")
    print("2. Get square num")
    print("3. exit")


is_continued = True
try_times = 3
while is_continued and try_times > 0:
    print_menu()
    option_num = int(input("Please select an option: "))

    match option_num:
        case 1:
            input_num = int(input("Please input num: "))
            is_even = True if input_num % 2 == 0 else False  # ternary operation
            print(f"{input_num} is even number --> {is_even}")

        case 2:
            input_num = int(input("Please input num: "))
            print(f"square of {input_num} is {input_num * input_num}")

        case 0:
            print("Exit program")
            is_continued = False

        case _:
            print("Sorry wrong option.")

    try_times -= 1
    print(f"you have {try_times} times to play this game")
