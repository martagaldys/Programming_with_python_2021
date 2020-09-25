
#  working with lists []

names = ['Barcelona', 'Vienna', 'Bielsko-Biala', 'Cracow', 'Munich', 'Innsbruck', 'Bregenz', 'Salzburg', 'Warsaw', 'Gliwice' ]

number_of_cities = len(names)

if number_of_cities >= 10:
    print(names)
else:
    print('there are less than 10 cities')

print('\n')

if number_of_cities >= 10:
    for i in range(number_of_cities):
        print(names[i])
else:
    print('there are less than 10 cities')

print('\n')

for i in names:
    print(i)

print('\n')
print('\n')

names = ['Barcelona', 'Vienna', 'Bielsko-Biala', 'Cracow', 'Munich', 'Innsbruck', 'Bregenz', 'Salzburg', 'Warsaw', 'Gliwice' ]

population = ['5500000', '1000000', '170000', '1000000', '2000000', '200000', '100000', '170700', '200000', '150000']

cities = [names, population]
print(cities[0][0],'Has a population of', cities [1][0])

print('\n')

for i in range (number_of_cities):
    print(cities[0][i],'Has a population of', cities [1][i])


# working with dictionaries {}
# names = ['Barcelona', 'Vienna', 'Bielsko-Biala', 'Cracow', 'Munich', 'Innsbruck', 'Bregenz', 'Salzburg', 'Warsaw', 'Gliwice' ]
# population = ['5500000', '1000000', '170000', '1000000', '2000000', '200000', '100000', '170700', '200000', '150000']

city_dictionary = {'Barcelona': 5500000, 'Vienna': 1000000, 'Bielsko-Biala', 'Cracow',
                  'Munich', 'Innsbruck', 'Bregenz', 'Salzburg', 'Warsaw', 'Gliwice' }

# creating dictionary from our previous list

for i in range (number_of_cities):
    dict_cities 