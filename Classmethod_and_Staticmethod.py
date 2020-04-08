
# Regular methods in a class automatically takes instances as their first arguments
# Class methods automatically takes class as their first arguments
# Static mathods doesnot take any arguments . IT does not operate on class or the instances


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternate  Constructor
    @classmethod
    def get_from_string(cls, emp_string):                 # Using class method as 'alternate constructor' 
        first , last, pay = emp_string.split('-')
        return cls(first, last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# print(Employee.raise_amount)
# Employee.set_raise_amt(1.08)
# print(Employee.raise_amount)


#  Demo for class method
employee_str_1 = 'Jubin-kc-70000'
new_employee =  Employee.get_from_string(employee_str_1)
print(new_employee.email)


# Demo for static method
import datetime
my_date = datetime.date(2020, 4, 2)

print(Employee.is_workday(my_date))











