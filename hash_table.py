array = [[], [], [], [], []] # has 5 empty "buckets"

def hash_function(string):
    string_weight = sum([ord(char)-97 for char in string])
    return string_weight % 5

def insert(array, key, value):
    index = hash_function(key)
    array[index].append((key,value))

def find(array, key):
    index = hash_function(key)
    for data in array[index]:
        if data[0] == key:
            return data[1]


alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value