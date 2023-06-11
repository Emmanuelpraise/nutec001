# Simple Ticket Booking System By Emmanuel Praise.
db = []


def get_name():
    name = input('Please enter your name: ')
    return name


def get_mail():
    email = input('Please enter your email: ')
    return email


def get_ticket():
    ticket_type = input(
        'Enter the type of ticket you want, \nAvailable options include: Regular, VIP, VVIP, Premium: ')
    return ticket_type


def finalize(name, email, ticket_type):
    print(f'''\
    You have successfully registered for the NUTEC Festival Event
    Name  : {name}
    E-mail: {email}
    Ticket: {ticket_type}''')


regular = 100
vip = 50
vvip = 40
premium = 10
available_tickets = regular + vip + vvip + premium

while available_tickets > 0:
    print('Welcome to the NUTEC booking system')
    name = get_name()
    email = get_mail()
    ticket = get_ticket().lower()
    mydb = {'name': name, 'email': email, 'ticket': ticket}

    exists = False
    for record in db:
        if mydb['name'] == record['name'] and mydb['email'] == record['email']:
            exists = True
            print('Name and email already exist!\nPlease try again')
            break
        elif mydb['name'] == record['name']:
            exists = True
            print('Name already exists!\nPlease try again')
            break
        elif mydb['email'] == record['email']:
            exists = True
            print('Email already exists!\nPlease try again')
            break

    if not exists:
        if ticket == 'regular' and regular > 0:
            regular -= 1
        elif ticket == 'vip' and vip > 0:
            vip -= 1
        elif ticket == 'vvip' and vvip > 0:
            vvip -= 1
        elif ticket == 'premium' and premium > 0:
            premium -= 1
        else:
            print(
                'Invalid ticket selection or no more tickets available. Please try again.')
            continue
        db.append(mydb)
        available_tickets -= 1
        finalize(name, email, ticket)

    print(f'''\
           Regular: {regular} tickets,
           VIP    : {vip} tickets,
           VVIP   : {vvip} tickets,
           Premium: {premium} tickets,
           TOTAL: {regular + vip + vvip + premium} tickets left''')
