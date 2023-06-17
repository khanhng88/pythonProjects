def outer_func():
    outer_var = 111

    # nested func
    def inner_func():
        inner_var = 222
        print("outer var is: ", outer_var)
        print("inner var is: ", inner_var)

    inner_func()
    # print("inner var is: ", inner_var)


outer_func()
