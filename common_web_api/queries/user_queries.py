class UserQueries:
    insert_into_user_details = " insert into users(email_id, user_name, date_created, date_updated)" \
                               " values (:email_id, :name, current_timestamp, current_timestamp) "

    get_user_details = " select  id, email_id, user_name from users where id = :user_id "
