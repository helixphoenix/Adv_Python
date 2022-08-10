# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    
    deck = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    
    print("Item Count: ", str(len(deck)))

    # TODO: deques can be iterated over
    for letter in deck :
        print(letter.upper(), end=",")

    # TODO: manipulate items from either end
    deck.pop()
    deck.popleft()
    deck.append(2)
    deck.appendleft(1)
    print("popped",deck)
    # TODO: rotate the deque
    print(deck)
    deck.rotate(1) 
    print(deck)

if __name__ == "__main__":
    main()
