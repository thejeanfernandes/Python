# function to test employee_name

'''checks if the employee name
Arguments:
        employee_name
Returns:
     exit if the name does not follow the rules or return the name if pass the rule.     
'''  

def checkname(employee_name):
    if(employee_name.isalpha() == False):
        exit()
    return employee_name