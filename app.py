from flask import Flask
from flask import render_template
from flask_scss import Scss
from flaskext.markdown import Markdown
import mistune

app = Flask(__name__)
Scss(app)
Markdown(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/2')
def index2():
    # data = open('_posts/2017-02-01-markdown-examples.md').read()
    # data = mistune.markdown(data)
    data = ''
    return render_template('home2.html', content=data)


app.run(host='127.0.0.1', port= 81, debug=True)
