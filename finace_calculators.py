import math

#Print the menu options.

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("")

#Prompt the user to choose a calculation.

calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#Investment calculator.

if calculation == "investment":
    deposit = float(input("Enter the deposit: "))
    interest_rate = float(input("Enter the interest rate: "))
    years = float(input("Enter the number of years you plan to invest: "))
    type_of_interest = input("Do you want 'simple' or 'compound' interest?")

    #Calculate the total amount of interest
    
    interest = interest_rate / 100
    simple_interest = deposit * (1 + interest * years)
    compound_interest = deposit * math.pow((1+interest), years)

    #Printing out the total amount after user inputs
    print("")
    print("Your deposit is:", deposit)
    print("Your interest rate percentage is:", interest_rate)
    print("Number of years chosen:", years)
    print("Type of interest is:", type_of_interest)
    print("")


    if type_of_interest == 'simple':
        print("The total amount payable with simple interest is:", simple_interest)
    
    elif type_of_interest == 'compound':
        print("The total amount payable with compound interest is:", compound_interest)
    
    else:
        print("You have entered an invalid interest type!")

#Bond calculator
        
elif calculation == "bond":
    house_value = float(input("What is the present house value?:"))
    interest_rate = float(input("What is the annual interest rate?"))
    months = float(input("How many months until you repay?"))
    
    #Caculating monthly interest and repayment
    
    monthly_interest = (interest_rate / 100) / 12

    repayment = (monthly_interest * house_value)/(1 - (1 + monthly_interest) ** (- months))

    #Outputs for bond calculations.
    
    print("")
    print("The present house value is:", house_value)
    print("The annual interest rate is:", interest_rate)
    print("The monthly interest rate is:", monthly_interest)
    print("The number of months chosen for re-payment:", months)
    print("")
    print("The monthly repayment amount is:", repayment)

else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")

    
#Stop
    

    

    
    
