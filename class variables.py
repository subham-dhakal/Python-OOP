'''
 Class variables are common and shared with the class as well as the methods.
 Instance variable are unique and differs for each instances

'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp1 = Employee('saurav', 'dhakal', 80000)

print(emp1.email)
