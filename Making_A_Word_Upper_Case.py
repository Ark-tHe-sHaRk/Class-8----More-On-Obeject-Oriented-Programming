#Create Class
class IOstring():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input('Enter a word/string: ')

    def print_string(self):
        print('The word you have put in lowercase, in uppercase is: ', self.str1.upper())

#Obect Creation
str1 = IOstring()

#Calling the functions
str1.get_string()
str1.print_string()
