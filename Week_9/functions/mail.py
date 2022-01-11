# function to test email
def checkmail(employee_mail):

    '''checks the employee email 
    Arguments:
            employee_email
    Returns:
        exit if the email does not follow the rules or return the email if pass the rule.     
    '''  

    if(employee_mail.isalnum() == False):
        employee_mail.replace('@', '')
        employee_mail.replace('.','')
    if(employee_mail.isalnum == False):
        exit()
    return employee_mail