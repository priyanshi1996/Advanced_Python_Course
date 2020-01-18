# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


def main():
    # create a new Person object
    cls1 = Person()

    #Before overriding any  function
    # use different Python functions to convert it to a string
    print(repr(cls1)) # <__main__.Person object at 0x102869f60>
    # Here python is generating some default string that represents class
    # name and its address in memory
    print(str(cls1)) # <__main__.Person object at 0x102869f60>
    print("Formatted: {0}".format(cls1)) # Formatted: <__main__.Person object at 0x102869f60>
    
    #When we override repr function
    print(repr(cls1)) # <Person Class - fname:Joe, lname:Martini, age:25
    print(str(cls1))  # <Person Class - fname:Joe, lname:Martini, age:25
    print("Formatted: {0}".format(cls1)) #Formatted <Person Class - fname:Joe, lname:Martini, age:25
    

    #When we override repr function and str function
    print(repr(cls1)) # <Person Class - fname:Joe, lname:Martini, age:25
    print(str(cls1))  # Person  (Joe Martini is 25)
    print("Formatted: {0}".format(cls1)) #Formatted Person  (Joe Martini is 25)
    print(bytes(cls1)) # b'Person:Joe:Martini:25'

if __name__ == "__main__":
    main()
