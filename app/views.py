from app import app
from flask import render_template
from forms import SignUpForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', method=['GET', 'POST'])
def index():
  form = SignUpForm()
  return render_template('index.html',
      form = form,
      providers = app.config['OPENID_PROVIDERS'])
