class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'hello, my name is {self.name} y tengo {self.age} años ')


if __name__ == '__main__':
    person = Person('Frank', 23)

    person.say_hello()
