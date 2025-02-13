import http.server
import socketserver

PORT = 8000  # Выберите любой свободный порт, например, 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Сервер запущен на порту:", PORT)
    httpd.serve_forever()
