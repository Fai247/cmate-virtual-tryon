from flask import Flask


def create_app():
    # initiate flask instance
    app = Flask(__name__)

    # Set the secret key to some random bytes. Keep this really secret!
    app.config['SECRET_KEY'] = b'xanjay_secrect'
    app.config['UPLOAD_FOLDER'] = 'user_uploads'
    # existing code omitted

    # from controller import run_cmate
    # app.register_blueprint(run_cmate.bp)

    return app
