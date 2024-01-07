from webapp import version_router

def attach_views(app):
    @app.route('/', methods=['GET'])
    def index():
        return 'Web App with Python Flask!'

    @app.route("/userdetails", methods = ["GET"])
    def user_details():
        return version_router.VersionRouterWeb.handle_get_user_details()

    @app.route("/adduser", methods = ["POST"])
    def save_user_details():
        return version_router.VersionRouterWeb.handle_save_user_details()

    @app.route("/traindetails", methods = ["GET"])
    def get_train_detail():
        return version_router.VersionRouterWeb.handle_get_train_detail()

    @app.route("/addtrain", methods = ["POST"])
    def save_train_details():
        return version_router.VersionRouterWeb.handle_save_train_details()

    @app.route("/trainseatcount", methods = ["GET"])
    def get_seat_count_details():
        return version_router.VersionRouterWeb.handle_get_seat_count_details()

    @app.route("/booktickets", method = ["POST"])
    def save_train_ticket_seat():
        return  version_router.VersionRouterWeb.handle_save_train_ticket_seat()

    @app.route("/canceltickets", methods = ["POST"])
    def cancel_train_ticket():
        return version_router.VersionRouterWeb.handle_cancel_train_ticket()


