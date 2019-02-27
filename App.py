from flask import Flask,render_template, request, redirect, url_for

# import CRUD Operations 
from catalog-database import Base, Category, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///catalog-database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

## fuction which show categories && items
@app.route('/')
@app.route('/category/<int:category_id/>items')
def showcategory( category_id):
category=session.quary(Category).filter_by(id=category_id).one()
items=session.quary(item).filter_by(category_id=category_id)
#return render_template (category.html,category=category,items=item)
output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.id
        output += '</br>'

# function which show item        

@app.route('/categories/<int:category_id>/items/<int:item_id>')
def showItems(category_id, item_id):
    item = session.query(Item).filter_by(
        category_id=category_id, id=item_id).one()
    ##return render_template('item.html', item=item)
      output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.id
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output


    # functio to add new item 
@app.route('/item/<int:item_id>/add/', methods=['GET', 'POST'])
def Addnewitem( category_id ):
if request.method=='POST':
	newItem=Item(name=request.form['name'],
		description = request.form['description'],
        category_id = request.form['category_id']
    session.add(newItem)
    session.commit()
    return redirect (url_for ('showcategory',category_id=category_id)
  else:
     return render_template('Addnewitem.html',category_id=category_id
     	)

     

@app.route('/category/<int:category_id>/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    deleteitem = session.query(item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(deleteitem)
        session.commit()
        return redirect(url_for('category', category_id=category_id))
    else:
        return render_template('deleteitem.html', item=deleteitem)




@app.route('/category/<int:category_id>/<int:item_id>/edit',
           methods=['GET', 'POST'])
def EditItem():
 edititem=session.quary(item).filter_by(id=item.id).one()
 if request.method=='POST':
     if request.form['name']:
   	     edititem.name=request.form['name']
   	 if request.form['description']:
   	     edititem.name=request.form['description']
   	 if request.form['category_id']:
   	     edititem.name=request.form['category_id']
     session.add(edititem)
     session.commit()
     return redirect(url_for('category_id', 
	restaurant_id=category_id))
else
return render_template(edititem.html,category_id=category_id,
	                     item_id=item_id)





if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)