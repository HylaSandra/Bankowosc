import socket

HOST = 'localhost'
PORT = 2137

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()

users = [
    {
        'name': 'Sandra',
        'surname': 'Hyla',
        'PESEL': '99112245678',
        'account_number': '12345678901234567890',
        'balance': '100',
    },
    {
        'name': 'Piotr',
        'surname': 'Kozioł',
        'PESEL': '99112241234',
        'account_number': '12345678901234567891',
        'balance': '200',
    },
    {
        'name': 'Leokadia',
        'surname': 'Czerepach',
        'PESEL': '99112245566',
        'account_number': '12345678901234567892',
        'balance': '300',
    }
]

while True:
    conn.send(b'Podaj swoj PESEL: ')
    pesel = conn.recv(1024).decode('utf-8')
    for user in users:
        if pesel == user['PESEL']:
            user_found = user
            break
    else:
        conn.send(b'Nie znaleziono uzytkownika!\n')
        continue
    break

def welcome(user_found):
    conn.send(b'Czesc ' + user_found['name'].encode('utf-8') + b' ' + user_found['surname'].encode('utf-8') + b'!\n')

welcome(user_found)

options = {
    '1': 'deposit',
    '2': 'withdraw',
    '3': 'transfer',
    '4': 'balance',
}

def deposit(user_found):
    conn.send(b'Podaj kwote do wplaty: ')
    amount = conn.recv(1024).decode('utf-8')
    user_found['balance'] = str(int(user_found['balance']) + int(amount))
    conn.send(b'Twoj nowy stan konta to: ' + user_found['balance'].encode('utf-8') + b'\n')

def withdraw(user_found):
    conn.send(b'Podaj ilosc gotowki do wyplaty: ')
    amount = conn.recv(1024).decode('utf-8')
    if int(amount) > int(user_found['balance']):
        conn.send(b'Zbyt niski stan konta!\n')
    else:
        user_found['balance'] = str(int(user_found['balance']) - int(amount))
        conn.send(b'Twoj nowy stan konta to: ' + user_found['balance'].encode('utf-8') + b'\n')

def transfer(user_found):
    conn.send(b'Podaj kwote do przelewu: ')
    amount = conn.recv(1024).decode('utf-8')
    if int(amount) > int(user_found['balance']):
        conn.send(b'Zbyt niski stan konta!\n')
    else:
        user_found['balance'] = str(int(user_found['balance']) - int(amount))
        conn.send(b'Twoj nowy stan konta to: ' + user_found['balance'].encode('utf-8') + b'\n')

def balance(user_found):
    conn.send(b'Twoj stan konta to: ' + user_found['balance'].encode('utf-8') + b'\n')

def option_handler(option, user_found):
    if option == '1':
        deposit(user_found)
    elif option == '2':
        withdraw(user_found)
    elif option == '3':
        transfer(user_found)
    elif option == '4':
        balance(user_found)

while True:
    conn.send(b'Wybierz opcje:\n1. Wplata\n2. Wyplata\n3. Przelew\n4. Stan konta\n')
    option = conn.recv(1024).decode('utf-8')
    if option in options:
        option_handler(option, user_found)
    else:
        conn.send(b'Niepoprawny wybor!\n')


data = conn.recv(1024)
print(data)
