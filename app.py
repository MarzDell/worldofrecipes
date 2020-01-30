import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import TEXT


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipe_manager'
app.config['MONGO_URI'] = 'mongodb+srv://Cat:Kot@myfirstcluster-tlipu.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

recipes = mongo.db.recipes
the_recipe = mongo.db.recipes
categories = mongo.db.categories

mongo.db.recipes.create_index([('$**', 'text')])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/view_recipe')
def view_recipe():
    records = list(mongo.db.recipes.find())
    return render_template('view.html', recipes=records)
  
@app.route('/add_recipe')
def add_recipe():
    return render_template('insert.html',
                           categories=mongo.db.categories.find())

@app.route('/insert', methods=['POST'])
def insert():
    recipes = mongo.db.recipes
    payload = request.form.to_dict()
    payload.update({'views': 0})
    recipes.insert_one(payload)
    return redirect(url_for('view_recipe'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    title = request.form.get('search')
    find = {'$text': {'$search':title}}
    results = mongo.db.recipes.find(find)
    return render_template('view.html', recipes=results, count=results.count())

@app.route('/stat')
def stat():
    return render_template('statistic.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)