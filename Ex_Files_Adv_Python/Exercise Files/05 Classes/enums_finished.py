# define enumerations using the Enum base class

from enum import Enum, unique, auto


# In Enums we can not have duplicate name, however value can be duplicate
# In order to prevent duplicate values we can use @unique decorator
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE) # Fruit.APPLE
    print(type(Fruit.APPLE)) # <enum 'Fruit'>
    print(repr(Fruit.APPLE)) # <Fruit.APPLE :1>

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value) # APPLE 1

    # print the auto-generated value
    print(Fruit.PEAR.value) # 5

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA]) #Come Mr. Tally-man


if __name__ == "__main__":
    main()
