# constructor : __init__()

class UserData():
    age = 0
    name = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User name is : {self.name} and has {self.age} years old str"

    def user(self):
        print(f"User name is : {self.name} and has {self.age} years old")


user_1 = UserData("bhavya", 25)
print(type(user_1))
user_1.user()
print(user_1)


class PhoneNum(UserData):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num


user_2 = PhoneNum("ridham", 20, 87836753342)
print(user_2)
