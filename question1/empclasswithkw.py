class Employee:
    def __init__(self, fullName, **kwargs):
        self.name = fullName.split()[0] 
        self.lastname = fullName.split()[1]
        for key in kwargs:
            setattr(self, key, kwargs[key])
