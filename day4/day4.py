new_data = []
passenger = {}
data_check = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eye_color = ['amb','blu','brn','gry','grn','hzl','oth']
a_character = ['1234567890abcdef']
check_counter = 0
total_valid = 0
actual_valid = 0

def check_values(key,value):
    if key == 'byr' and 1920 <= int(value) <= 2020:
        return True
    if key == 'iyr' and 2010 <= int(value) <= 2020:
        return True
    if key == 'eyr' and 2020 <= int(value) <= 2030:
        return True
    if key == 'hgt' and 'cm' in value:
        if 150 <= int(value.strip('cm')) <= 193:
            return True
    if key == 'hgt' and 'in' in value:
        if 59 <= int(value.strip('in')) <= 76:
            return True
    if key == 'hcl':
        if value[0] == '#':
            if len(value) == 7:
                return True
    if key == 'ecl' and value in eye_color:
        return True
    if key == 'pid' and len(str(value)) == 9:
        return True

with open('day4.txt') as file_object:
    raw_data = file_object.readlines()
    for data in raw_data:
        n_data = data.replace(' ','\n')
        t_data = n_data.splitlines()
        for items in t_data:
            new_data.append(items)
    new_data.append('')

for items in new_data:
    temp_counter = 0
    if items != '':
        passenger[items[:3]] = items[4:]
    else:
        try:
            del passenger['cid']
        except:
            pass
        check_counter = len(passenger.keys())
        if check_counter == 7:
            total_valid += 1
        for key,value in passenger.items():
            if check_values(key,value):
                temp_counter += 1
            if temp_counter == 7:
                actual_valid += 1
        passenger = {}

print(total_valid)
print(actual_valid)