"""
indexing: accessing an element in string via []
[start : end : step]
start index is included
end index is excluded
"""

credit_num = "1232-1346-5600"
# print(credit_num[5])
# print(credit_num[0:3])  # start = 0, end = 3
# print(credit_num[:3])  # start = 0, end = 3
# print(credit_num[4:7])
# print(credit_num[4:])  # print out the rest of string start from index 4

# negative indexes
# print(credit_num[-1])  # print out the last char in str

# print(credit_num[::2]) # print out every second char of str

"""
get the last 4 digits of credit number
"""
# last_digits = credit_num[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# reverse string
print(credit_num[::-1])
