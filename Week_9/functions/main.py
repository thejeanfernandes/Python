from functions.id import checkid
from functions.name import checkname
from functions.mail import checkmail


"""This program will take some information from the user and will verify a serious of rules.
The rules are: Employee ID (this is required, and must be a number that is 7 or less digits long)
Employee Name (this is required, and must be comprised of primarily upper and lower case letters. It also cannot contain any of the following characters: ! " @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \ ).
Employee Email Address (this is required, and must be comprised of primarily of alphanumeric characters. It also cannot contain any of the following characters: ! " ' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \ ).
Employee Address (this is not required, but if it is provided, it must be comprised primarily of alphanumeric characters. It cannot contain any of the following characters: ! " ' @ $ % ^ & * _  = + < >  ? ; : [ ] { } )."""

Employee= dict() # empty dictionary
for loop5 in range(5): # loop for 5 iterations
  # user id input
  employee_id = input("Enter the employee ID: ")
  # user name input
  employee_name = input("Enter the employee name: ")
  # user mail input
  employee_mail = input("Enter the employee email: ")
  #user address input
  employee_address = input("Enter the employee address: ")

  try: # test employee address
    if employee_address.isalnum() == False:
      break
    print("Hello, " + checkname(employee_name) + " Your employee ID is " + str(checkid(employee_id)) + " and your email address is " + checkmail(employee_mail) + " and your address is " + employee_address)
  except: # if address not provided
    print("Hello, " + checkname(employee_name) + " Your employee ID is " + str(checkid.checkid(employee_id)) + " and your email address is " + checkmail(employee_mail) + " you did not provide an address.")

Employee[employee_id] = [employee_name, employee_mail, employee_address]

for key, value in Employee.items():
  value.insert(0, key)
  print(value) #print the whole list