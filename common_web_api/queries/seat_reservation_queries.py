class SeatReservationQueries:
    get_train_seat_booking = " select count(*) from  bookings where train_id =:train_id and is_completed = 1"

    insert_into_seat_details = " insert into bookings(user_id, train_id, is_completed, booking_time_created, booking_time_updated) " \
                               " values(:user_id, :train_id, :is_confirmed, current_timestamp, current_timestamp) "

    cancel_train_ticket = " update  bookings set soft_deleted = 1, soft_deleted_time_updated = current_timestamp, booking_time_updated = current_timestamp" \
                          " where id = :booking_id "

    upgrade_train_ticket = " UPDATE bookings SET is_completed = 1" \
                           " WHERE train_id = :train_id and id = (SELECT subquery.min_id FROM (SELECT MIN(id) AS min_id FROM bookings WHERE train_id = :train_id and is_completed = 0 AND " \
                           " (soft_deleted IS NULL OR soft_deleted = 0)) AS subquery) "