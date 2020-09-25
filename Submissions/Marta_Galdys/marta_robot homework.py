

# decision 1 _ based on distance to an object

current_distance_to_obejct = 10
desire_distance_to_an_object = 3

if current_distance_to_obejct > 10:
    print('move faster')
    print('move 3 forward')

elif (current_distance_to_obejct > 5 ) :
    print('move at the same speed')
    print('move 3 forward')

elif (current_distance_to_obejct > desire_distance_to_an_object) & (current_distance_to_obejct < 5) :
    print('reduce the speed')
    if current_distance_to_obejct < 3:
        move = ((current_distance_to_obejct - desire_distance_to_an_object) /2)
        print('move' + move)
else:
    print('stop')


