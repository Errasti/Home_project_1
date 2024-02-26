from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/category/')
def category_type():
    types = {'type': ['Обувь', 'Детская одежда', 'Мужская одежда', 'Женская одежда']}
    return render_template('category.html', **types)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/kids/')
def kids():
    return render_template('kids.html')


@app.route('/man/')
def man():
    return render_template('man.html')


@app.route('/woman/')
def woman():
    return render_template('woman.html')


@app.post('/feedback/')
def feedback_post():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response()
    response.set_cookie('name', name)
    response.set_cookie('email', email)
    return redirect(url_for('hello'))


@app.route('/hello/')
def hello():
    context = {
        'name': request.cookies.get('name'),
        'email': request.cookies.get('email'),
    }
    return render_template('hello.html', **context)


@app.get('/feedback/')
def feedback_get():
    return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug=True)
