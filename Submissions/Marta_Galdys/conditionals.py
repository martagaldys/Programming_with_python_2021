

my_city_name = 'Bielsko-Biala'
my_city_population = 171000

my_new_city_name = 'Barcelona'
my_new_city_population = 5500000

if my_city_population > 10000000:
    print( 'My city is a Megacity')

elif my_city_population > 1500000:
    print( 'My city is a Large Metropolitan Area')
    if my_new_city_population > my_city_population:
        print('My new city is bigger than te previous one')


elif my_city_population > 500000:
    print('My city is a Metropolitan Area')

elif my_city_population > 50000:
    print('My city is a Small urban area')

else:
    print('My city is smaller than small urban area')










print('End of script')