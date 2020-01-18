# advanced iteration functions in the itertools package

import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1)) #Joe
    print(next(cycle1)) #John
    print(next(cycle1)) #Mike
    print(next(cycle1)) #Joe

    # use count to create a simple counter
    # Starting value here is 100, which default is 0
    # 10 is step value here, which default is 1
    count1 = itertools.count(100, 10)
    print(next(count1)) #100
    print(next(count1)) #110
    print(next(count1)) #120

    # accumulate creates an iterator that accumulates values
    # It will add the result of previous value to the current value
    # By default its addition
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals)
    print(list(acc)) # [10, 30, 60, 110, 150, 190, 220]

    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(list(acc)) # [10, 20, 30, 40, 50, 50, 50]

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x)) # ['A', 'B', 'C', 'D', '1', '2', '3', '4']
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    # Dropwhile will drop the values from the sequence while 
    # the test funtion returns True, and then it will start returning 
    # every value after that
    print(list(itertools.dropwhile(testFunction, vals)))
    # [40, 50, 40, 30]

    #It will return values from the sequence while the predicate 
    # function returns true and then it will stop giving you value
    print(list(itertools.takewhile(testFunction, vals)))
    # [10, 20, 30]
    
    
if __name__ == "__main__":
    main()
    