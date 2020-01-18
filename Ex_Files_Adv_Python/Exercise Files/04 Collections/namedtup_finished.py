# Demonstrate the usage of namdtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)
    # Here instead of using namedTuples we could have created a class and 
    # use its data members, but for performing small operations named 
    # tuples are good. 
    # We could have used p1[0] and p1[1] but p.x and p.y are more readable 
    # and that's why we are using them

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
