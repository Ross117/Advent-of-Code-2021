with open('C:/Users/rmorran001/Documents/Python Scripts/Advent of Code/2021/Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def get_number_to_keep(method):

    numbers_to_keep = input.copy()

    for i in range(len(input[0])):

        zeros = 0
        ones = 0

        for value in numbers_to_keep:
            if value[i] == '0':
                zeros += 1
            elif value[i] == '1':
                ones += 1
        
        numbers_to_keep_helper = []

        if (zeros > ones and method == 'mstCmn') or (ones > zeros and method == 'lstCmn') or (zeros == ones and method == 'lstCmn'):
            for value in numbers_to_keep:
                if value[i] == '0':
                    numbers_to_keep_helper.append(value)
        elif (ones > zeros and method == 'mstCmn') or (zeros > ones and method == 'lstCmn') or (zeros == ones and method == 'mstCmn'):
            for value in numbers_to_keep:
                if value[i] == '1':
                    numbers_to_keep_helper.append(value)

        numbers_to_keep = numbers_to_keep_helper.copy()
        
        if len(numbers_to_keep) == 1:
            return int(numbers_to_keep[0], 2)
            
oxygen_generator_rating = get_number_to_keep('mstCmn')
co2_scrubber_rating = get_number_to_keep('lstCmn')

print(oxygen_generator_rating * co2_scrubber_rating)