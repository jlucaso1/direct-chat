import socket

IP = '::'
PORT = 7777

# Configurar socket para ouvir requisições no protocolo UDP e IPv6
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# Associa o socket ao endereço IP e porta especificados e escuta conexões
sock.bind((IP, PORT))
print('Servidor rodando...')

while True:
    # Recebe uma mensagem do cliente
    msg, sender = sock.recvfrom(1024)
    # Imprime o endereço IP, porta do cliente e os dados decodificados em utf-8
    print('Mensagem recebida de', sender, '| Dados:', msg.decode('utf-8'))

# Fecha o socket
sock.close()
print('Servidor encerrado.')
