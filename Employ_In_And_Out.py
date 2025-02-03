#Create Class
class Employee:

    #Initialise the class
    def __init__(self):
        print('Employee Class Created')

    #Calling Destructor
    def __del__(self):
        print('Destructor Called, Employee Class Deleted')

def Create_obj():
    print('Creating Object...')
    obj = Employee()
    print('Function Ends...')
    return obj

print('Calling Create_obj() Function...')
obj = Create_obj()
print('Program Ends...')

#Output:
# Calling Create_obj() Function...
# Creating Object...
# Employee Class Created
# Function Ends...
# Program Ends...
# Destructor Called, Employee Class Deleted
