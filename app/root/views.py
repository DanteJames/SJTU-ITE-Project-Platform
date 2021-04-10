from flask import render_template
from . import root_blueprint


@root_blueprint.route('/')
def index():
    routes = ['root.index', 'user.register', 'user.login']
    return render_template('index.html', routes=routes)
