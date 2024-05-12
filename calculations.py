#website that makes budgeting simple
#user can enter income and expenses
#program lists weekly and monthly expenses and totals them
#user will be able to pick the time frame they would like to budget.


#Put monthly expenses in a dictionary (expense:amount)
def monthly_expense():
    expense = {}
    while True:
        name_of_expense = input('Monthly Expense Name (type \'done\' once all expenses are in): ')
        if name_of_expense.lower() == 'done':
            break
        try:
            if name_of_expense.isdigit():
                raise ValueError("Please enter a valid expense name")
            price = None
            while price is None:
                price_input = input('Enter Amount: ')
                try:
                    price = float(price_input)
                except ValueError:
                    print('Please enter a valid amount')
        except ValueError as ve:
            print(ve)
            continue
        if not name_of_expense.strip():
            print('Please enter valid expense name')
            continue
        expense[name_of_expense] = price
    return expense

# Use these variables to calculating (adding expenses, subtracting from monthly income, etc.)
monthly_expense_values = monthly_expense()
total_monthly_expense = sum(monthly_expense_values.values())

print()
print()
#Display monthly expenses and show total
print('Monthly Expense          Amount')
print('--------------------------------')
for name_of_expense, price in monthly_expense_values.items():
    print(f'    {name_of_expense}                 {price:.2f}')
print(f'                  Total: ${total_monthly_expense:.2f}')
print()
print()



#Put weekly expenses in a dictionary (weekly_expense:amount)
def weekly_expense():
    expense = {}
    while True:
        name_of_expense = input(str('Weekly Expense Name (type \'done\' once all expenses are in): '))
        if name_of_expense.lower() == 'done':
            break
        try:
            if name_of_expense.isdigit():
                raise ValueError("Please enter a valid expense name")
            price = None
            while price is None:
                price_input = input('Enter Amount: ')
                try:
                    price = float(price_input)
                except ValueError:
                    print('Please enter a valid amount')
        except ValueError as ve:
            print(ve)
            continue
        if not name_of_expense.strip():
            print('Please enter valid expense name')
            continue
        expense[name_of_expense] = price
    return expense

weekly_expense_values = weekly_expense()
total_weekly_expense = sum(weekly_expense_values.values())
print()
print()
#Display weekly expenses and show total
print('Weekly Expense          Amount')
print('--------------------------------')
for name_of_expense, price in weekly_expense_values.items():
    print(f'    {name_of_expense}                ${price:.2f}')
print(f'                  Total: ${total_weekly_expense:.2f}')
print()
print()



#Loop to get the user income and how they would like to budget their income
# Calculate mthly_including_weekly within a try/except block to handle ValueError
try:
    mthly_including_weekly = (total_weekly_expense * 4) + total_monthly_expense
except ValueError:
    print("Invalid input. Please make sure the values for total_weekly_expense and total_monthly_expense are valid numbers.")

# Prompt the user to enter their income
while True:
    user_income_input = input('Enter the amount you are trying to budget with (payday amount): ')
    try:
        user_income = float(user_income_input)
        break
    except ValueError:
        print('Please enter a valid number for your income.')




# Prompt the user to enter the budget period
#The user should only be able to enter a valid budget period (week, bi-weekly, month, year, or close to)
while True:
    budget_period = input('How long do you want to budget this amount for - Week, Bi-Weekly, Month, Year?: ').lower()
    if budget_period in ['Weekly', 'weekly', 'week', 'Week', 'bi-weekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly',
                         'Biweekly', 'Monthly', 'monthly', 'Month', 'month', 'Year', 'Yearly', 'year', 'yearly']:
        break
    else:
        print('Please enter valid budget period.')



#Do the budget calculations based on the budget period input
#Use a list to branch into each calculation and output
#If user does not make enough to budget for the time frame selected tell them how much they are short
#FIXME: Check print out of income after expense if it is negative
if budget_period in ['Weekly', 'week', 'Week', 'weekly']:
    week = mthly_including_weekly / 4
    income_after_expense = user_income - week
    if income_after_expense < 0:
        print()
        print(f'You are short ${-income_after_expense:.2f} to budget your monthly bills this week.')
        print()
        print('Your Income to Expense Breakdown')
        for expense, value in monthly_expense_values.items():
            print(f'{expense}    :    ${value:.2f}')
        for expense, value in weekly_expense_values.items():
            print(f'{expense}    :    ${value:.2f} * 4')
        print(f'Total Monthly Expense (including weekly): ${mthly_including_weekly:.2f}')
        print(f'Amount needed to budget for week: {week:.2f}')
        print(f'Income this period: ${user_income:.2f}')
        print(f'Week Expense: -${week:.2f}')
        print(f'Loss: -${income_after_expense:.2f}')
    else:
        print()
        print(f'You need to put aside ${week:.2f} per week to make your monthly bills. '
          f'You have ${income_after_expense:.2f} left over after budgeting ${user_income:.2f} weekly')
        print()
