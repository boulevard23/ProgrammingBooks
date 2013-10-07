from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class SignUpForm(Form):
  openid = TextField('openid', validators=[Required()])
