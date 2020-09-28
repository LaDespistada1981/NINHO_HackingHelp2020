from flask_wtf import FlaskForm
from wtforms import SubmitField,BooleanField,IntegerField,StringField,TextAreaField,PasswordField
from wtforms.validators import DataRequired
from flask_wtf import Form
class SolicitacaoForm(Form):
  nome = StringField('Nome', validators=[DataRequired()]);
  sobrenome = StringField('Sobrenome',validators=[DataRequired()]);
  cpf = StringField('cpf');
  rg = StringField('rg');
  numFilhos = IntegerField('numFilhos');
  deficiencia = StringField('deficiencia',validators=[DataRequired()]);
  telefone = StringField('telefone',validators=[DataRequired()]);
  bairro = StringField('bairro',validators=[DataRequired()]);
  municipio = StringField('municipio',validators=[DataRequired()]);
  cep = StringField('cep',validators=[DataRequired()]);
  obs = TextAreaField('obs')
  submit = SubmitField('Solicitar')