Tietokantasovellus harjoitustyö

sovellusta voi kokeilla Herokussa: https://tsoha-market.herokuapp.com/
Voi rekisteröityä ja jättää ilmoituksen ja lähettää viestejä. Ilmoitukseen pitää laittaa kuva muuten se ei näy. Sovellukseen voi kirjautua adminina tunnus: admin salasana: Sal975


- Sovelluksessa on etusivu jossa näkyvät uusimmat ilmoitukset aikajärjestyksess. Etusivulle pääsee Tsoha-Kauppa tekstistä vasemmassa ylänurkassa 
- Haulla voi etsiä ilmoituksia osastoittaan ja tehdä sanahakuja 
- Ilmoituksille voi laittaa viimeisen voimassaolopäivän jonka jälkeen ilmoitusta ei näytetä. Maksimi on 60 päivää.
- Käyttäjän tulee rekisteröity voidakseen lisätä ja poistaa ilmoituksia. 
- Käyttäjät voivat lähettää viestejä ilmoituksen jättäjälle mutta sovellus ei vastaa tiedoista joita käyttäjät toisilleen lähettävät. Eli näitä tieoja ei salata vaan viestit tallennetaan sellaisenaan tietokantaan. Viesteihin voi myös vastata.
- Käyttäjät eivät voi lisätä kategorioita vaan ainoastaa admin.
- Ilmoituksen tekemiseen on lomake johon syötetään tiedot ja valitaan kategoria, ilmoitustyyppi ja voimassaolo. Kaikkiin ilmoituksiin vaaditaan kuva.
 
Vielä tehtävää: Kaikki suunniteltu on toteutettu, osoto ilmoituksiin kuvan vaatiminen on asia joka pitäisi korjata mutta havahduin tähän ongelmaan liian myöhään, viestien järjestely olisi tehtävä paremmin. 



Sovellus on tarkoitettu tavaran (tai miksei palveluidenkin) myyntiin, ostamiseen, vaihtamiseen ja lahjoittamiseen. 

- Sovellukseen tulee etusivu jossa näkyvät uusimmat ilmoitukset.
- Ilmoitukseen tulee otsikko ja pidempi tekstikenttä ja siihen voi myös lisätä yhden kuvan. 
- Etusivulla näkyvät otsikot joista pääsee ilmoitukseen
- Ilmoitukset voi valita näytettäväksi myös kategorioittain ilmoitustyyppien mukaan(myynti, osto jne.) ja niitä voi selata sekä tehdä sanhakuja. 
- Ilmoituksille voi laittaa viimeisen voimassaolopäivän jonka jälkeen ilmoitusta ei näytetä
- Käyttäjän tulee rekisteröity voidakseen lisätä ja poistaa ilmoituksia. 
- Käyttäjät voivat lähettää viestejä ilmoituksen jättäjälle ja sovellus ei vastaa tiedoista joita käyttäjät toisilleen lähettävät. Eli näitä tieoja ei salata vaan viestit tallennetaan sellaisenaan tietokantaan
- Käyttäjät eivät voi lisätä kategorioita vaan ainoastaa admin.
- Ilmoituksen tekemiseen on lomake johon syötetään tiedot ja valitaan kategoria, ilmoitustyyppi ja voimassaolo.
- Hakuun tulee lomake jossa voi valita kategorian, ilmoitustyypin ja lisätä hakusanan.
- Sovelluksen asettelu on vielä mietinnän alla. Ulkoasussa hyödynnetään bootstrap kirjastoa.

Ajatus tietokannan tauluista:

CREATE TABLE users (<br>
    &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
    &nbsp;&nbsp;username TEXT UNIQUE,<br>
    &nbsp;&nbsp;password TEXT NOT NULL,<br> 
	  &nbsp;&nbsp;user_level INTEGER NOT NULL,<br>
);

CREATE TABLE messages (<br>
    &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
    &nbsp;&nbsp;content TEXT,<br>
    &nbsp;&nbsp;from_id INTEGER REFERENCES users,<br>
    &nbsp;&nbsp;to_id INTEGER REFERENCES users,<br>
    &nbsp;&nbsp;ent_at TIMESTAMP<br>
);

CREATE TABLE ad (<br>
    &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
    &nbsp;&nbsp;user_id INTEGER REFERENCES users,<br>
    &nbsp;&nbsp;cat_id INTEGER REFERENCES category,<br>
    &nbsp;&nbsp;ad_type INTEGER,<br>
    &nbsp;&nbsp;sent_at TIMESTAMP,<br>
    &nbsp;&nbsp;valid INTEGER,<br>
    &nbsp;&nbsp;item TEXT,<br>
    &nbsp;&nbsp;ad_text TEXT,<br>
    &nbsp;&nbsp;img INTEGER REFERENCES images<br>
);

CREATE TABLE category (<br>
    &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
    &nbsp;&nbsp;parent_id INTEGER,<br>
    &nbsp;&nbsp;dep INTEGER,<br>
    &nbsp;&nbsp;cat_name TEXT UNIQUE<br>
);

CREATE TABLE images (<br>
    &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
    &nbsp;&nbsp;data BYTEA<br>
);
