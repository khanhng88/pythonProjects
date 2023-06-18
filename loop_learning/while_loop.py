"""
while <expression>:
    do sth 1
    do sth 2
    ...
"""

# num = 0
# while num < 5:
#     if num == 3:
#         num += 1
#         continue
#     else:
#         print(num)
#         num += 1


"""
====menu options=========
1. Check even/odd num
2. Get square num
3. exit
"""


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

    if option_num == 1:
        input_num = int(input("Please input num: "))
        is_even = True if input_num % 2 == 0 else False  # ternary operation
        print(f"{input_num} is even number --> {is_even}")

    elif option_num == 2:
        input_num = int(input("Please input num: "))
        print(f"square of {input_num} is {input_num * input_num}")

    elif option_num == 0:
        print("Exit program")
        is_continued = False

    else:
        print("Sorry wrong option.")

    try_times -= 1
    if try_times == 0:
        print("No try times left.")
    else:
        print(f"you have {try_times} times to play this game")



