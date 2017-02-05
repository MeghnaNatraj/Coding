__author__ = 'Meghna'

from datetime import datetime
import math
start=datetime.now()
for times in range(0,1000):
    input = ['ABCW','BAZ', 'FOO', 'BAR', 'XTN', 'ABCDEF','YTHRFYG','WHRID','WHRH','ESI','EUSIV','RUWOC','SPWN','WIFHC']
    max = 0
    input.sort(key=len,reverse=True)
    input_length = len(input)
    set_array = [set(item) for item in input]
    for i in range(0,input_length):
        if math.pow(len(input[i]),2) < max: break
        for j in range(i+1,input_length):
                if not set_array[i].intersection(set_array[j]):
                    length = len(input[i])*len(input[j])
                    if length > max:
                        max = length
#     print(max)
print(datetime.now()-start)
print(max)

# Time Complexity - max(n^2 * m)
# Space Complexity - mn
#
# Brute force
# from datetime import datetime
# start=datetime.now()
# for times in range(0,1000):
#     input = ['ABCW','BAZ', 'FOO', 'BAR', 'XTN', 'ABCDEF','YTHRFYG','WHRID','WHRH','ESI','EUSIV','RUWOC','SPWN','WIFHC']
#     max = 0
#     for i in range(0,len(input)):
#         for j in range(i+1,len(input)):
#                 flag = True
#                 for c in input[i]:
#                     if c in input[j]:
#                         flag = False
#                 if flag :
#                     length = len(input[i])*len(input[j])
#                     if length > max:
#                         max = length
# #     print(max)
# print(datetime.now()-start)
# print(max)