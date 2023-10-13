from flask import Flask, request

app = Flask(__name__)

# Створюємо маршрут для стартової сторінки
@app.route('/')
def index():
    # Отримуємо IP-адресу користувача з запиту
    user_ip = request.remote_addr
    return f'Ваша IP-адреса: {user_ip}'

if __name__ == '__main__':
    app.run()
