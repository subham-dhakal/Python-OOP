'''
 Class variables are common and shared with the class as well as the methods.
 Instance variable are unique and differs for each instances

'''

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

emp1 = Employee('saurav', 'dhakal', 80000)
emp2 = Employee('subham', 'dhakal', 60000)




# print(emp1.pay)
# print(emp1.__dict__)

emp1.apply_raise()
print(emp1.pay)

# print(emp1.__dict__)
# print(emp1.raise_amount)

print(Employee.num_of_emps)






