import os
import socket
import threading

WEBROOT = "webroot"


def handle_client(c, add):
    print(add, "connected.")

    with c:
        request = c.recv(1024)

        # 解析HTTP请求头
        headers = request.split(b"\r\n")
        file = headers[0].split()[1].decode()

        # Load the file content
        if file == "/":
            file = "index.html"

        try:
            with open(WEBROOT + file, "rb") as f:
                content = f.read()
            response = b"HTTP/1.0 200 OK\r\n\r\n" + content

        except FileNotFoundError:
            response = b"HTTP/1.0 404 NOT FOUND\r\n\r\nFile not found!"

        # Send http response
        c.sendall(response)


if __name__ == '__main__':

    # Change working directory to script folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # 监听任意地址的80端口
        server.bind(("0.0.0.0", 80))
        server.listen()

        while True:
            client, addr = server.accept()  # 接收来自客户端的连接
            t = threading.Thread(target=handle_client, args=(client, addr))
            t.start()
