# Python code

my_list = [10,20,30,40,5]


print(my_list[-1],'\n')


for n in my_list:
    print(n)

size = len(my_list)

print(size)

n = 0

while n < size:
    print(my_list[n])
    n+=1

print('Done for today!\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print('The lowest value is', min(numbers))
print('The Max value is', max(numbers))

print(numbers[0:8:3])

print()

# Converting Between Lists and Tuples
number_tuple = (1, 2, 3)
number_list = list(number_tuple)
print(number_list)
str_list = ['one', 'two', 'three']
str_tuple = tuple(str_list)
print(str_tuple)