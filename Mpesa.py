# This is an Mpesa-alike app that works almost the same as the famous Mpesa program
# This program was developed only for fun and practice with no illegal intent in mind!

import secrets
import string
import datetime
import json
import smtplib
import ssl

username = input('Enter your name to start: \n').capitalize() # The name the program will refer to you as

import ast # for converting strings to dicts
# checking whether the user exists in the customer records and if not return False...
def check_user():
    try:
        with open('mpesa_clientDetails.txt') as userDetails: # opens file as read mode in text format by default
            for line in userDetails.readlines():
                dict_line = ast.literal_eval(line) # converting string to dictionary to enable key-checking
                if dict_line['name'] == username:
                    print('------------------------------------------')
                    print(f'Welcome {username.capitalize()}... So glad to have you back \n')
                    return True 
    except:
        open('mpesa_clientDetails.txt', 'w') # if ur running this program for the first time, then it creates the #file first
        check_user() # then it runs the function again
    return False 

# Incase user is not in our records, system creates a new record for them
def createNewUser():
    now = datetime.datetime.now()
    now_time = now.strftime("%x")
    if not check_user():
        user_id = generate_userId()
        userAccount = str({'name': username.capitalize(), 'user_id': user_id, 'date_created': now_time})

        # Opens the general file for all Mpesa clients and writes a new record.
        with open('mpesa_clientDetails.txt', 'a') as writeNewUser:
            writeNewUser.write(userAccount + '\n')

            print('\n--------------------------------------------------')
            print(f'{username.capitalize()}\'s details have been captured. Welcome aboard\n')

        # creates a separate personal file for users to store more personal info and transactions

        user_file = f'{username}\'s_file.json' # name of the personal file
        try:
            with open(user_file, 'x') as userFileCreate: # checks whether file is already present and exits if so

                userPersonalAccountDetails = {'name': username, 'pin': 2022, 'user_id': user_id, 'date_created': now_time, 'exact_time_created': now.strftime('%X'), 'accnt_bal': 5000, 'loan_bal': 0, 'credit_worthiness': 'perfect'}

                userPersonalObject = dict(client_details = userPersonalAccountDetails, Transaction_history=[])

                json.dump(userPersonalObject, userFileCreate)

                print(f'\n{username.capitalize()}, your personal accounts file has been created.')
                print('------------------------------------------------\n')
        except:
            print(f'\nLooks like {username}\'s file is present...\n')
    return 

# generates random user_id using the secrets module
def generate_userId():
    user_id = username+'-'+secrets.token_urlsafe()
    return user_id

createNewUser()


# After running the checks and what-not, we now begin the transaction processing

def sendMoney(name, amount, pin):

    sender_fname = f'{username.capitalize()}\'s_file.json' # clients file name calculated

    with open(sender_fname) as readDetails: 
         loaded_data = json.load(readDetails) # convert loaded json to python dictionary
        
    userbal = loaded_data['client_details']['accnt_bal']
    userpin = loaded_data['client_details']['pin']

    # checks to ensure logical processing and correct pin
    try:
        assert userbal > amount, 'Too little balance'
    except AssertionError:
        print('\nBalance error... check your balance!\n')
        return
    try:
        assert userpin == pin, 'Wrong pin, do again please.'
    except AssertionError:
        print('\nWrong pin... Try again please...\n')
        return

    new_user_bal = userbal - amount
    loaded_data['client_details']['accnt_bal'] = new_user_bal # calculating new accnt balance

    
    # creating a secure transaction id
    password = string.ascii_uppercase + string.digits
    trans_id = ''.join(secrets.choice(password) for i in range(12))

    # time when transaction was sent
    time_sent = datetime.datetime.now()
    time_sent_formatted = time_sent.strftime('%X')

    #update transanction histry list
    loaded_data['Transaction_history'].append(f'Kshs. {amount} Sent to {name} at {time_sent_formatted} with transaction_id: {trans_id}. New balance is Kshs.{new_user_bal}')

    # write the updated dictionary with this client's details to their file.
    with open(sender_fname, 'w') as reWriteFile:
        updatedInfo = json.dump(loaded_data, reWriteFile)

    # Updates receivers file
    receiver_fname = f'{name.capitalize()}\'s_file.json'

    try:
        with open(receiver_fname) as read:
            readData = json.load(read)
    except:
        print('\nSorry but no such user!\n')
        return 
    r_balance = readData['client_details']['accnt_bal']
    new_r_balance = amount + r_balance
    readData['client_details']['accnt_bal'] = new_r_balance # updating recipient account balance

    readData['Transaction_history'].append(f'Received Kshs.{amount} from {username} at {time_sent_formatted} with transaction_id: {trans_id}. New balance is {new_r_balance}')

    # writing the updated info back
    with open(receiver_fname, 'w') as write:
        json.dump(readData, write)


    
    # alerting the user of the successful transaction
    print('----------------------------------------------------------------------------------')
    print(f'\n{trans_id} Confirmed. Kshs. {amount} sent to {name.upper()} on {time_sent_formatted}. New balance is {new_user_bal}\n')
    print('-----------------------------------------------------------------------------------')

