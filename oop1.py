# initiate a class
class employees:
    # special method/magic method/dunder method = constractor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 1000000 
        self.designation = "Data Scientist"
        print("attributes/data have been initiated")

    def travel(self,destination):
        print("started called function")
        print(f'Employee is now travelling to {destination}')

# create an object/instance of class

sam = employees()

""" print(sam.id)
print(sam.salary)
print(sam.designation)

# calling method"""
""" sam.travel('chandrapur')  """

print(type(sam))