# from flask import Flask, url_for, request
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# @app.route('/form_sample', methods=['POST', 'GET'])
# def form_sample():
#     if request.method == 'GET':
#         return f'''<!doctype html>
#                         <html lang="en">
#                           <head>
#                             <meta charset="utf-8">
#                             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                             <link rel="stylesheet"
#                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                             crossorigin="anonymous">
#                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
#                             <title>CoffeShop</title>
#                           </head>
#                           <body>
#                             <h2 align="center" style="color:Black">Регистрация на сайт</h2>
#                             <div>
#                                 <form class="login_form" method="post">
#                                     <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
#                                     <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
#                                         <label for="about">ФИО</label>
#                                         <textarea class="form-control" id="about" rows="3" name="about"></textarea>
#                                     </div>
#                                         <label for="form-check">Укажите пол</label>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
#                                           <label class="form-check-label" for="male">
#                                             Мужской
#                                           </label>
#                                         </div>
#                                         <div class="form-check">
#                                           <input class="form-check-input" type="radio" name="sex" id="female" value="female">
#                                           <label class="form-check-label" for="female">
#                                             Женский
#                                           </label>
#                                         </div>
#                                     </div>
#                                     <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
#                                 </form>
#                             </div>
#                           </body>
#                         </html>'''
#     elif request.method == 'POST':
#         print(request.form['email'])
#         print(request.form['password'])
#         print(request.form['class'])
#         print(request.form['file'])
#         print(request.form['about'])
#         print(request.form['accept'])
#         print(request.form['sex'])
#         return "Форма отправлена"
#
#
# if __name__ == '__main__':
#     app.run(port=8080, host='127.0.0.1')


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_product_price(product_name):
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
    return render_template('postgit add .html')


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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# fggh