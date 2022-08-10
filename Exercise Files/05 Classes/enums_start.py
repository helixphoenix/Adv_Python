# define enumerations using the Enum base class

from enum import Enum, auto, unique

def main():
    pass
    # TODO: enums have human-readable values and types
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3 
    TOMATO = 4 
    PEAR = auto()
    
def main():
            

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(type(Fruit.APPLE))
    # TODO: print the auto-generated value
    print(Fruit.APPLE.PEAR.value)

    # TODO: enums are hashable - can be used as keys
    listFruits = {}
    listFruits[Fruit.BANANA] ="wut"
    print(listFruits)

if __name__ == "__main__":
    main()
