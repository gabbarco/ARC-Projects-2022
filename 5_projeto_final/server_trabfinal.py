import socket

# Número máximo de bytes que podem ser enviados
# de uma vez só com o UDP
MAX_BYTES = 65535

def server(port):
    # Criando o socket
    # AF_INET: utilizando a pilha de protocolos da Internet
    # SOCK_DGRAM: selecionando o protocolo UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ligando o socket ao endereço de localhost
    # e à porta indicada pelo usuário (default = 1060)
    sock.bind(('127.0.0.1', port))

    # getsockname retorna o nome do socket
    print('Listening at {}'.format(sock.getsockname()))
    print ('Número de jogadores na sala: 0/3')
    print( 'Aguardando jogadores...')
    text2=""
    i=0

    while True:
        # A função recvfrom fica aguardando a chegada
        # da socilitação do cliente
        # Além dos dados enviados pelo cliente, também
        # conseguimos acessar o endereço IP do cliente
        data, address = sock.recvfrom(MAX_BYTES)

        # Decodificamos os dados para ascii e apresentamos
        # na sáida padrão
        text1 = data.decode('ascii')
        print('{!r} conectado com sucesso'.format(text1))

        # Enviamos uma resposta à solicitação do cliente
        print("Jogadores na sala: ")
        text = '{}    ({})    {}'.format(text1, address,text2)
        text2= "{}".format(text)
        print(text)
        data = text.encode('ascii')
        sock.sendto(data, address)
        i=i+1
        if (i==1):
            print("Aguardando 2 jogadores!!")
        if (i==2):
            print("Aguardando 1 jogador!!")
        if (i==3):
            print("Sala completa!!")


if __name__ == '__main__':
    # Execução da função com a porta do nosso servidor
    server(1060)