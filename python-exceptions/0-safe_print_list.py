#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
<<<<<<< HEAD
            print("{}".format(my_list[i]), end="")
=======
            print(my_list[i], end="")
>>>>>>> Add safe_print_list function
            count += 1
        except IndexError:
            break
    print()
    return count
