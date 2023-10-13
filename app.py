from flask import Flask, render_template
import random

random_number = random.randint(1, 6)
print(random_number)

app = Flask(__name__)

@app.route('/')
def random_number():
    # Генеруємо випадкове число від 1 до 6
    random_number = random.randint(1, 6)
    
    # Передаємо випадкове число у HTML-шаблон
    return render_template('index.html', random_number=random_num)
if __name__ == '__main__':
    app.run(debug=True)