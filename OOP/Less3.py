class Person:
    
    def __init__(self, name, last_name, rank = 1):
        self.name = name
        self.last_name = last_name
        self.rank = rank


    def person_info(self):
        return f'Name: {self.name}, Lastname: {self.last_name}, Rank: {self.rank}'


    def __del__(self):
        print(f'Goodbye, mister {self.name} {self.last_name}')


p1 = Person('Ilya', 'Nilov', 3)
p2 = Person('Alex', 'Sidorov', 3)
p3 = Person('unknown', 'user')


print(p1.person_info())
print(p2.person_info())
print(p3.person_info())

del(p3)

input()
