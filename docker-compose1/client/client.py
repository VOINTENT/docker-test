import socket, time, sys

if __name__ == '__main__':
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('talkto', 2000))
        s.send(b'Hello, world!\n')
        data = s.recv(1024)
        print('Received:', data)
        sys.stdout.flush()
        s.close()
        time.sleep(5)
