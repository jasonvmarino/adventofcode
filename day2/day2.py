c_passwords = []
n_passwords = []
pass_letters = []

with open('day2.txt') as file_object:
    info = file_object.readlines()
    for passwords in info:
        h_num = passwords.find('-')
        num1 = passwords[0:h_num]
        s_num = passwords.find(' ')
        num2 = passwords[h_num+1:s_num]
        pass_letter = passwords[s_num+1]
        password = passwords[s_num+4:]
        for pass_ in password:
            pass_.strip('\n')
        if int(num1) <= password.count(pass_letter) <= int(num2):
            c_passwords.append(passwords)
        letter_one = password[int(num1)-1]
        letter_two = password[int(num2)-1]
        if letter_one != letter_two:
            if letter_one == pass_letter:
                n_passwords.append(passwords)
            elif letter_two == pass_letter:
                n_passwords.append(passwords)
print(len(c_passwords))
print(len(n_passwords))