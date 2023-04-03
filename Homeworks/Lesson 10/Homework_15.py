input_string = ['', '']


def input_function(n=2):
    input_string_local = ['', '']
    for j in range(n):
        input_string_local[j] = input()
        
    input_string_local = list(map(lambda x: x + '\n', input_string_local))
    return input_string_local


print('Input four strings')
for i in range(2):
    input_string[i] = input_function()
print(input_string)

try:
    file = open('my_file.txt', 'w')
    file.writelines(input_string[0])
finally:
    file.close()

with open('my_file.txt', 'a') as file:
    file.writelines(input_string[1])
