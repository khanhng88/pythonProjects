"""
format specifier = {:flags} format a value based on what is inserted in flags

.(number)f = round to that decimal places
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use plus sign to indicate positive value
:= = place sign to left most position
:  = insert a space before positive number
:, = comma separator

"""

price1 = 3.145689
price2 = -986000.12
price3 = 12.3
# print(f" price 1 is {price1:.2f}")
# print(f" price 2 is {price2:.3f}")
# print(f" price 3 is {price3:.1f}")
# print(f" price 3 is {price3:013}")
# print(f" price 3 is {price3:<13}")
# print(f" price 3 is {price3:>13}")
# print(f" price 3 is {price3:^13}")
# print(f" price 2 is {price2:+}")
print(f"pice 2 is {price2:,.3f}")
