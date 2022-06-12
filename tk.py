import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2137))

response = s.recv(1024)
print(response.decode('utf-8'))

pesel = input('')

s.send(pesel.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))


option = input('')

s.send(option.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

amount = input('')

s.send(amount.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

continue_ = input('')

s.send(continue_.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

option = input('')
s.send(option.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

continue_ = input('')

s.send(continue_.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

option = input('')

s.send(option.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

continue_ = input('')

s.send(continue_.encode('utf-8'))

response = s.recv(1024)
print(response.decode('utf-8'))

option = input('')

s.send(option.encode('utf-8'))
 