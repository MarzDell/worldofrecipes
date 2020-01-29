import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipe_manager'
app.config['MONGO_uri'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)