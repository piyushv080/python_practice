#function 
calculation_to_units = 26
name_of_unit = "hours"

def days_to_unit():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_unit()

#fn input parameter
def days_to_unit(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_unit(35)

# days_to_unit()

# two input parameter
def days_to_unit(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_unit(50,"Interesting!")

# variable scope in function
def scope_check():
    print(name_of_unit) #global variable
   # print(num_of_days) # local variable

scope_check(20)