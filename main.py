read_lines = []
c_max = 0
seat_value_list = []
seat_taken_list = []

with open('day5.txt') as file_object:
    raw_lines = file_object.readlines()
    for lines in raw_lines:
        read_lines.append(lines[:-1])

for nums in range(35,886):
    seat_value_list.append(nums)

for lines in read_lines:
    binary = lines.replace('B','1').replace('F','0').replace('R','1').replace('L','0')
    row = binary[0:7]
    column = binary[7:]
    seat_id = (int(row,2)*8)+int(column,2)
    seat_taken_list.append(seat_id)
    if seat_id in seat_value_list:
        seat_value_list.remove(seat_id)
    if seat_id > c_max:
        c_max = seat_id

print(c_max)
print(seat_value_list)
