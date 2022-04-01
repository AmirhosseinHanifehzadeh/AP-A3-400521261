class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, char):
        if self.age > char.age:
            print("{} is younger than me.".format(char.name))
        elif self.age < char.age:
            print("{} is older than me.".format(char.name))
        else:
            print("{} is the same age as me.".format(char.name))

