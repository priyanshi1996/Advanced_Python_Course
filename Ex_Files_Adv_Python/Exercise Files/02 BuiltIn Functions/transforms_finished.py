# use transform functions like sorted, filter, map


def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    #  The filter functions does essentially what its name implies. 
    #  It creates an iterator that filters out values from a given sequence. You pass it a function to perform a Boolean test and if that test returns false, 
    #  then that item is removed from the resulting seque
    odds = list(filter(filterFunc, nums))
    print(odds)
    # Output:[1,5,13,381,47]

    # use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)
    # Output:['a','b','c','e','i','k','l','m','n','o']

    # use map to create a new sequence of values
    #  The map function creates an iterator that takes one or more sequences 
    #  of values and produces a new sequence by applying a given function 
    #  to each value in the original sequences.
    squares = list(map(squareFunc, nums))
    print(squares)
    # Output:[1, 64, 16, 25, 169, 145161, 168100, 3364, 2209]

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()