elif budget_period in ['bi-weekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly', 'Biweekly']:
    biweekly = mthly_including_weekly / 2
    income_after_expense = user_income - biweekly
    if income_after_expense < 0:
        print()
        print(f'You are short ${-income_after_expense:.2f} to budget your monthly bills bi-weekly.')
        print()
        print('Your Income to Expense Breakdown')
        for expense, value in monthly_expense_values.items():
            print(f'{expense}    :    ${value:.2f}')
        for expense, value in weekly_expense_values.items():
            print(f'{expense}    :    ${value:.2f} * 2')
        print(f'Total Monthly Expense (including weekly): ${mthly_including_weekly:.2f}')
        print(f'Amount needed to budget bi-weekly: {biweekly:.2f}')
        print(f'Income this period: ${user_income:.2f}')
        print(f'Week Expense: -${biweekly:.2f}')
        print(f'Loss: -${income_after_expense:.2f}')
    else:
        print()
        print(f'You need to put aside ${biweekly:.2f} from your bi-weekly pay to make your monthly bills.'
          f'You will have ${income_after_expense:.2f} after budgeting ${user_income:.2f} bi-weekly.')
        print()
elif budget_period in ['Monthly', 'monthly', 'Month', 'month']:
    income_after_expense = user_income - mthly_including_weekly
    if income_after_expense < 0:
        print()
        print(f'You are short ${-income_after_expense:.2f} to budget your monthly bills this month.')
        print()
        print('Your Income to Expense Breakdown')
        for expense, value in monthly_expense_values.items():
            print(f'{expense}    :    ${value:.2f}')
        for expense, value in weekly_expense_values.items():
            print(f'{expense}    :    ${value:.2f} * 4')
        print(f'Total Monthly Expense (including weekly): ${mthly_including_weekly:.2f}')
        print(f'Amount needed to budget for a month: {mthly_including_weekly:.2f}')
        print(f'Income this period: ${user_income:.2f}')
        print(f'Week Expense: -${mthly_including_weekly:.2f}')
        print(f'Loss: -${income_after_expense:.2f}')
    else:
        print()
        print(f'You need to put aside ${mthly_including_weekly:.2f} to make your monthly bills.'
          f'You have ${income_after_expense:.2f} after budgeting ${user_income:.2f} for the month.')
        print()
elif budget_period in ['Year', 'Yearly', 'year', 'yearly']:
    year = mthly_including_weekly * 12
    income_after_expense = user_income - year
    if income_after_expense < 0:
        print()
        print(f'You are short ${-income_after_expense:.2f} to budget your monthly bills for a year.')
        print()
        print('Your Income to Expense Breakdown')
        for expense, value in monthly_expense_values.items():
            print(f'{expense}    :    ${value:.2f}')
        for expense, value in weekly_expense_values.items():
            print(f'{expense}    :    ${value:.2f} *')
        print(f'Total Annual Expense: ${year:.2f}')
        print(f'Amount needed to budget for a year: {year:.2f}')
        print(f'Income this period: ${user_income:.2f}')
        print(f'Week Expense: -${mthly_including_weekly * 12:.2f}')
        print(f'Loss: -${income_after_expense:.2f}')
    else:
        print()
        print(f'You need to put aside ${year:.2f} to pay your monthly bills for a year.'
          f'You have ${income_after_expense:.2f} after budgeting ${user_income:.2f} for a year.')
        print()






#prompt the user to be able to enter their saving preferences
#create two branch types if the user has enough to save.
if income_after_expense > 0:
    while True:
        savings = str(input('Would you like to put away for a rainy day? (Y/N?): '))
        if savings in ['Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no']:
            break
        else:
            print('Please enter valid input.')

    #This is the start of the YES Branch (to saving money) must have more than $0 of leftover income.
    if savings in ['Y', 'y','Yes','yes']:
        week = mthly_including_weekly / 4
        biweekly = mthly_including_weekly / 2
        year = mthly_including_weekly * 12
        print()
        print()
        print('A good place to start your savings is 10% of your income (after expenses),'
          ' however, you can customize how much of your income after expenses'
          ' to save ')
        print()
        print()

