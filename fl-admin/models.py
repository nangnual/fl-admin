from flask import Flask
from .extensions.py import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String)
	password = db.Column(db.String, nullable=False)
	products = db.relationship('Product', backref='product', lazy=True)

	def __repr__(self):
		return self.name

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	supplier = db.Column(db.Integer, db.foreign_key('user.id'), nullable=False)

	def __repr__(self):
		return '{} by {}'.format(self.name, self.supplier)
