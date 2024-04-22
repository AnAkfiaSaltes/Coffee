from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_product_price(product_name):
    # n_id = 1
    conn = sqlite3.connect('trains0.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM кофе WHERE productName = ?", (product_name,))
    price = cursor.fetchone()
    conn.close()
    if price:
        return price[0]
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form['product_name']
    price = get_product_price(product_name)
    if price:
        addToCart(product_name, price)
        return 'Product added to cart!'
    else:
        return 'Product not found!'


cartItems = []


def addToCart(productName, price):
    cartItems.append({'name': productName, 'price': price})


@app.route('/save_bank_info', methods=['POST'])
def save_bank_info():
    card_number = request.form['card_number']
    pin_code = request.form['pin_code']

    with open('bank info.db', 'a') as file:
        file.write(f"Card Number: {card_number}, PIN Code: {pin_code}\n")

    return 'Bank info saved successfully!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')