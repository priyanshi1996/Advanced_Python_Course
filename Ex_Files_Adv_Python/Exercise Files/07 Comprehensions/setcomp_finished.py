# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a set of unique Fahrenheit temperatures
    ftemps1 = [(t * 9/5) + 32 for t in ctemps] # list
    ftemps2 = {(t * 9/5) + 32 for t in ctemps} # set
    #Curly brace is representing set because its not key: value pair
    print(ftemps1)
    print(ftemps2)

    # build a set from an input source
    sTemp = "Hello Priya"
    chars = {c.upper() for c in sTemp}
    print(chars) # {'H', 'E', 'L', 'O', 'P', 'R', 'I', 'Y', 'A', ' '}
    # here it is printing space also


    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars) #{'H', 'E', 'L', 'O', 'P', 'R', 'I', 'Y', 'A'}


if __name__ == "__main__":
    main()
