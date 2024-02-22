from flask import Flask, render_template


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


if __name__ == '__main__':
    app.run(debug=True)
