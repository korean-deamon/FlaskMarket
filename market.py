from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# @app.route('/about/<username>')
# def about_page(username):
#     return f'Hi this page about {username}'


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '123456789012', 'price': 1000},
        {'id': 2, 'name': 'Laptop', 'barcode': '987654321098', 'price': 2000},
        {'id': 3, 'name': 'Headphones', 'barcode': '456789012345', 'price': 150},
        {'id': 4, 'name': 'Smartwatch', 'barcode': '654321098765', 'price': 300},
    ]
    return render_template('market.html', items=items)