"dict and sets"
# dict
my_dict = {'Кирилл' : 2006 , 'Ivan' : 2003, 'Ann' : 2016}
print('Dict: ' , my_dict)
print('Existing value Var1: ' , my_dict['Кирилл'])
print('Existing value Var2: ' , my_dict.get('Ivan'))
print('Not existing value: ' , my_dict.get('Alex' , 'Такого имени во множестве нет'))
my_dict.update({'Nikolay' : 1954 , 'Nina' : 1948})
print(my_dict)
a = my_dict.pop('Nina')
print('Deleted value: ' , a)
print('Modified dictionary:' , my_dict)




# sets var 1
my_set = {1, 1, 3, 5,  4, 4, 2}
print('set' , my_set)
print(my_set.add(7))                 # непонятно, почему в консоль выводится "None"? Но так было и в лекции
print(my_set)                        # а здесь вроде Good
my_set.add(8)                        # Без print() все гораздо лучше получается
print('Addendum: ' , my_set)         # и здесь Good
my_set.discard(3)
print('Modified dictionary: ' , my_set)




# sets var 2
my_set = {1, 1, 3, 5,  4, 4, 2}
print('set' , my_set)
my_list = list(my_set)
my_list = my_list + [7, 8]
my_set = set(my_list)
print('Addendum: ' , my_set)
my_set.discard(3)
print('Modified dictionary: ' , my_set)