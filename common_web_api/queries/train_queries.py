class TrainQueries:
    get_train_details = " select id, train_name, starting_place, ending_place, depurture_time, reaching_time, max_capacity from trains where id :train_id  "

    insert_into_user_details = " insert into trains(train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time)" \
                               " values (:train_name, :starting_place, :ending_place, :max_capacity, :depurture_time, :reaching_time ) "
