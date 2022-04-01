class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname 
        self.lastname = lastname 
        self.salary = salary


    @classmethod
    def from_string(class_obj, string):
        firstname, lastname, salary = list(map(str, string.split('-')))
        return class_obj(firstname, lastname, int(salary))

