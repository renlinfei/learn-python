# class Player():
#     def __init__(self, name, hp, occu):
#         self.__name = name
#         self.hp = hp
#         self.occu = occu
#     def print_role(self):
#         print('%s: %s %s' %(self.__name, self.hp, self.occu))
#     def change_name(self, new_name):
#         self.__name = new_name
#
# player1 = Player('tom', 100, 'warrior')
# player2 = Player('jerry', '80', 'master')
#
# player1.print_role()
# # player1.change_name('chris')
# player1.name = 'qaqa'
# player1.print_role()


# player2.print_role()

class Monster():
    def __init__(self, hp=100):
        self.hp = hp
    def run(self):
        print('移动位置')
class Animal(Monster):
    '定义怪物'
    def __init__(self, name, hp):
        super().__init__(hp)
        self.name = name
class Boss(Monster):
    '定义Boss'
    pass

a1 = Monster(34)
print(a1.hp)
a1.run()

a2 = Animal('tomcat',30)
print(a2.hp)
a2.run()

print(type(a1))
print(type(a2))
print(isinstance(a1, Monster))