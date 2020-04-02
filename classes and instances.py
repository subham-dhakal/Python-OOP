class Employee:

    def __init__(self, first, last, pay):     # constructor or initalizer
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {} '.format(self.first, self.last)


emp1 = Employee('Subham', 'dhakal', 50000)
emp2= Employee('Ram', 'bahadur', 30000)

print(emp1.fullname())
print(Employee.fullname(emp2))
