with open('C:/Users/rmorran001/Documents/Python Scripts/Advent of Code/2021/Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def create_binary_str(method):

    binary_str = ''

    for i in range(len(input[0])):
        zeros = 0
        ones = 0
        for value in input:
            if value[i] == '0':
                zeros += 1
            elif value[i] == '1':
                ones += 1
        if (zeros > ones and method == 'mstCmn') or (ones > zeros and method == 'lstCmn'):
            binary_str = binary_str + '0'
        elif (ones > zeros and method == 'mstCmn') or (zeros > ones and method == 'lstCmn'):
            binary_str = binary_str + '1'

    return int(binary_str, 2)

gamma_rate = create_binary_str('mstCmn')
epsilon_rate = create_binary_str('lstCmn')

print(gamma_rate * epsilon_rate)