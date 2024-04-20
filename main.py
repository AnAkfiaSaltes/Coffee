from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Получаем данные из запроса
    image_url = request.form['image_url']
    product_name = request.form['product_name']
    # Добавляем логику для добавления товара в корзину
    # Здесь может быть ваша логика для работы с корзиной, например, добавление товара в базу данных
    return f'The product {product_name} with image {image_url} has been added to the cart!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')