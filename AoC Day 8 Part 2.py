with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def count_occurencies(entry, letter):

    occurencies = 0

    for value in entry:
        if letter in value:
            occurencies += 1

    return occurencies

def decode(entry):

    # decode each entry's individual segment/signal config
    # and then use this to work out which combination of signals
    # represents each number

    numbers = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c','f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a' , 'b', 'd', 'e', 'f' , 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    signal_numbers = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    segment = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': '',
    }

    # identify the numbers we can based on length
    signal_numbers[1] = list([value for value in entry[0] if len(value) == 2][0])
    signal_numbers[4] = list([value for value in entry[0] if len(value) == 4][0])
    signal_numbers[7] = list([value for value in entry[0] if len(value) == 3][0])
    signal_numbers[8] = list([value for value in entry[0] if len(value) == 7][0])

    # once we know 1 & 7, we know segment a 
    segment['a'] = [value for value in signal_numbers[7] if value not in signal_numbers[1]][0]
    # identify the rest based on the number of times they appear in the 10 numbers in the entry
    segment['c'] = [value for value in signal_numbers[1] if count_occurencies(entry[0], value) == 8][0]
    segment['f'] = [value for value in signal_numbers[1] if count_occurencies(entry[0], value) == 9][0]
    segment['b'] = [value for value in signal_numbers[4] if count_occurencies(entry[0], value) == 6][0]
    segment['d'] = [value for value in signal_numbers[4] if count_occurencies(entry[0], value) == 7][0]
    segment['e'] = [value for value in signal_numbers[8] if count_occurencies(entry[0], value) == 4][0]
    segment['g'] = [value for value in signal_numbers[8] if count_occurencies(entry[0], value) == 7 and value not in signal_numbers[4]][0]

    for number in signal_numbers:
        if len(signal_numbers[number]) != 0:
            continue
        
        # build up the equivalent numbers based on each individual entry's segment/signal config
        for letter in numbers[number]:
            signal_numbers[number].append(segment[letter])

    return signal_numbers


# script
input_split = [value.split(' | ') for value in input]

input_cleaned = []

for value in input_split:
    input_cleaned.append([value[0].split(' '), value[1].split(' ')])

sum_output_value = 0

for entry in input_cleaned:
    signal_numbers = decode(entry)
    
    # match up second part of entries against signal numbers
    entry_number = ''
    for entry in entry[1]:
        for number in signal_numbers:
            if ''.join(sorted(entry)) == ''.join(sorted(signal_numbers[number])):
                entry_number = entry_number + str(number)

    sum_output_value += int(entry_number)
    
print(sum_output_value)
    
     