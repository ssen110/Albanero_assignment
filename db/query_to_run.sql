CREATE DATABASE albanero;

use albanero;

create TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
    email_id varchar(200),
    user_name varchar(200),
    date_created datetime,
    date_updated datetime default current_timestamp
);

create table trains(
	id int AUTO_INCREMENT PRIMARY key,
    train_name varchar(200),
    starting_place varchar(200),
    ending_place varchar(200),
    max_capacity int,
    depurture_time datetime,
    reaching_time datetime
);

create table bookings(
	id int AUTO_INCREMENT primary key,
    user_id int,
    train_id int,
    is_completed bool,
    soft_deleted bool,
    booking_time_created datetime,
    booking_time_updated datetime,
    soft_deleted_time_updated datetime,
    constraint bookings_ibfk_1 foreign key(user_id) references users(id) on delete cascade,
    constraint bookings_ibfk_2 foreign key(train_id) references trains(id) on delete cascade,
    INDEX(user_id),
    INDEX(train_id)
);
