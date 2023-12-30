import os

from flask import Flask, make_response, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from lib import gpt, crud, forms
from lib.database import with_db

HOST = '0.0.0.0'
PORT = int(os.getenv('SERVICE_PORT', default='8081'))

app = Flask(__name__)
app.secret_key = "app_secret"
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@with_db
@login_manager.user_loader
def load_user(user_id, db):
    user_repository = crud.UserRepository(db)

    return user_repository.get_one(user_id)


@app.route('/hello', methods=['GET'])
def hello():
    return make_response('gptNotes alive!', 200)


@with_db
@app.route('/login/', methods=['POST', 'GET'])
def login(db):
    if current_user.is_authenticated:
        return redirect(url_for('/'))

    template_context = {}
    form = forms.LoginForm()
    template_context['form'] = form

    if form.validate_on_submit():
        user_repository = crud.UserRepository(db)
        user = user_repository.get_one(form.username.data, id_field='username')
        if user and user_repository.check_password(form.username.data, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('/'))

        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))

    return render_template('login.html', **template_context)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")

    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    template_context = {'current_user': current_user}

    return render_template('index.html', **template_context)


@app.route('/gpt/<gpt_action>', methods=['GET'])
@login_required
def gpt_answer(gpt_action: str):
    '''
    get answer from gpt (by action)
    '''

    text = request.args.get('text')
    if not text:
        return make_response('please provide the text', 404)

    if gpt_action == 'improve':
        return make_response(gpt.gpt_improve(text), 200)
    elif gpt_action == 'append':
        return make_response(gpt.gpt_append(text), 200)
    elif gpt_action == 'retell':
        return make_response(gpt.gpt_retell(text), 200)

    return make_response('unknown action', 404)


def main():
    app.run(host=HOST, port=PORT, debug=True)


if __name__ == '__main__':
    main()
