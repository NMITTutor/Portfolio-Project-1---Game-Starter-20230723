"""_summary_
"""
import sys


def fizz_buzz(upto):
    """_summary_

    Args:
        upto (_type_): _description_
    """

    the_list_of_tuples = []
    i = 0
    while i < upto:
        # for i in range(upto):
        if i % 3 == 0 and i % 5 == 0:
            the_list_of_tuples.append((i, 'FizzBuzz'))
        elif i % 3 == 0:
            the_list_of_tuples.append((i, 'Fizz'))
        elif i % 5 == 0:
            the_list_of_tuples.append((i, 'Buzz'))
        else:
            the_list_of_tuples += [(i, str(i))]

        i += 1

    return the_list_of_tuples


def fizz_buzz_in_general(upto, fizzMultiple, buzzMultiple):
    return [(i, "FizzBuzz") if i % fizzMultiple == 0 and i % buzzMultiple == 0 else
            (i, "Fizz") if i % fizzMultiple == 0 else
            (i, "Buzz") if i % buzzMultiple == 0 else
            (i, str(i))
            for i in range(upto)]

    pass


if __name__ == "__main__":
    # for a_tuple in fizz_buzz(10):
    #    print(a_tuple)
    try:
        list_of_command_line_arguments = sys.argv
        print(list_of_command_line_arguments)
        if len(list_of_command_line_arguments) == 4:
            upto, fizz, buzz = map(int, list_of_command_line_arguments[1:])
            # upto, fizz, buzz = [int(list_of_command_line_arguments[i])
            #                    for i in [1, 2, 3]]
            # Using list comprehension
            for a_tuple in fizz_buzz_in_general(upto, fizz, buzz):
                print(a_tuple)
        else:
            raise ValueError
    except ValueError:
        print("Run fizzbuzzes with three integer parameters like this: python -m fizzbuzzes upto<integer> fizz<integer> buzz<integer>")
    pass
