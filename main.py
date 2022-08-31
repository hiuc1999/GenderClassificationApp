from flask import Flask
from app import views

app = Flask(__name__) # webserver gateway interphase (WSGI)

#homepage
app.add_url_rule(rule='/',endpoint='home',view_func=views.index)
# introduction
app.add_url_rule(rule='/details/',endpoint='details',view_func=views.details)
# app page
app.add_url_rule(rule='/app/',
                 endpoint='app',
                 view_func=views.app,
                 methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)