#Usr should only be able to enter a valid savings pct (only a float between 1 and 100)
        while True:
            select_savings_pct = input('Enter the percentage (ex: 10, 10.5, etc.): ')
            try:
                select_savings = float(select_savings_pct)
                if 1 <= select_savings <= 100:
                    # convert the entered number to a percentage and store in variable
                    save = income_after_expense * (select_savings / 100)
                    print(f'You will need to put away ${save:.2f} from your left over money (${income_after_expense:.2f})'
                        f' to save {select_savings:.1f}% of your income after expenses.')
                    print()
                    break
                else:
                    print('Please enter a percentage between 1 and 100')
            except ValueError:
                print('Please enter a valid number')


            print()
    #print the totals for the user to see the breakdown of their expenses and savings
    #Print the 4 different kind of bidget offered by the program and include savings if is eligable or opted to save
        if budget_period in ['Weekly', 'weekly', 'week', 'Week']:
            print()
            print('Here is your Weekly Budget Overview')
            print()
            print('Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'  {expense}     :     ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'  {expense}     :     ${value:.2f} * 4 (weekly)')
            print(f'Total Weekly Expense: ${mthly_including_weekly:.2f} / 4 = ${week:.2f} per week')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Save: ${save:.2f}')
            print(f'Income After expenses and savings: ${income_after_expense - save:.2f}')
            print()

        if budget_period in ['bi-weekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly', 'Biweekly']:
            print()
            print(f'Here is your Bi-Weekly Budget Overview')
            print()
            print('Month Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'   {expense}    :    ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 4 (weekly)')
            print(f'Total Bi-Weekly Expense: ${mthly_including_weekly:.2f} / 2 = ${biweekly:.2f} bi-weekly')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Save: ${save:.2f}')
            print(f'Income After expenses and savings: ${income_after_expense - save:.2f}')
            print()

        if budget_period in ['Monthly', 'monthly', 'Month', 'month']:
            print()
            print(f'Here is your Monthly Budget Overview')
            print()
            print(f'Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 4 (weekly)')
            print(f'Total Monthly Expesnse: ${mthly_including_weekly:.2f} per month')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Save: ${save:.2f}')
            print(f'Income After expenses and savings: ${income_after_expense - save:.2f}')
            print()

        if budget_period in ['Year', 'Yearly', 'year', 'yearly']:
            print()
            print(f'Here if you Annual Budget Overview')
            print(f'Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 12')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    (${value:.2f} * 4) * 12')
            print(f'Total Annual Expense: ${mthly_including_weekly:.2f} * 12 = ${year:.2f} per year')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Save: ${save:.2f}')
            print(f'Income After expenses and savings: ${income_after_expense - save:.2f}')
            print()




    #'NO' branch for users who decided not to save if they have the option (print their budget)
    #This branch should not have a save variable
    if savings in ['N', 'n', 'No', 'no']:
        week = mthly_including_weekly / 4
        biweekly = mthly_including_weekly / 2
        year = mthly_including_weekly * 12
        if budget_period in ['Weekly', 'weekly', 'week', 'Week']:
            print()
            print('Here is your Weekly Budget')
            print()
            print(f'Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'  {expense}     :     ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'  {expense}     :     ${value:.2f} * 4')
            print(f'Total Weekly Expense: ${(total_weekly_expense * 4) + total_monthly_expense:.2f} / 4 = ${week:.2f} per week')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Income After expenses: ${income_after_expense:.2f}')
            print()
        if budget_period in ['bi-weekly', 'biweekly', 'Bi-Weekly', 'Bi-weekly', 'Biweekly']:
            print()
            print(f'Here is your Bi-Weekly Budget Overview')
            print()
            print('Month Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'   {expense}    :    ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 4 (weekly)')
            print(f'Total Bi-Weekly Expense: ${mthly_including_weekly:.2f} / 2 = ${biweekly:.2f} bi-weekly')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Income After expenses: ${income_after_expense:.2f}')
            print()
        if budget_period in ['Monthly', 'monthly', 'Month', 'month']:
            print()
            print(f'Here is your Monthly Budget Overview')
            print()
            print(f'Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f}')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 4 (weekly)')
            print(f'Total Monthly Expense: ${mthly_including_weekly:.2f} per month')
            print(f'Income this period: ${user_income:.2f}')
            print(f'After expenses: ${income_after_expense:.2f}')
            print()
        if budget_period in ['Year', 'Yearly', 'year', 'yearly']:
            print()
            print(f'Here if you Annual Budget Overview')
            print()
            print(f'Monthly Expense Name    :    Monthly Expense Amount')
            for expense, value in monthly_expense_values.items():
                print(f'    {expense}    :    ${value:.2f} * 12')
            for expense, value in weekly_expense_values.items():
                print(f'    {expense}    :    (${value:.2f} * 4) * 12 (annually)')
            print(f'Total Annual Expense: ${mthly_including_weekly * 12:.2f} * 12 = ${year:.2f} per year')
            print(f'Income this period: ${user_income:.2f}')
            print(f'Income After expenses: ${income_after_expense:.2f}')
            print()






#else:
    #if income_after_expense < 0:
        #print('You are here')
     ##   if budget_period in ['Weekly', 'weekly', 'week', 'Week']:


#FIXME: Write an Else branch for the if statement for when the user income after expesense is less than 0`
#PHYSICALLY DRAW THE DESIRED PRINT OUT OF THE BUDGET OVERVIEW








