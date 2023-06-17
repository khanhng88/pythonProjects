global_var = 1


# any var declared outside funcs can be accessed globally
def print_stn():
    print(global_var)


print_stn()
print(global_var)
print(True)
