# game_number: Number of the game
# winner_line: Name of person who won line
# winner_house: Name of persone who won house
# line_no_balls: How many balls to call a line
# house_number_balls: How many balls to call full house
# winning_ticket_line: The numbers that make up the Line that won
# winning_ticket_house: The numbers that make up the House that won
# Created at: Time stamp when entry was added to database

CREATE TABLE games (
game_number INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
winner_line varchar(20),
winner_house varchar(20),
line_no_balls TINYINT,
house_number_balls TINYINT,
winning_ticket_line varchar(26),
winning_ticket_house varchar(100),
created_at varchar(10)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Table balls
# ball: The ball number
# times_called: The frequency of this ball being used.

CREATE TABLE stats (
ball INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
times_called INT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO games (position, offender, wiki, crime, punishment, image, created_at)
VALUES (1,"Test User 1","Test User 2",12,34,"3,0,0,34,0,56,63,0,90","1,11,0,0,0,0,66,73,84,0,12,24,32,40,53,0,0,85,9,0,28,34,0,0,69,0,80","07-01-2021")

INSERT INTO stats (ball, times_called)
VALUES (3,1),(34,1),(66,1),(73,1),(84,1),(1,1),(11,1),(12,1),(24,1),(32,1),(40,1),(53,1),(85,1),(9,1),(28,1),(34,1),(69,1),(80,1)
