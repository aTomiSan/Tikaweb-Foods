CREATE TABLE foods (id SERIAL PRIMARY KEY, name TEXT, amount INT, visible INT, stored INT); 
CREATE TABLE groceries (id SERIAL PRIMARY KEY, name TEXT, amount INT, type INT, visible INT); 
CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, ingredients TEXT, additional TEXT);
CREATE TABLE expenses (id SERIAL PRIMARY KEY, time TIMESTAMP, value INT); 
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);

INSERT INTO foods (name, amount, visible, stored) VALUES ('Wokkivihannekset', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Tofu', 1, 1, 0); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Riisi', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Kookoskerma', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Currytahna', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Peruna', 10, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Voi', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Kasvisliemikuutio', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Jauheliha', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Kananmuna', 6, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Vehnäjauhoja', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Pinaatti', 1, 1, 0); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Feta', 1, 1, 0); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Tomaatti', 1, 1, 1); 
INSERT INTO foods (name, amount, visible, stored) VALUES ('Sipuli', 1, 1, 1);

INSERT INTO recipes (name, ingredients, additional) VALUES ('Kasviswokki', 'Wokkivihannekset Tofu Riisi Kookoskerma Currytahna', 'Ruskista, lisää kerma ja currytahna. Keitä riisi.'); 
INSERT INTO recipes (name, ingredients, additional) VALUES ('Perunamuusi', 'Peruna Voi Kasviliemikuutio', 'Keitä perunat, muussaa, lisää voi ja kasviliemi.'); 
INSERT INTO recipes (name, ingredients, additional) VALUES ('Jauhelihapivit', 'Jauheliha Kananmuna vehnäjauho', 'Sekoita ainekset, muotoile pihvit ja paista.'); 
INSERT INTO recipes (name, ingredients, additional) VALUES ('Feta-pinaatti-munakas', 'Feta Pinaatti Kananmuna Tomaatti Sipuli', 'Kuullota sipuli ja tomaatti, lisää pinaatti ja feta murskattuna. Lisää munat sekoitettuna ja kyspytä kannen alla miedolla lämmöllä');

