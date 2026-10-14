# data_types = ['ivanov',23,True,33.44,False,33,'Ivan']
# #add
# data_types.append('Ermek')
# #add2
# data_types.insert(0,'iphone')
# #delete
# data_types.remove(23)
# del data_types[0]
# print(data_types)

#Расширение списка другим списком
# data_type_1 = [1,2,3,4,5,6,7]
# data_type_2 = ['J.Sean','Florida','50 Cent','Kesha']

# data_type_2.append(data_type_1.pop(4))

# data_type_1.extend(data_type_2)
# print(data_type_1)

#КОРТЕЖ

# names = ('Naruto','Saske','Sakura')
# names = list(names)
# names.append('Hinata')
# names = tuple(names)

# print(names)

#Словари

student = {
    'name': 'Ivanov Ivan',
    'age': 24,
    True: 'education',
    False: 123,
}

student['city'] = 'Osh'

print(student['city'])
