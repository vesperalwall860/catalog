from flask import render_template, url_for, flash, redirect
from . import main
from .. import models, db


@main.route('/')
def index():
    products = models.Product.query\
                    .filter(models.Product.price > 0)\
                    .order_by(models.Product.price.asc()).all()

    return render_template('index.html', products=products)


@main.route('/product/<int:product_id>')
def product(product_id):
    product = models.Product.query.get(product_id)

    return render_template('product.html', product=product)


@main.route('/sort-by-price/<sort_type>')
def sort_by_price(sort_type):
    if sort_type == 'desc':
        products = models.Product.query.order_by(
                        models.Product.price.desc()).all()
    else:
        products = models.Product.query.order_by(
                        models.Product.price.asc()).all()

    return render_template('catalog.html', products=products)

