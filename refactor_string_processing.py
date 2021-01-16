string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
divided_string = [x.split(',') for x in string.split('\n')]

correct_division = []

for string_set in divided_string:

    fixed_string = []
    
    for string in string_set:

        if len(string) > 2 and "." not in string:
            string = string[1:-1]
        elif '.' in string:
            string = float(string)
        else:
            string = int(string)

        fixed_string.append(string)

    correct_division.append(fixed_string)
    
print(correct_division)