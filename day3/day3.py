map_ = []

with open('day3.txt') as file_object:
    raw_line = file_object.readlines()
    for line in raw_line:
        map_.append(line.strip('\n'))

def ski(slope_x,slope_y,map):
    max_x = len(map[0])
    max_y = len(map)
    y_pos = 0
    x_pos = 0
    tree_count = 0
    while y_pos < max_y:
        try:
            y_pos += slope_y
            x_pos += slope_x
            if x_pos >= 31:
                x_pos -= 31
            y_check = map_[y_pos]
            x_check = y_check[x_pos]
            if x_check == '#':
                tree_count += 1
        except:
            return tree_count

test1 = ski(1,1,map_)
test2 = ski(3,1,map_)
test3 = ski(5,1,map_)
test4 = ski(7,1,map_)
test5 = ski(1,2,map_)
test = test1 * test2 * test3 * test4 * test5
print(test)