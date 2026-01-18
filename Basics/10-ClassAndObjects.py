class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(f'Employee id is {self.id}')
        print(f'Employee name is {self.name}')
    
emp = Employee(1, 'coder')
emp1 = Employee(2, 'tester')

emp.printDetails()
emp1.printDetails()

#Use del property to first delete id attribute and then the entire object
del emp.id

try:
    print(emp.id)
except AttributeError:
    print('Emp.id is not present')

del emp

try:
    emp.printDetails()
except NameError:
    print('emp object is not present')