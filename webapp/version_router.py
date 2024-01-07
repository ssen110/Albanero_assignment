from webapp.web_handlers import user_handler, train_handler, seat_details_handler


class VersionRouterWeb:
    @staticmethod
    def handle_get_user_details():
        return user_handler.UserHandler().get_user_details()

    @staticmethod
    def handle_save_user_details():
        return user_handler.UserHandler().save_user_details()

    @staticmethod
    def handle_save_train_details():
        return train_handler.TrainHandler().save_train_details()

    @staticmethod
    def handle_get_train_detail():
        return train_handler.TrainHandler().get_train_details()

    @staticmethod
    def handle_get_seat_count_details():
        return seat_details_handler.SeatDetailsHandler().get_train_ticket_count_details()

    @staticmethod
    def handle_save_train_ticket_seat():
        return seat_details_handler.SeatDetailsHandler().save_train_ticket_seat()

    @staticmethod
    def handle_cancel_train_ticket():
        return seat_details_handler.SeatDetailsHandler().cancel_train_ticket()

