# use iterator functions like enumerate, zip, iter, next
import itertools 
def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    a= iter(days)

    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    


    

    # TODO: iterate using a function and a sentinel
    with open("testfile.txt") as f:
        for line in iter(f.readline,''):
         print(line)
          
          
    # TODO: use regular iteration over the days
    
    for day in range(1,len(days)):
        print(day,days[day])

    # TODO: using enumerate reduces code and provides a counter
    
    for i,k in enumerate(days, start=1):
        print(i,k)

    # TODO: use zip to combine sequences
    for i in zip(days, daysFr):
        print(i)


if __name__ == "__main__":
    main()
