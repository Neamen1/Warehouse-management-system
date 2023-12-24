from flask import (render_template, Blueprint)
from flask_login import current_user, login_required

from flaskblog.models import Notification

notifications = Blueprint('notifications', __name__)


@notifications.route('/notifications')
@login_required
def get_notifications():
    user_id = current_user.id

    user_notifications = Notification.query.filter_by(userId=user_id).order_by(Notification.timestamp.desc()).all()

    return render_template('layout.html', notifications=user_notifications)
