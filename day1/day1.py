num_list = []
counter = 0
two_values = []
three_values = []

with open('day1-1.txt') as n_list:
    nums = [line.rstrip() for line in n_list]
    for num in nums:
        num_list.append(int(num))
    for numbers in num_list:
        for values in range(0,len(num_list)-1):
            if numbers == num_list[values]:
                pass
            else:
                if numbers + num_list[values] == 2020:
                    two_values.append(numbers * num_list[values])
                else:
                    pass

print(two_values[0])

for numbers in num_list:
    for value1 in range(0,len(num_list)-1):
        for value2 in range(0,len(num_list)-1):
            if numbers == num_list[value1]:
                pass
            elif numbers == num_list[value2]:
                pass
            elif num_list[value1] == num_list[value2]:
                pass
            else:
                if numbers + num_list[value1] + num_list[value2] == 2020:
                    three_values.append(numbers * num_list[value1] * num_list[value2])
                else:
                    pass



print(three_values[0])
