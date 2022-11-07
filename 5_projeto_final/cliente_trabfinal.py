import socket
from datetime import datetime

# Número máximo de bytes que podem ser enviados
# de uma vez só com o UDP
MAX_BYTES = 65535


def client(port):
    # Criando um socket
    # AF_INET: utilizando a pilha de protocolos da Internet
    # SOCK_DGRAM: selecionando o protocolo UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Preparamos os dados da solicitação
    text1 = input("Login: ")
    print('{} conectado com sucesso'.format(text1))
    data = text1.encode('ascii')

    # Enviamos os dados para o endereço do servidor
    # na porta adequada (default = 1060)
    sock.sendto(data, ('127.0.0.1', port))
    # Ficamos aguardando a resposta do servidor
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        # Apresentamos a resposta decodificada na saída padrão
        text = data.decode('ascii')
        print('Jogadores na sala:')
        print('{!r}'.format(text))
        #Loop para demonstração


if __name__ == '__main__':
    # Execução da função com a porta do nosso servidor
    client(1060)