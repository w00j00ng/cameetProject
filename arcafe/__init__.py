from flask import Flask
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from .views import main_views, nagbot_views, kakao_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(nagbot_views.bp)
    app.register_blueprint(kakao_views.bp)

    return app
