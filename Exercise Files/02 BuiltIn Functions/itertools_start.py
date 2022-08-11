# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    pass


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cyclek= itertools.cycle(seq1)
    print(next(cyclek))
    print(next(cyclek))
    print(next(cyclek))
    print(next(cyclek))
    print(next(cyclek))


    # TODO: use count to create a simple counter
    
    counter=itertools.count(10,0.5)
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    
    accs= itertools.accumulate(vals)
    print(list(accs))
            
    # TODO: use chain to connect sequences together
    
    l= itertools.chain('fitjhhis','12314')
    print(list(l))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    
    
if __name__ == "__main__":
    main()
    