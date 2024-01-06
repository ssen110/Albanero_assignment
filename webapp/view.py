


def attach_views(app):
    @app.route('/', methods=['GET'])
    def index():
        return 'Web App with Python Flask!'