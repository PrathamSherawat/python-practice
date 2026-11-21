EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 60

def bake_time_remaining(elapsed_bake_time):
    """give us the time remaining to bake the lasagna"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes( number_of_layers):
    '''give us the time for the total number of layers'''
    return 2*number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """

    return elapsed_bake_time + 2*number_of_layers
    
    
    



#TODO (student): define the 'elapsed_time_in_minutes()' function below.



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
