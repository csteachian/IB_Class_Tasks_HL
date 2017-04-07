# Input Validation

def validate(lower, upper, message):
    userinput = int(input(message))
    while userinput < lower or userinput > upper:
        print("Error. Try again. The number should be ",lower,"-",upper)
        userinput = int(input(message))
    return userinput


