from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Input integers
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Basic arithmetic operations
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2
    quotient_result = my_int1 / my_int2

    # Conditional logic
    max_result = (my_int1 < my_int2).if_else(my_int2, my_int1)

    # Custom operations using @nada_fn decorator
    @nada_fn
    def custom_operation(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a + b) * (a - b)

    custom_result = custom_operation(my_int1, my_int2)

    # Functions using @nada_fn decorator
    @nada_fn
    def square(a: SecretInteger) -> SecretInteger:
        return a * a

    @nada_fn
    def min_value(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a < b).if_else(a, b)

    # Advanced operations
    square_result1 = square(my_int1)
    square_result2 = square(my_int2)
    min_result = min_value(my_int1, my_int2)

    # Output results to different parties
    return [
        Output(sum_result, "sum_output", party2),
        Output(product_result, "product_output", party2),
        Output(difference_result, "difference_output", party2),
        Output(quotient_result, "quotient_output", party2),
        Output(max_result, "max_output", party3),
        Output(custom_result, "custom_output", party3),
        Output(square_result1, "square_output1", party3),
        Output(square_result2, "square_output2", party3),
        Output(min_result, "min_output", party3)
    ]