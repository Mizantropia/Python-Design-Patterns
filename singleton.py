class Person:
    __instance = None

    def __new__(cls, name, age, nationality):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.name = name
        cls.__instance.age = age
        cls.__instance.nationality = nationality
        return cls.__instance

    def __call__(cls, *args, **kwargs):
        print(f"The current person is {cls.__instance.name}")

person = Person('Oliwia', 20, "PL")
person()

person2 = Person('Sebastian', 21, 'PL')
person2()

person()