def divideTwoNumbers(passed_list):
    '''Processes a list of numbers, and devides one number by the other
Arguments:
        passsed_list [list of dictionaries] -- each disctionary has the format of [top_number: int, bottom_number: int}
Returns:
        a list of valus obtained when we devide top+number by bottom_number for each dictionary        
'''    
    divide_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 2

    for divide_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(divide_vals["top_number"])
        except:
                print("The first parameter is not an integer")
                numbers_ok = False
        try:
            passed_number2 = int(divide_vals["bottom_number"])
        except:
                print("The second number is not an integer")
                numbers_ok = False
            
        if numbers_ok:
                divide_results = passed_number1 / passed_number2
                divide_results.append(divide_result)
            
        return divide_results

def MultiplyTwoNumbers(passed_list):
    '''Processes a list of numbers, and multiplies one number by the other
Arguments:
        passsed_list [list of dictionaries] -- each disctionary has the format of [top_number: int, bottom_number: int}
Returns:
        a list of valus obtained when we multiply top+number by bottom_number for each dictionary        
'''       
    Multiply_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 2

    for Multiply_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(Multiply_vals["top_number"])
        except:
                print("The first parameter is not an integer")
                numbers_ok = False
        try:
            passed_number2 = int(Multiply_vals["bottom_number"])
        except:
                print("The second number is not an integer")
                numbers_ok = False
            
        if numbers_ok:
                divide_results = passed_number1 * passed_number2
                divide_results.append(multiply_result)
            
        return Multiply_results