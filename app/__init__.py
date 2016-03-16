from flask import Flask

app = Flask(__name__)
app.secret_key = 'dsfsdfds.dfdsfdsf.dsfsdf.45.dsfdsf.dfs!'

from app import views