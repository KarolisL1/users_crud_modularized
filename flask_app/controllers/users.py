# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import Users


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = Users.get_all()
    print(users)
    return render_template("index.html", users=users)
            
@app.route("/users/new")
def new():
    return render_template("new_user.html")

@app.route("/users/edit/<int:user_id>")
def edit(user_id):
    data = {'user_id': user_id}
    user = Users.get_one_user(data)
    return render_template("edit.html", user=user)

@app.route("/users/update/<int:user_id>", methods=["POST"])
def update(user_id):
    data = {
        'user_id': user_id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    Users.update(data)

    return redirect(f"/users/{user_id}")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.

    # We pass the data dictionary into the save method from the Friend class.
    Users.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/users/<int:user_id>')
def single_user(user_id):
    data = {'user_id': user_id}
    user = Users.get_one_user(data)
    return render_template('single_user.html', user=user)

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    data = {'user_id': user_id}
    Users.delete(data)
    return redirect('/')