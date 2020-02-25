import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8817))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Forbindelse fra {address} er blevet oprettet!")
    clientsocket.send(bytes("Velkommen til serveren!", "utf-8"))
    clientsocket.close()