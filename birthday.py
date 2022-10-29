import datetime

print('---------------------------------------------------------------------------')

print('\nThis program tells you every info you need to know abt your birthday\nLet\'s start\n')

# Take in the users info 

stampDate = datetime.datetime.now() # a snapshot of day, month, year, time

year_o_b = int(input('Enter your year of birth please: \n')) # year of birth

age_in_years = int(stampDate.strftime('%Y')) - year_o_b # Age in years

month_o_b = int(input('Enter you month of birth please: \n')) # month of birth

todaysMonth = stampDate.strftime('%m') # current month as a number

day_o_b = int(input('Enter day of birth: \n')) # day of birth

today = stampDate.strftime('%d') # today as a number

age_in_months = int(todaysMonth) - month_o_b #age in months

if age_in_months > 0:
    pass
else:
     age_in_months = int(todaysMonth)


age_in_days = int(today) - day_o_b 

if age_in_days > 0:
    pass
else:
    age_in_days = int(today)

print(f'\nYou have, so far, lived {age_in_years} years, {age_in_months} months and {age_in_days} days\n')
