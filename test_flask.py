from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATE_FOLDER'] = 'templates'


@app.route('/', methods=('GET',))
def index():
    return 'INDEX page'.encode('utf-8')


@app.route('/example', methods=('GET', 'POST'))
def example_with_template():
    got = request.args.get('user', "None")
    return render_template('example.html', variable=got)


app.run(host='127.0.0.1', port=8080)

