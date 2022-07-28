# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # # TODO: Create a Counter for class1 and class2
    c1= Counter(class1)
    c2=Counter(class2)
    print(c1,c2)

    # # TODO: How many students in class 1 named James?
    # print(c1["James"])

    # # TODO: How many students are in class 1?
    # print(sum(c1.values()))

    # # TODO: Combine the two classes
    # c1.update(class2)
    # print(c1)

    # # TODO: What's the most common name in the two classes?
    # c1_common= c1.most_common(3)

    # print(c1_common)
    # # TODO: Separate the classes again
    # c1.subtract(class2)
    # print("c1",c1,(sum(c1.values())))
    # print("c2",(sum(c2.values())))

    # TODO: What's common between the two classes?
    commons=[]
    for student in c1.keys():
        if student in c2.keys():
            commons.append(student)
            
    print(c1 & c2)        
        
    print(commons)     


if __name__ == "__main__":
    main()
