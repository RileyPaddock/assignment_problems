flips = {
    'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
    'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
    'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
    'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
    'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
}

def count(dataset,next,prev):
    num_both = 0
    num_prev = 0
    for outcomes in dataset:
        pairs = [str(outcomes[i])+str(outcomes[i+1]) for i in range(len(outcomes)-1)]
        for pair in pairs:
            if pair[0] == prev:
                num_prev += 1
                if pair[1] == next:
                    num_both += 1
    return num_both/num_prev

def get_strings(next,prev):
    if next == 'H':
        next_str = 'heads'
    else:
        next_str = 'tails'
    if prev == 'H':
        prev_str = 'heads'
    else:
        prev_str = 'tails'
    return [next_str, prev_str]

for person in flips:
    print("\nTesting "+str(person)+":")
    data = flips[person].split(' ')
    possibilities = ['HH','TH','HT','TT']
    for test in possibilities:
        strings = get_strings(test[0],test[1])
        print("\n   P( next flip was "+str(strings[0])+" | previous flip was "+str(strings[1])+" ):")
        print("\n       "+str(count(data,test[0],test[1])))

print("\nSimple Testing:")
dataset = ['HHTTHT']
possibilities = ['HH','TH','HT','TT']
for test in possibilities:
    strings = get_strings(test[0],test[1])
    print("\n   P( next flip was "+str(strings[0])+" | previous flip was "+str(strings[1])+" ):")
    print("\n       "+str(count(dataset,test[0],test[1])))
