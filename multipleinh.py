#multiple inheritance
# Parent class 1
class Person:
 def person_info(self, name, age):
    print('Inside Person class')
    print('Name:', name, 'Age:', age)
# Parent class 2
class Company:
 def company_info(self, company_name, location):
    print('Inside Company class')
    print('Name:', company_name, 'location:', location)

# Parent class 3
class House:
 def house_info(self, house_name, location):
    print('Inside House class')
    print('Name:', house_name, 'location:', location)
# Child class
class Employee(Person, Company,House):
 def Employee_info(self, salary, skill):
    print('Inside Employee class')
    print('Salary:', salary, 'Skill:', skill)
# Create object of Employee
emp = Employee()
# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.house_info('Microsoft', 'Africa')
emp.Employee_info(12000, 'Machine Learning')