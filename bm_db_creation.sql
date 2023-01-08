CREATE DATABASE iSpindel;

CREATE USER 'iSpindel'@'localhost' IDENTIFIED BY 'ohyeah';
GRANT ALL PRIVILEGES ON iSpindel . * TO 'iSpindel'@'localhost';
FLUSH PRIVILEGES;