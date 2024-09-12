Ostosten hallinta-sovellus 

Sovelluksen tarkoitus on hallita kotona olevia ruokia, suunnitella tulevia ruokia ja luoda kauppalista niiden perusteella, ja siten helpottaa arjen ruokaostosten tekemistä. Sen avulla voi myös seurata ruokiin kuluvia menoja. 

Applikaatiossa on viisi sivua: Etusivu, Ostoslista, Ruoat, Reseptit ja Kulut.

ETUSIVU-sivulla kirjaudutaan sisään applikaatioon tai luodaan tunnus. 

OSTOSLISTA-sivu listaa kauppalistan, johon on lisätty kahdelta muulta ruoat- ja reseptit-sivuilta ruoka-ainekset, joita tulee ostaa kaupasta. Ainesten järjestystä on mahdollista muuttaa, jotta se vastaa tavaroiden sijaintia kun kuljetaan kaupan läpi. Koko kauppalistan voi kerralla siirtää varastossa olevaksi. 
Ostoksen lisääminen tietokantaan vaatii ruoan nimen, määrän, tyypin (järjestystä varten). Lisäksi tietokannassa on sen näkyvyys.
CREATE TABLE groceries (id SERIAL PRIMARY KEY, name TEXT, amount INT, type INT, visible INT);

FOODS-sivu listaa kaikki ruoka-ainekset, joita kotona yleensä käytetään. Sivu näyttää ensimmäisenä ne ruuat, joita on jo kotona, ja sen jälkeen ne, joita ei ole. Tällä sivulla niitä voi lisätä ja poistaa sekä lisätä kauppalistaan. Varastossa-otsikon alla on ruoat, joita on kotona varastossa ja Loppuneet ruoat otsikon alla ne mitkä on loppu. Poistettaessa ruoka-aines merkitään näkymättömäksi. Mahdollisesti on oltava kokonaan aineksen poistava ominaisuus. 
Ruoan lisääminen tietokantaan vaatii ruoan nimen, määrän, ja tiedon onko sitä varastossa. Lisäksi tietokannassa on sen näkyvyys.
CREATE TABLE foods (id SERIAL PRIMARY KEY, name TEXT, amount INT,  visible INT, stored INT); 

RESEPTIT-sivu listaa reseptit ja niiden ainesosat. Tällä sivulla reseptejä voi lisätä ja poistaa sekä lisätä ainesosat kauppalistaan.  Jos jokin reseptin ruoka-aine ei ole foods-tietokannassa, niin se lisätään ensin sinne. Lisääminen tietokantaan vaatii reseptin nimen, listan pakollisista ainesosista ja listan valinnaisista ainesosista. 
Respetejä voi myös muokata. 
Reseptin tiedot tietokannassa on sen nimi, ainesosat ja lisätiedot. 
CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, ingredients TEXT, additional TEXT);  

KULUT-sivulle kirjataan kulut joita on mennyt kaupassa käyntiin. Tietokannassa on tiedot kulutetusta rahasta ja ajankohdasta. 
CREATE TABLE expenses (id SERIAL PRIMARY KEY, time TIMESTAMP, value INT); 

Lisäksi sovelluksessa on tietokanta käyttäjistä. 
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT); 


