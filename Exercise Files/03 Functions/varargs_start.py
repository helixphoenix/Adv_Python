# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*numbers):
    res=""
    for num in numbers:
        res+=str(num)
    return res


def main():
    # TODO: pass different arguments
    print(addition(243,3535,46546,4141,37,27,23,43,28,18,17,49))

    # TODO: pass an existing list

    existing_plans_are_not_my_failure=[5,10,15,20] 
    print(addition(*existing_plans_are_not_my_failure))
if __name__ == "__main__":
    main()
