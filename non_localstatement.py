def outer_func():
    outer_var = 111

    # nested func
    def inner_func():
        nonlocal outer_var  # if we want to modify out func var, recall that var with type nonlocal
        outer_var = 222
        print("outer var is: ", outer_var)

    inner_func()
    print(outer_var)


outer_func()
