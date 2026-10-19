import socket
import re
from http import HTTPStatus


def parse_request(data):
    text = data.decode('utf-8', errors='replace')
    head = text.split('\r\n\r\n', 1)[0]
    lines = head.split('\r\n')
    request_line = lines[0] if lines else ''
    headers = lines[1:] if len(lines) > 1 else []
    return request_line, headers


def get_status_from_path(path):
    match = re.search(r'[?&]status=(\d{3})', path)
    if match:
        code = int(match.group(1))
        try:
            return HTTPStatus(code)
        except ValueError:
            pass
    return HTTPStatus.OK


def build_response(request_line, headers, client_address):
    parts = request_line.split(' ')
    method = parts[0] if parts else 'GET'
    path = parts[1] if len(parts) > 1 else '/'
    status = get_status_from_path(path)
    body_lines = [
        f"Request Method: {method}",
        f"Request Source: {client_address}",
        f"Response Status: {status.value} {status.phrase}"]
    body_lines.extend(headers)
    body = '\r\n'.join(body_lines) + '\r\n'
    body_bytes = body.encode('utf-8')
    response_headers = [
        f"HTTP/1.1 {status.value} {status.phrase}",
        "Content-Type: text/plain; charset=utf-8",
        f"Content-Length: {len(body_bytes)}",
        "Connection: close",
        ""]
    return ('\r\n'.join(response_headers) + '\r\n').encode('utf-8') + body_bytes


def main():
    HOST = '127.0.0.1'
    PORT = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущен на http://{HOST}:{PORT}")
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Подключение от {client_address}")
            with client_socket:
                data = client_socket.recv(4096)
                if data:
                    request_line, headers = parse_request(data)
                    print("--- Запрос ---")
                    print(request_line)
                    for h in headers:
                        print(h)
                    response = build_response(request_line, headers, client_address)
                    client_socket.sendall(response)
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
