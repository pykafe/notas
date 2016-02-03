Lists
=====
Strutura dadus ida nebe rai koleksaun tipo dadus oin-oin ho sequensia nebe uza squre '[ ]' hanesan taka no loke maka ita bolu ***Lista***. Bainhira ita kria ona lista ita bele halo mudansa hanesa ita aumenta, hamenus no buka item sira. Tamba ita bele aumenta no hamenus item sira iha lista maka ita bolu lista hanesan **mutable**. Hosi koleksaun dadus nebe iha lista kada dadus iha nia numeru index nebe ***hahu ho 0.***


Tuir mai exemplo oinsa atu kria lista.

**alista = [*x*]**

iha nebee:

**alista** =  variabel ida nebe fo sai hanesan lista

**x** = parameter ida nebe sai hanesan objeto(string, int etc).

    >>> lista_a = ['ida', 'rua', 'tolu', 4, 5]  
    >>> lista_a[0]
    'ida'
    >>> lista_a[1]
    'rua'
    >>> lista_a[4]
    5

Tamba ita bolu lista hanesan mutable. Lista Iha metode no funsaun sira nebe ita uza maka henesan tuir mai:

*Metode sira*:

lista.append(*x*)
*exemplo*:

    >>> a = [1, 2, 3, 5]
    >>> a
    [1, 2, 3, 5]
    >>> a.append(6)
    >>> a
    [1, 2, 3, 5, 6]

lista.extend(*L*)

*exemplo*:

    >>> a = [1, 2, 3, 5]
    >>> b = [5, 7]


lista.insert(*i, x*)

**i **= parameter ba index

**x** = parameter ba objecto

*exemplo*:

    >>> a = [1, 2, 3, 5]
    >>> a.insert(3, 4)
    >>> a
    [1, 2, 3, 4, 5]


lista.remove(*x*)

*exemplo*:

    >>> a = [1, 2, 3, 5]
    >>> a.remove(5)
    >>> a
    [1, 2, 3, 4]

lista.pop()

Uza 'pop' hodi hamos objecto/elemento ida nebe iha ikus liu.

*exemplo*:

    >>> a = [1, 2, 3, 5, "six"]
    >>> a.pop()
    >>> a
    [1, 2, 3, 4]

lista.index(*x*)

*exemplo*:

    >>> a = [1, 2, 3, 4]
    >>> a.index(1)
    0
    >>> a.index(2)
    1

lista.count(*x*)

*exemplo*:

    >>> a = [1, 2, 5, 3, 4,  5, "six"]
    >>> a.count("six")
    1
    >>> a.count(5)
    2

lista.sort()

*exemplo*:

    >>> a = [2, 1, 4, 5, 3,  5, "six"]
    >>> a.sort()
    [1, 2, 3, 4,  5, 5, "six"]  

lista.reverse()

*exemplo*:

    >>> a = [1, 2, 3, 4,  5, 5, "six"]
    >>> a.reverse()
    [2, 1, 4, 5, 3,  5, "six"]

**Funsaun sira **

len(lista)

*exemplo*:

    >>> a = [1, 2, 3, 4,  5,]
    >>> len(a)
    5

max(lista)

*exemplo*:

    >>> a = [1, 2, 3, 4,  7, 5]
    >>> max(a)
    7

min(lista)

*exemplo*:

    >>> a = [1, 2, 3, 4,  7, 5]
    >>> min(a)
    1

list(a_tuple)

*exemplo*:

    >>> aTuple = (1, 2, 3, 4,  7, 5)
    >>> list(aTuple)
    [1, 2, 3, 4,  7, 5]


#How do you change value at index?

#Joining elements in a list



#Adding elements in a list

    def add_to_list(my_value, my_list):
        return my_list + [my_value]

#Get Item from a List

    def get_index_from_list(my_index, my_list):
        if isinstance(my_index, int):

#Check list for value

    def is_in_list(my_value, my_list):
        return my_value in my_list

#Get a lists length

    def get_length(my_list):
        get_length = len(my_list)
        return get_length

#Concatenate (merge) two lists

    def merge_lists(first_list, second_list):
        merge_lists = first_list + second_list
        return merge_lists

#Converting a list to string

    def list_to_string(my_list):
        return ' '.join(my_list)

#Converting a string to list

    def string_to_list(my_string):
        if isinstance(my_string, str):
            return list(my_string)

#Count the frequency of elements in a list

from collections import Counter

    def count_occurrences(my_list):
        return Counter(my_list)
