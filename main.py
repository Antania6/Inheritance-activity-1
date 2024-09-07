class person:
    def __init__(self,name,idNumber):
        self.name=name
        self.idNumber=idNumber

    def display(self):
        print(self.name)
        print(self.idNumber)


class employee(person):
    def __init__(self,name,idNumber,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,idNumber)

    def show(self):
        print(self.salary)
        print(self.post)
        person.display(self)


obj1 = employee("Tom",23987,50000,"HR")
obj1.show()

