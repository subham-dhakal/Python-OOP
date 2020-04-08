# Getter , Setter , Deleter  property

class Employee:

    raise_amount  = 1.04        # class variable
    num_of_emps = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

        Employee.num_of_emps += 1    # Increase the no. of employee every time we make new Employee instance 


    @property
    def email(self):        # Now we can use email function as an variable and access ( eg. emp_1.email)
       return "{}.{}@gmail.com".format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Delete Name !")
        self.first = None
        self.last = None

emp_1 = Employee('will', 'dhakal')

emp_1.first = 'subham'

emp_1.fullname = 'rame raksman'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


