name = "Alex"
print(name)
# LEGB rule: local (function) -> Enclosing -> global -> built in


def inch_to_cm():
    example_input_value = 10
    convert_value = example_input_value * 2.54 # local var or function var
    print(f"10 inches is equal to {convert_value} cm")


print(convert_value)
inch_to_cm()
