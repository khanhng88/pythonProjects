"""
Dictionary: a collection of {key: value} pairs. It is ordered, unchangeable, no dups allowed
"""

caps = {"USA": "Washington D.C.",
        "India": "New dehli",
        "China": "Beijing",
        "Vietnam": "hanoi"}
# print(dir(caps))
# get value
# print(caps.get("China"))  # if not exists return none
# input_country = input("Please input your country: ")
# if caps.get(input_country):
#     print(f"The capital for {input_country} is {caps.get(input_country)}")
# else:
#     print(f"The capital for {input_country} does not exist")

# add and update existing {key: value} in dictionary
# caps.update({"Germany": "Berlin"})
# caps.update({"China": "Bei"})
# print(caps)
# caps.popitem()  # pop out the latest item
# print(caps)
# caps.clear()  # clear dictionary
# print(caps)

# print keys and values
# countries = caps.keys()
# capitals = caps.values()
# for country in countries:
#     print(country)
#
# for capital in capitals:
#     print(capital)

for key, value in caps.items():
    print(f"{key}: {value}")