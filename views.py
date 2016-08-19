from init import app, db
import models, flask

@app.route('/')
def index():
    print("Index working")
    user = models.User()
    user.data = 'will'

    db.session.add(user)
    db.session.commit()

    user = models.User.query.filter_by(id=1).first()
    name = user.data
    return flask.render_template('index.html', name = name)