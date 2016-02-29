########################
# Iteration
########################


def sum_of_integers(maximum):
    ''' return the sum of all the integers up to maximum
    hint: create a total_sum variable value 0, and a counter variable value 1
    WHILE the counter is less than OR EQUAL TO the maximum, add the counter to the total_sum, add 1 to the counter
    after the while loop has exited, return the total_sum
    '''
    total_sum = 0
    counter = 1
    while counter <= maximum:
        total_sum = total_sum + counter
        counter = counter + 1
    return total_sum


def test_sum_of_integers():
    assert sum_of_integers(2) == 3
    assert sum_of_integers(5) == 15


def ten_multiples_of(number):
    ''' return a list containing 10 mutpliples of the input parameter number
    hint: create an empty list, and a counter variable value 1
    WHILE the lenght of the list is less than 10, append counter * number to the list, add 1 to the counter
    after the while loop has exited, return the list
    '''
    lista = []
    x  = 1
    while len(lista) < 10:
        lista.append(x * number)
        x = x + 1
    return lista


def test_ten_multiples_of():
    result_1 = ten_multiples_of(2)
    assert isinstance(result_1, list)
    assert len(result_1) == 10
    assert sum([x % 2 for x in result_1]) == 0

    result_2 = ten_multiples_of(5)
    assert isinstance(result_2, list)
    assert len(result_2) == 10
    assert sum([x % 5 for x in result_2]) == 0


def mulitply_odd_numbers_until(maximum):
    ''' return the value of multiplying together all the odd integers up to maximum
    hint: NO HINTS THIS TIME
    '''
    total_sum = 0
    x = 1
    while x <= maximum:
        total_sum = total_sum + x
        x = x + 1
    return total_sum



def test_mulitply_odd_numbers_until():
    assert mulitply_odd_numbers_until(5) == 1 * 3 * 5
    assert mulitply_odd_numbers_until(9) == 1 * 3 * 5 * 3


def sum_and_product(in_list):
    ''' return 2 values from this function - a tuple
    the first value is the sum of all the values in the list
    the second alue is the product of all the values in the list
    sum_and_product([2, 3]) == (6, 5)
    sum_and_product([2, 4, 6]) == (12, 48)
    '''
    list_product = 1
    for item in in_list:
        list_product = list_product * item
    return sum(in_list), list_product
   




def test_sum_and_product():
    assert sum_and_product([2, 3]) == (5, 6)
    assert sum_and_product([2, 4, 6]) == (12, 48)
