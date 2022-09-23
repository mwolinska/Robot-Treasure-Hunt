from random import randint

class Robot:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.robot_id = randint(0, 1000)

    @classmethod
    def create_from_user_input(cls):
        robot_name = cls.get_name_from_input()
        robot_age = cls.get_age_from_input()
        return cls(robot_name, robot_age)

    @staticmethod
    def get_name_from_input():
        print("What is your robot's name?")
        new_name = input()
        return new_name

    @staticmethod
    def get_age_from_input():
        print("What is your robot's age?")
        new_age = int(input())
        return new_age

    # def observe(self, world: World):
    #     self.observations = world.get_observations(self.position)

    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age}. My ID is {self.robot_id}")
