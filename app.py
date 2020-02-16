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
    
@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/view_recipe')
def view_recipe():
    records = list(mongo.db.recipes.find())
    return render_template('view.html', recipes=records)

@app.route('/view_specific/<recipe_id>', methods=['GET', 'POST'])
def view_specific(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                            {'$inc': {'views': 1}})
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('individual_recipe.html',
                            recipe=the_recipe, categories=all_categories)
 
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
    
    
@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    the_recipe = mongo.db.recipes.find_one
    ({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update/<recipe_id>', methods=['POST'])
def update(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)}, {
        "img": request.form.get('img'),
        "categories": request.form.get('categories'),
        "title": request.form.get('title'),
        "ingredients": request.form.get('ingredients'),
        "method": request.form.get('method'),
        "nutrition": request.form.get('nutrition'),
        "time": request.form.get('time'),
        "author": request.form.get('author'),
    })
    return redirect( url_for('view_recipe'))
    
    
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
    mongo.db.recipes.delete_one({ "_id":ObjectId(recipe_id)})
    return redirect( url_for('view_recipe'))
    
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    title = request.form.get('search')
    find = {'$text': {'$search':title}}
    results = mongo.db.recipes.find(find)
    return render_template('view.html', recipes=results, count=results.count())

@app.route('/count/<recipe_id>', methods=['GET', 'POST'])
def count():
    count = mongo.db.recipes.find({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                            {'$inc':{'view': 1}})
    return render_template('view.html', recipe=count)

@app.route('/stat')
def stat():
    return render_template('statistic.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=False)