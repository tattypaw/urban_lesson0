my_dict = {'Ivan': 1999, 'Peter':2001, 'Simon': 1995}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ivan'])
print('Not existing value:', my_dict.get('Jon', 'Такого имени нет'))
my_dict.update({'Mary': 1998,
                'Clark': 1990})
print('Deleted value:',my_dict.pop('Mary'))
print('Modified dictionary:', my_dict)
print()

my_set = {1, 'Mary', 2, 'Boris', (0,1),2,3}
print('Set:', my_set)
my_set.add(5.6)
my_set.add('Ivan')
my_set.discard(2)
print('Modified set:', my_set)