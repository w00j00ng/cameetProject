from flask import Blueprint, render_template
from flask import session, g
from arcafe.models import User_02
from arcafe import db


bp = Blueprint('mydata', __name__, url_prefix='/mydata/')


@bp.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User_02.query.get(user_id)


@bp.route('/')
def mydata():
    query_mydata = db.engine.execute(f'SELECT * FROM usage_02 WHERE username = "{g.user.username}" ORDER BY id')
    all_rows = [row for row in query_mydata]
    print(all_rows)
    return render_template('mydata/index.html', result=all_rows)
