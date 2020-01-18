# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d))) # 26

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop() # Pops data from right
    d.popleft() # pops data from left
    d.append(2) # append data to the right
    d.appendleft(1) # appned data to the left
    print(d)

    # rotate the deque
    print(d)
    d.rotate(1) # By default its value is 1, +ve value means rotate to the 
                # right and -ve value means rotate to the left
    print(d)


if __name__ == "__main__":
    main()
