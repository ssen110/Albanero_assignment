from webapp.web_handlers import user_handler

class VersionRouterWeb:
    @staticmethod
    def handle_get_user_details():
        return user_handler.UserHandler().get_user_details()

    @staticmethod
    def handle_save_user_details():
        return user_handler.UserHandler().save_user_details()

