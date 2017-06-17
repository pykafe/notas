# Types and casting

1 is an Integer
1.0 is a Float
'1' is a String

1 + 1 == 2
1 + 1.0 == 2.0
1 + '1' == 2 # Error!!!
1 + int('1') == 2  # _cast_ numbered strings as integers
1 + float('1') == 2.0  # _cast_ numbered strings as floats