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
        return "<Person Class - fname:{0},mname:{1} lname:{2}, age:{3}, message:{4}".format(self.fname,self.mname,self.lname,self.age,self.unique)

    # TODO: use str for a more human-readable string
    
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname,self.mname,self.lname,self.age,self.unique)
        return bytes(val.encode('utf8'))

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))

    print(bytes(cls1))

if __name__ == "__main__":
    main()
