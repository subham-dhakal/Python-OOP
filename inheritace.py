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



class Developer(Employee):          # inheritance
    raise_amount = 1.10

    def __init__(self, first, last ,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang  = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        self.employees = employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('----> ', emp.fullname())

    


dev_1 = Developer('saurav', 'dhakal', 80000, 'php')
dev_2 = Developer('subham', 'dhakal', 60000, 'python')


mgr_1  = Manager('Ram','Chandra',90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
mgr_1.print_emp()


print(issubclass(Manager,Employee))



