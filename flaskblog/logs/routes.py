from flask import (render_template, abort, Blueprint)
from flask_login import current_user, login_required

from flaskblog import logger_db

logs = Blueprint('logs', __name__)


@logs.route('/logs', methods=['GET'])
@login_required
def get_logs():
    if not current_user.has_roles('admin'):
        abort(403)
    couch_logs = [doc['doc'] for doc in logger_db.view('_all_docs', include_docs=True)]

    log_entries = [{'date': doc['date'], 'logs': doc['logs']} for doc in couch_logs]
    log_entries = sorted(log_entries, key=lambda entry: entry['date'], reverse=True)

    return render_template('logs.html', log_entries=log_entries)
