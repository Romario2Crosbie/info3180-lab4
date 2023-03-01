from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms import FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    file = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Only JPEG and PNG images are allowed!')
    ])