# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Dudu"
        self.mname = "Hazal"
        self.lname = "OK"
        self.age = 32
        self.unique = "everyone has similarities and differences, stop labeling and classifying people"

    # TODO: use __repr__ to create a string useful for debugging
    
    def __repr__(self):
        return "<Person Class - fname:{0},mname:{1} lname:{2}, age:{3}".format(self.fname,self.mname,self.lname,self.age)

    # TODO: use str for a more human-readable string


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))


if __name__ == "__main__":
    main()
