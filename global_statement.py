global_var = 1


def print_sth():
    global global_var  # if we want to modify the global var, need to mention type Global
    global_var = 2
    print(global_var)


print_sth()
print(global_var)
