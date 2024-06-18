import socket


HOST = "192.168.0.7"
PORT = 9999

print(">>Server Start")
# 서버 소켓 생성 : ip주소 버전, TCP or UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 옵션 설정 : already in use 에러 해결하여 방금 사용하고
"""소켓 서버가 종료되었다가 다시 시작될 때 이미 사용 중인 포트를 즉시 다시 사용할 수 있도록 하는 
옵션을 설정, 이를 통해 서버를 빠르게 재시작할 수 있으며, 
이전에 사용된 포트를 다른 프로세스가 차지하고 있는 경우에도 소켓을 바로 재사용할 수 있음"""
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

# 서버가 계속 대기
while True:
    print("waiting for a connection")
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)
    client_socket.send(bytes("connect", "utf-8"))
    while True:
        msg = input("클라이언트에게 보낼 메시지:")
        client_socket.send(msg.encode())
        if msg == "bye":
            break
    client_socket.close()

# 1회 접속 후 종료
print("waiting for a connection")
client_socket, addr = server_socket.accept()
print("Connection from", addr)
client_socket.send(bytes("connect", "utf-8"))
while True:
    msg = input("클라이언트에게 보낼 메시지:")
    client_socket.send(msg.encode())
    if msg == "bye":
        break
client_socket.close()
