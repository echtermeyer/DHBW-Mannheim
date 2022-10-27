class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def summary(self):
        print(f"{self.name} hat am {self.birthday} Geburtstag")


class Customer(Person):
    def __init__(self, name, birthday, customer_id):
        super().__init__(name, birthday)

        self.customer_id = customer_id

    def summary(self):
        print(f"{self.name} mit der ID {self.customer_id}")


class Employee(Person):
    def __init__(self, name, birthday, username):
        super().__init__(name, birthday)

        self.username = username


address_book = [Employee()]