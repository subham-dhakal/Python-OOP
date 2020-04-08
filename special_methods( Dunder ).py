
class Employee:

    raise_amount  = 1.04        # class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1    # Increase the no. of employee every time we make new Employee instance 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   # class variable need be accessed through Class itself or by Instances


    def __repr__(self):  # used to represent object for the developers
        return "Employee('{}','{}', {})".format(self.first,self.last,self.pay)


    def __str__(self):      # used to represent object for the end-user
        return  "{} - {}".format(self.fullname(),self.email)


    def __add__(self, other):               # Adds the total salary of two objects 
        return "The total salary  of {} and {} = {}".format(self.fullname(),other.fullname(),(self.pay + other.pay))


    def __len__(self):   # gives the length of employee's fullname 
        return len(self.fullname())

emp1 = Employee('saurav', 'dhakal', 80000)
emp2 = Employee('subham', 'dhakal', 60000)


# adds salary of two objects
print(emp1 + emp2)                   # Customizing the add functionality 


print(len(emp1))  # prints the length of employee's fullname

# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())
# print(emp1.__str__())



