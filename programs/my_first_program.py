from nada_dsl import *

def gcd(a, b):
    zero = SecretInteger(0)
    
    while not (b == zero):
        temp = b
        b = a % b
        a = temp
        
    return a

def nada_main():
    party1 = Party(name="Party1")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the GCD of the two input integers
    gcd_result = gcd(my_int1, my_int2)

    # Return the GCD as an output
    return [Output(gcd_result, "gcd_output", party1)]
