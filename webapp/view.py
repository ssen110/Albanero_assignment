from flask import request
from webapp import version_router

def attach_views(app):
    @app.route('/', methods=['GET'])
    def index():
        return 'Web App with Python Flask!'

    @app.route("/userdetails", methods = ["GET"])
    def user_details():
        return version_router.VersionRouterWeb.handle_get_user_details()

