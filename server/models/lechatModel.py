from pony.orm import Required, PrimaryKey, db_session
from . import db

class Product(db.Entity):
    # Definieren der Primärschlüssel-ID, die automatisch generiert wird
    id = PrimaryKey(int, auto=True)
    # Definieren der Felder 'name' und 'price', die erforderlich sind
    name = Required(str)
    price = Required(float)

    @db_session
    def before_insert(self):
        # Datenverarbeitung vor dem Einfügen in die Datenbank
        # Beispiel: Name normalisieren (Leerzeichen entfernen und ersten Buchstaben groß schreiben)
        self.name = self.name.strip().title()