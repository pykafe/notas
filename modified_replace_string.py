def replace_char(string, index, char):
    # returns modified string with index replaced with char
    pass


replace_char('foo', 0, 'b')  # returns 'boo'
replace_char('foo', 1, 'b')  # returns 'fbo'
replace_char('foo', 2, 'b')  # returns 'fob'
replace_char('mario', 2, 't')  # returns 'matio'

replace_char('ta', 0, 'h')  # returns 'ha'
replace_char('ha', 1, 'o')  # returns 'ho'

def ano(string, index, char):
    value = []
    value_string = ""
    for item in string:
        value.append(item)
    # value = ['f', 'o', 'o']
    value[index] = char
    # value = ['b', 'o', 'o']
    for item in value:
        value_string += item
    # value_string = 'boo'
    print(value_string)


def ony(string, index, char):
    print(string[:index] + char + string[index + 1:])

   	# LANKA-LANKA ATU MODIFKA STRING NO REPLACE INDEX:
   	
	# >>>string = "mario"
	# >>>index = 2
	# >>>char = "t"
	# >>>print(string[:index])
	# ma
	# >>>print(string[:index] + char)
	# mat
	# >>>print(string[index + 1:])
	# io
	# >>>print(string[:index] + char + string[index + 1:])
	# matio