import math
# enter while loop in case user input a invalid answer
while True:
    decision = input("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
    if (decision.lower() == "investment"):
        print()
        # greeting and tell user what will happen next
        print("Welcome to our investment calculator. \nHere we will ask you for a few important elements of your investment for the calculation.")
        deposit_money = int(input("\nHow much you are going to depositing? "))
        interest_rate = float(input("\nHow much is the interest rate?\n(Please only input the numbers.\ne.g. input 8 for 8%\ninput 0.5 for 0.5%) "))
        saving_period = int(input("\nHow long you would like to depositing for?\n(Please input the number of years) "))
        # enter while loop in case user input a invalid answer for the interest type
        while True:
            interest = input("\nWhich type of interest will be?\nSimple or Compound? ")
            if (interest.lower() == "simple"):
                total_amount = int(deposit_money * (1 + interest_rate/100 * saving_period))
                print()
                print(f"The total amount will be {total_amount}, after depositing {deposit_money} for {saving_period} years with Simple interest.")
                # break out of the loop as the we have calculated the answer for the user
                break
            elif (interest.lower() == "compound"):
                total_amount = int(deposit_money * math.pow((1 + interest_rate/100), saving_period))
                print()
                print(f"The total amount will be {total_amount}, after depositing {deposit_money} for {saving_period} years with Compound interest.")
                # break out of the loop as the we have calculated the answer for the user
                break
            else:
                print("Sorry, input not valid. Please try again.\n")
        break
    elif (decision.lower() == "bond"):
        print()
        # greeting and tell user what will happen next
        print("Welcome to our bond calculator. \nHere we will ask you for a few important elements of your bond for the calculation.")
        house_value = int(input("\nHow much the house worth at the moment? "))
        interest_rate = float(input("\nHow much is the interest rate?\n(Please only input the numbers.\ne.g. input 8 for 8%\ninput 0.5 for 0.5%) "))
        repay_period = int(input("\nHow long you would like to repay for the bond?\n(Please input the number of months) "))
        repayment = (interest_rate/1200 * house_value) / (1 - (1 + interest_rate/1200) ** (-repay_period))
        print()
        print(f"You will need to repay {repayment} each month for the house over {repay_period} months.")
        # break out of the loop as the we have calculated the answer for the user
        break
    else:
        print("Sorry, input not valid. Please try again.\n")