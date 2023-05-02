drop TABLE IF EXISTS answers;
DROP TABLE IF EXISTS users_quizzes;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS users;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    score INT
);

CREATE TABLE quizzes(
    id SERIAL PRIMARY KEY,
    quiz VARCHAR(255),
    opt1 VARCHAR(255),
    opt2 VARCHAR(255),
    opt3 VARCHAR(255),
    correct_answer VARCHAR(255),
    level INT,
    user_id INT NOT NULL REFERENCES users(id)
);

CREATE TABLE answers(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    quiz_id INT NOT NULL REFERENCES quizzes(id),
    correct BOOLEAN
);


CREATE TABLE users_quizzes(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    quiz_id INT NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE
);


INSERT INTO users(name) VALUES ('Greg');
INSERT INTO users(name) VALUES ('Ali');
INSERT INTO users(name) VALUES ('Ken');

INSERT INTO quizzes (quiz,opt1,opt2,correct_answer,level,user_id) VALUES(
    'who is the king?','greg','zhu','greg',1,1);


INSERT INTO quizzes (quiz,opt1,opt2,correct_answer,level,user_id) VALUES(
    'who is red?','ken','zhu','zhu',1,1);


INSERT INTO answers(user_id,quiz_id,correct) VALUES(1,1,True);
INSERT INTO answers(user_id,quiz_id,correct) VALUES(1,2,True);
