Tietokantasovellus harjoitustyö

sovellusta voi kokeilla Herokussa: https://tsoha-market.herokuapp.com/
Voi rekisteröityä ja jättää ilmoituksen ja lähettää viestejä. Ilmoitukseen pitää laittaa kuva muuten se ei näy.

Sovelluksen nyky tilanne:
- Sovellukseen tulee etusivu jossa näkyvät uusimmat ilmoitukset.
- Ilmoitukseen tulee otsikko ja pidempi tekstikenttä ja siihen voi myös lisätä yhden kuvan. 
- Etusivulla näkyvät otsikot joista klikkaamalla avautuu koko ilmoitus
- Ilmoitukset voi valita näytettäväksi myös kategorioittain ilmoitustyyppien mukaan(myynti, osto jne.) ja niitä voi selata sekä tehdä sanhakuja. 
- Käyttäjät voivat lähettää viestejä ilmoituksen jättäjälle ja sovellus ei vastaa tiedoista joita käyttäjät toisilleen lähettävät. Eli näitä tieoja ei salata vaan viestit tallennetaan sellaisenaan tietokantaan
- Ilmoituksen tekemiseen on lomake johon syötetään tiedot ja valitaan kategoria, ilmoitustyyppi
-Rekisteröityminen, kirjautuminen ja uloskirjautuminen on toteutettu. 

Toteuttamatta vielä:
- Ilmoitukset voi valita näytettäväksi myös kategorioittain ilmoitustyyppien mukaan(myynti, osto jne.) ja niitä voi selata sekä tehdä sanhakuja. 
- Ilmoituksille voi laittaa viimeisen voimassaolopäivän jonka jälkeen ilmoitusta ei näytetä
-Ilmoitusten poistamien on toteuttamatta 
- Hakuun tulee lomake jossa voi valita kategorian, ilmoitustyypin ja lisätä hakusanan
-useita bugeja korjattavana jotka liittyvät siihen onko käyttäjä rekisteröitynyt vai ei. Lisäksi syötteiden oikeallisuutta pitää parantaa. 




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
