# Demonstrate the usage of defaultdict objects

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    fruitCount = {}
    # Count the elements in the list
    # This code will give error because we are trying to modify the value
    # of this key, before its been initialy added to the dictionary
    for fruit in fruits:
        fruitCount[fruit] += 1
    
    # To avoid the above error we could write something like this
    for fruit in fruits:
        if fruit in fruitCount.keys():
            fruitCount[fruit] += 1
        else:
            fruitCount[fruit] = 1

    # use a dictionary to count each element
    # this code says that if I am trying to access a key which 
    # does not exists, create a default value for me
    fruitCounter = defaultdict(int)
    # We can also use lambda here, here each key will start from 100
    # fruitCounter = defaultdict(lambda:100)

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
