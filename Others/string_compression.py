__author__ = 'Meghna'

input_string = 'AAABBCCCCCCAAAAA'
length = len(input_string)
output_string = ''
idx = 0
while idx < length:
    count = 1
    while idx + count < length and input_string[idx] == input_string[idx + count]:
        count +=1
    output_string += str(count)
    output_string += input_string[idx]
    idx = idx + count
print output_string
