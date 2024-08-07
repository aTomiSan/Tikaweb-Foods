# Tikaweb-Foods

Ruokalista -appi  

Applikaation tarkoitus on hallita kotona olevia ruokia, suunnitella tulevia ruokia ja luoda kauppalista niiden perusteella, ja siten helpottaa arjen ruokaostosten tekemistä. 

Applikaatiossa on neljä sivua: index, foods, recipes ja groceries (eli kauppalista).

Index-sivulla kirjaudutaan sisään applikaatioon tai luodaan uusi käyttäjätunnus. Tällä sivulla voi myös lisätä ystävän, joka pääsee näkemään ja muokkaamaan samoja tietokantoja.  
Funktiot:
def log_in()       # kirjaudu sisään
def log_out()      # kirjaudu ulos
def sign_in()      # luo käyttäjätunnus 
def add_friend()   # lisää ystävä 
SQL:
CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, password TEXT, friends LIST) 


Foods-sivu  listaa kaikki ruoka-ainekset, joita kotona yleensä käytetään. Sivu näyttää ensimmäisenä ne ruuat, joita on jo kotona, ja sen jälkeen ne, joita ei ole. Tällä sivulla niitä voi lisätä ja poistaa sekä lisätä kauppalistaan.
Lisääminen tietokantaan vaatii ruokalajin nimen, tyypin (hedelmä/vihannes, kuivaruoka, proteiini, maitotuotteet, kuiva-aineet, tavarat jne) numeroituina, koon, kappalemäärän, varastossa, kauppalistalla, ja näkyvyys. 
Varastossa-sarake määrittää onko ruokaa kotona varastossa, ja sitä pystyy vaihtamaan tällä sivulla. 
Pakkauskoko auttaa reseptien automaattisessa lisäämisessä, esim. yksi punajuuripussi on 2x koska siitä riittää kahteen ruokaan.
Poistettaessa ruoka-aines merkitään näkymättömäksi. Mahdollisesti on oltava kokonaan aineksen poistava ominaisuus. 
SQL: 
CREATE TABLE foods (id SERIAL PRIMARY KEY, nimi, tyyppi, koko, kpl, varastossa, kauppalistalla, visibility ) 
Funktiot: 
def add(food) 		            # lisää ruoka listaan 
def remove(food)              # poistaa ruoan listasta ja merkitsee tietokannasta visibilityn nollaksi 
def store(food)               # merkitsee ruoan varastossa olevaksi 
def unstore(food)             # merkitsee ruoan pois varastosta/loppuneeksi 
def add_grocery(food) 	    	# lisää ainesosan kauppalistaan
def remove_permanently(food)  # poistaa ruoan tietokannasta kokonaan


Recipes-sivu listaa reseptit ja niiden ainesosat. Tällä sivulla reseptejä voi lisätä ja poistaa sekä lisätä kauppalistaan. 
Jos jokin reseptin ruoka-aine ei ole foods-tietokannassa, niin se pitää ensin lisätä sinne. 
Resepteissä on pakolliset ja valinnaiset ainesosat. 
Lisääminen tietokantaan vaatii reseptin nimen, listan pakollisista ainesosista ja listan valinnaisista ainesosista. 
Respetejä voi myös muokata. 
SQL: CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, foods LIST) 
Funktiot: 
def add_recipe()                #
def remove_recipe(recipe)       #
def edit_recipe(recipe)         #
def choose_recipe()             # lisää reseptin ainesosat kauppalistaan, jos niitä ei ole varastossa   


Groceries-sivu listaa kauppalistan, johon on lisätty kahdelta aiemmalta sivulta ruoka-ainekset, joita tulee ostaa kaupasta. 
Ainekset on listattu niiden tyypin mukaan siten, että ne vastaa tavaroiden sijaintia kun kuljetaan kaupan läpi. Tätä järjestystä on mahdollista muuttaa tällä sivulla. 
SQL: 
CREATE TABLE groceries (id, nimi, tyyppi)
Funktiot: 
def add_grocery(food)           # lisää ainesosat kauppalistaan, jos niitä ei ole varastossa   
def remove_grocery(food)        # poistaa ainesosan kauppalistasta


