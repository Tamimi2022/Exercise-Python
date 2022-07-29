# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(Weather, Time_of_day, Cow_milking_status, Location_of_cows, Season, Slurry_tank, Grass_status):
    if Time_of_day == 'night' and Location_of_cows == 'pasture':
        return 'take cows to cowshed'
    
    elif Weather == 'rainy' and Location_of_cows == 'pasture':
        return 'take cows to cowshed'
    
    elif Cow_milking_status == True and Location_of_cows == 'pasture':
        return '''take cows to cowshed
milk cows
take cows back to pasture'''
    
    elif Cow_milking_status == True and Location_of_cows == 'cowshed':
        return 'milk cows'
    
    elif Weather == 'neutral' or Weather == 'rainy' and Location_of_cows == 'cowshed' and Slurry_tank == True:
        return 'fertilize pasture'
    
    elif Weather == 'neutral' or Weather == 'rainy' and Location_of_cows == 'pasture' and Slurry_tank == True:
        return '''take cows to cowshed
fertilize pasture
take cows back to pasture'''
    
    elif Season == 'spring' and Weather == 'sunny' and Grass_status == True and Location_of_cows == 'cowshed':
        return 'mow grass'
    
    elif Season == 'spring' and Weather == 'sunny' and Grass_status == True and Location_of_cows == 'pasture':
        return '''take cows to cowshed
mow grass
take cows back to pasture'''
    
    else:
        return 'wait'