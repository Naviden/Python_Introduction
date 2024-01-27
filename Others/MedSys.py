import time
import sys
sys.path.insert(1, './Data/emp_data')
from emp_db import emp_info

print('Welcome to MedSys!')
time.sleep(1)

while True:
    emp_num = input('Employee Number ?')
    emp_pass = input('Employee Password ?')

    if emp_pass == str(emp_info[emp_num]['password']):
        print(f'Welcome to MedSys {emp_info[emp_num]["name"]} {emp_info[emp_num]["surname"]} !')
        time.sleep(0.5)
        break
    else:
        print('No match between employee number and password\nPlease insert them again ')
    