def withdrawCash(agent_no, amount, pin):
    user_fname = f'{username.capitalize()}\'s_file.json'
    with open(user_fname) as withdraw:
        userdata = json.load(withdraw)
        userbal = userdata['client_details']['accnt_bal']
        userpin = userdata['client_details']['pin']
    
    # checks amount
    try:
        assert amount < userbal, 'Your balance is too low to make this transaction'
    except:
        print('Balance is too low to complete this transaction')
        return 

    # checks pin
    try:
        assert userpin == pin, 'Your balance is too low to make this transaction'
    except:
        print('Balance is too low to complete this transaction')
        return 
    
    # writes back update to file
    # time when transaction was sent
    time_sent = datetime.datetime.now()
    time_sent_formatted = time_sent.strftime('%X')

    password = string.ascii_uppercase + string.digits
    trans_id = ''.join(secrets.choice(password) for i in range(12))

    new_userbal = userbal - amount

    userdata['Transaction_history'].append(f'Kshs. {amount} Withdrawn at {agent_no} at {time_sent_formatted} with transaction_id: {trans_id}. New balance is Kshs.{new_userbal}')

    # actual write
    with open(user_fname, 'w') as write:
        json.dump(userdata, write)
    
    print('-------------------------------------------------------------------------------------')
    print(f'Kshs. {amount} Withdrawn at {agent_no} at {time_sent_formatted} with transaction_id: {trans_id}. New balance is Kshs.{new_userbal}')
    print('-------------------------------------------------------------------------------------')




def myAccountDetails(): # a function to check account details
    # requesting transaction history

    filename = f'{username.capitalize()}\'s_file.json'

    with open(filename) as rd:
        data = json.load(rd)

    # asks user whether to use email or whatsapp or just print on terminal
    wayToPrint = int(input('\nHow would you like to print youre transaction histry?\n1-print here and now...\n2-send as email...\n3. Send as whatsapp message...\n'))

    if wayToPrint == 1:
        time = datetime.datetime.now()
        local_time = time.strftime('%c')
        print('-----------------------------------------------------------------------------------')
        print(f'{username}\'s account info as of: {local_time} from most recent to oldest:\n') 
        print('-----------------------------------------------------------------------------------')
        print('\n'+'\n\n'.join(data['Transaction_history'][::-1])+'\n')

    elif wayToPrint == 3:
        print('\nThis feature is not yet created for now, a future update will contain it!\n')

    elif wayToPrint == 2:
        ctx = ssl.create_default_context()
        receiver = input('enter your email address please...e.g: user1@example.com:\n')
        sender = 'henrymsechu1@gmail.com'
        password = 'vuomwejdmseauxru' # app password as provided by google two-step auth goes here... cant share due to security reasons
        content = '\n'+'\n\n'.join(data['Transaction_history'][::-1]) 
        message = f"""\
            From: "Simon-Muthungu" <henrymsechu1@gmail.com>
            To: "You my friend" <receiveradress@host.com>
            Subject: Here's youre transaction history as per Simons app...

            {content}
        """
        print(f'Sending {username.capitalize()} info to {receiver}...')
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as sendMail:
                sendMail.login(sender, password)
                sendMail.sendmail(sender, receiver, message)
                print('------------------------------------------------------------------------------------')
                print(f'\nA mail has successfully been sent to {receiver} at {local_time} with info on {username.capitalize()}\'s details\n')
                print('-----------------------------------------------------------------------------------')
        except: 
            print('\nThere was some error while sending this mail... Maybe check youre internet connection please\n')
            return
        # funnily enough, there are instances where an error message is displayed but the message is sent to the recipient. I guess not all errors result in not sending a mail!
        

        

userAction = int(input("What would you like to do? \n1 - send money or\n2 - withdraw cash\n3 - Check account details\n")) 
if userAction == 1: # send money option
    name = input('Please enter name of recipient...\n')
    amount = int(input('Please enter amount to send from your account...\n'))
    pin = int(input('Please enter your pin number...\n'))
    sendMoney(name,amount,pin)

elif userAction == 2: # withdraw money option
    agent_no = input('Please enter agent...\n')
    amount_to_withdraw = int(input('Please enter amount to withdraw from your account...\n'))
    pin = int(input('Please enter your pin number...\n'))
    withdrawCash(agent_no,amount_to_withdraw,pin)

elif userAction == 3:
    myAccountDetails()