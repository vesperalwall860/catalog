from flask import render_template, url_for, flash, redirect
from . import main
from .. import models, db


@main.route('/')
def index():
    products = models.Product.query.all()

    return render_template('index.html', products=products)


