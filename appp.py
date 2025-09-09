from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список товаров (имитация базы данных)
products = [
    {'id': 1, 'name': 'Shelly', 'price': 50},
    {'id': 2, 'name': 'Leon', 'price': 1000},
    {'id': 3, 'name': 'Colt', 'price': 100}
]

# Корзина (хранится в памяти)
cart = []

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('home'))

@app.route('/cart')
def show_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        cart.clear()
        return render_template('buy.html', name=name)
    return redirect(url_for('show_cart'))

@app.route('/remove/<int:product_id>')
def remove_from_cart(product_id):
    for i, item in enumerate(cart):
        if item['id'] == product_id:
            del cart[i]
            break
    return redirect(url_for('show_cart'))


if __name__ == '__main__':
    app.run(debug=True)
