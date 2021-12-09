import socket

IP = '::1'
PORT = 7777

# Cria um socket UDP/IPv6
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
dest = (IP, PORT)

# Envia evento de conexão
sock.sendto('Conectou'.encode('utf-8'), dest)
print('Aperte CTRL-C para encerrar o programa')
while True:
    try:
        # Recebe uma mensagem do teclado
        msg = input()
        print('Enviando mensagem: ', msg)
        # Envia a mensagem para o servidor codificada em UTF-8
        sock.sendto(msg.encode('utf-8'), dest)
    except KeyboardInterrupt:
        break
    except:
        break
# Envia evento de desconexão
sock.sendto('Desconectou'.encode('utf-8'), dest)
# Fecha o socket
sock.close()
print('Conexão finalizada')
