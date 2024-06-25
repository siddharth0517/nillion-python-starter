from nada_dsl import *


def nada_main():
    # Define the party
    party1 = Party(name="Party1")
    
    # Define secret integer inputs for the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Perform various computations
    addition = my_int1 + my_int2
    subtraction = my_int1 - my_int2
    multiplication = my_int1 * my_int2
    division = my_int1 / my_int2
    
    # Return the results as outputs
    return [
        Output(addition, "addition_result", party1),
        Output(subtraction, "subtraction_result", party1),
        Output(multiplication, "multiplication_result", party1),
        Output(division, "division_result", party1)
    ]
