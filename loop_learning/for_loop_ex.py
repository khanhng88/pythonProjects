user_input_str = input("Please input a number: ")
user_input_num = int(user_input_str)
total = 0

for num in range(user_input_num + 1):
    if num % 2 == 0 and num != 0:
        print(num)
        total += num
print(f"Total of even numbers is: {total}")
