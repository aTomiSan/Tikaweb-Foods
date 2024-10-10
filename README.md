OSTOSTEN HALLINTA SOVELLUS

Sovelluksen tarkoitus on hallita kotona olevia ruokia, suunnitella tulevia ruokia ja luoda kauppalista niiden perusteella, ja siten helpottaa arjen ruokaostosten tekemistä. Sen avulla voi myös seurata ruokiin kuluvia menoja. 

Applikaatiossa on viisi sivua: Etusivu, Ostoslista, Ruoat, Reseptit ja Kulut. 

ETUSIVU-sivulla kirjaudutaan sisään applikaatioon tai luodaan tunnus. Users-tietokanta pitää yllä tietoa sovelluksen käyttäjistä. 

OSTOSLISTA-sivu listaa kauppalistan, johon on lisätty kahdelta muulta ruoat- ja reseptit-sivuilta ruoka-ainekset, joita tulee ostaa kaupasta. Ainesten järjestystä on mahdollista muuttaa, jotta se vastaa tavaroiden sijaintia kun kuljetaan kaupan läpi. Koko kauppalistan voi kerralla siirtää varastossa olevaksi, ja myös tyhjentää. 
Groceries-tietokanta pitää yllä tietoa ostoslistasta. Ostoksen lisääminen tietokantaan vaatii ruoan nimen, määrän, tyypin (järjestystä varten,  Lisäksi tietokannassa on ruuan näkyvyys, eli näkyykö kyseinen ruoka käyttäjälle.

RUOAT-sivu listaa kaikki ruoka-ainekset, joita kotona yleensä käytetään. Sivu näyttää ensimmäisenä ne ruuat, joita on jo kotona, ja sen jälkeen ne, joita ei ole. Tällä sivulla niitä voi lisätä ja poistaa sekä lisätä kauppalistaan. Varastossa-otsikon alla on ruoat, joita on kotona varastossa, ja Loppuneet ruoat otsikon alla ne, jotka on loppu. Poistettaessa ruoka-aines merkitään näkymättömäksi vaikka se ei poistu tietokannasta.
Foods-tietokanta pitää yllä tietoa ruoista. Ruoan lisääminen tietokantaan vaatii ruoan nimen, määrän, ja tiedon onko sitä varastossa. Lisäksi tietokannassa on sen näkyvyys (oletuksena 1).

RESEPTIT-sivu listaa reseptit ja niiden ainesosat. Tällä sivulla reseptejä voi lisätä ja poistaa sekä lisätä ainesosat kauppalistaan. Jos jokin reseptin ruoka-aine ei ole foods-tietokannassa, niin se lisätään ensin sinne automaattisesti. Lisääminen tietokantaan vaatii reseptin nimen, listan pakollisista ainesosista ja listan valinnaisista ainesosista. 
Reseptejä voi myös muokata. 
Recipes-tietokanta pitää yllä tietoa resepteistä. Reseptin tiedot tietokannassa on sen nimi, ainesosat ja lisätiedot. 

KULUT-sivulle kirjataan kulut, joita on mennyt kaupassa käyntiin. Expenses-tietokannassa on tiedot kulutetusta rahasta ja ajankohdasta, joka merkitään automaattisesti kirjauksen tekohetkellä. 


OHJEET SOVELLUKSEN TESTAAMISEEN: 

Toistaiseksi sovellukseen riittää, että tekee uuden käyttäjän niin saa pääsyn tietokantoihin. Tietokannat eivät siis ole käyttäjäkohtaisia. 

SQL-komennot tietokantojen luomiseen testikäyttöä varten. 

CREATE TABLE foods (id SERIAL PRIMARY KEY, name TEXT, amount INT,  visible INT, stored INT); 
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



