# demonstrate template string functions
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    
    temp= Template("Wut ${title} by ${author}")
    
    # TODO: use the substitute method with keyword arguments
    strink= temp.substitute(title='happy',author='fitifiti')
   
    
    # TODO: use the substitute method with a dictionary

    specs={'author':'Dudu Hazal OK', 'title':'dreams'}
    
    dreams=temp.substitute(specs)
    print(dreams)
    
if __name__ == "__main__":
    main()
    