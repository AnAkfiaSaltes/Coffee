from flask import Flask, render_template, request
import os

app = Flask(__name__)

selected_item = None
prices = {
    "your_image1.jpg": 10,
    "your_image2.jpg": 20,
    "your_image3.jpg": 30,
    "your_image4.jpg": 40,
    "your_image5.jpg": 50,
    "your_image6.jpg": 60
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/select_item', methods=['POST'])
def select_item():
    global selected_item
    item_index = int(request.form['item_index'])
    if item_index == 7:
        return selected_item
    else:
        selected_item = request.form['item_price']
        return "Item price added to folder."


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')