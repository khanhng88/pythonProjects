"""
print("Hello world" + " Emma " + str(18))
print(f"Hello world Emma {19}")

print(3)
print(-3 * 12)
print(3.123)
"""
# for python: Dynamical type
# float inchToCm = 2.54f
inch_to_cm_factor = 2.54  # snake case, global var (defined outside of methods)
# print(f"1 inch = {1 * 2.54} cm")
# print(f"2 inch = {2 * inch_to_cm_factor} cm")


# parameter
# def inch_to_cm(inch_num):
#     return_value = inch_num * inch_to_cm_factor
#     return return_value


# def do_sth():
#     print(inch_to_cm_factor)


# print(f"{1} inch(es) = {inch_to_cm(1)} cm")
# return_value_1 = inch_to_cm(1)
# print(return_value_1)
# inch_to_cm(3)
# inch_to_cm(4)
# inch_to_cm(5)


def inch_to_cm_input(inch_num):
    print(f"{inch_num} inch(es) = {inch_num * inch_to_cm_factor} cm")


user_input = input("Please input a number: ")
inch_to_cm_input(int(user_input))
