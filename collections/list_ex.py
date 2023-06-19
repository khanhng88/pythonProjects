"""
Collections:
list = [] ordered, changeable, dups are OK
set = {} unordered, immutable, add/remove OK but NO dups
tuple = () ordered and unchangeable, dups are OK but FASTER

"""

fruits = ["papaya", "banana", "apple", "coconut", "dragon fruit"]
# print(fruits)
# print(fruits[2])
# print(fruits[0:2])  # return first 2 elements
# print(fruits[:2])  # return first 2 elements
# print(fruits[::2])  # every 2 elements
# print(fruits[::-1])  # reverse elements

# for fruit in fruits:
#     print(fruit)

# print(len(fruits))  # length of collection
# print("banana" in fruits)

# fruits[0] = "apple"  # allow dups in list
# for fruit in fruits:
#     print(fruit)


# fruits.append("lychee")
# fruits.remove("apple")  #  remove first occurence
# print(fruits)
# fruits.insert(0, "guava")  #  insert more values via index
# print(fruits)
# fruits.sort()  # sort the list in Alphabetical order
# print(fruits)

#reverse order compared to the initial order
# fruits.reverse()
# print(fruits)

#clear elements in list
# fruits.clear()
# print(fruits)

# return index of list
print(fruits.index("apple"))
# return the count of elements in list
print(fruits.count("coconut"))
print(fruits.count("mango")) # element not exist in list -> count returns 0
