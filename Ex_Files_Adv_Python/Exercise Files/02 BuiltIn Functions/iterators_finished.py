# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular interation over the days
    for m in range(len(days)):
        print(m+1, days[m])

    # using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    # It will give data in the form of tuples
    for m in zip(days, daysFr):
        print(m)
    # Output:
    # ('sun','Dim')
    # ('Mon','Lun')
    # and so on


    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")
    # Output:
    # 1 Sun = Dim in French
    # 2 Mon = Lun in French
    # If the two lists are not of the same length then the zip 
    # function terminates when the shortest sequence is exhausted
if __name__ == "__main__":
    main()
