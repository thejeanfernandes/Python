# function to test employee_id
def checkid(employee_id):

    '''checks the lengh of the employee id
Arguments:
        employee id
Returns:
     exits if its not the right length or return the variable if it is the right lengh        
'''  

    if(len(employee_id) > 7):
        exit()
    else:
        employee_id = int(employee_id)
    return employee_id