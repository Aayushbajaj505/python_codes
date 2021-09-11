class Animal():
    def __init__(self, breed, owner):
        print('CLASS ANIMAL CREATED')
        self.breed = breed
        self.owner = owner

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am Eating')


class Dog(Animal):

    def __init__(self, nickname):
        self.nickname = nickname

    # def initialize(self, nickname):
    #     self.nickname = nickname

    def who_am_i(self):
        print('I am a dog!')
        print(self.breed)
        print(self.owner)
        print(self.nickname)
        


my_dog = Dog('golden retriever', 'ayush')
# my_dog.initialize('badmaash')
my_dog.who_am_i()
