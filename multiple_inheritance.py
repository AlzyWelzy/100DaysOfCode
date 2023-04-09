class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} does stuff")

    def __repr__(self):
        return f"{self.name}"


class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

    def work(self):
        print(f"{self.name} makes food")


class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

    def work(self):
        print(f"{self.name} interfaces with customer")


class PizzaRobot(Chef, Server):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(f"{self.name} makes pizza")
