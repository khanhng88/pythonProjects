"""
if this is true:
    I do this
    And then I do that
else:
    I do another thing
    Then I do this
"""

my_num_str = input("Please input a number: ")
my_num = int(my_num_str)

if my_num <= 5:
    print(f"\t{my_num} is less than 5")
    if my_num % 2 == 0:
        print(f"\t{my_num} is an even num")
    else:
        print(f"\t{my_num} is a odd num")
elif my_num == 5:
    print(f"\t{my_num} is equal to 5")
else:
    print(f"\t{my_num} is greater than 5")


