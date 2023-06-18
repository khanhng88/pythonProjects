start = 1
stop = 5  # stop limit -> it is excluded
step = 2
my_range = range(start, stop, step)

for num in my_range:
    print(f"Number {num}")


# start = 1
# stop = 5  # stop limit -> it is excluded
# step = 2
# my_range = range(start, stop, step)

for num in range(10):
    if num == 4:
        continue
    print(f"Number {num}")




