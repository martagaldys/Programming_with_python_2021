
##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Marta Galdys
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: marta.maria.galdys@students.iaac.net
# Status: development
##################################################

# End of header section


city_name = 'Bielsko-Biala'
country = 'Poland'
city_area = 125
city_population = 171000
city_density = city_population/city_area

print ('My city name is '+ city_name)
print (city_name + ' is located in  ' + country)

print ('The area of the city is: ' + str(city_area) + 'km²')
print ('The number of inhabitants is: ' + str(city_population))
print ('\n')

print('Population Density:' + str(city_density) + ' inhabitants per km²' )


print ('\n')
mayor_of_city ='Jaroslaw Klimaszewski'
print ('The mayor of the city Bielsko-Biala is: ' + mayor_of_city)

print ('\n')
highest_elevation = 1117
lowest_elevation = 262
elevation_difference= highest_elevation - lowest_elevation

print('The highest elevation is: ' +str(highest_elevation) )
print('The lowest elevation is: ' +str(lowest_elevation) )
print('Elevation difference:')
print( str(elevation_difference) + 'm')
