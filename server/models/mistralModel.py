from pony.orm import Required, PrimaryKey, db_session
from . import db

class User(db.Entity):
    # Definieren der Primärschlüssel-ID, die automatisch generiert wird
    id = PrimaryKey(int, auto=True)
    # Definieren der Felder 'name' und 'email', die erforderlich sind
    name = Required(str)
    email = Required(str)

    @db_session
    def before_insert(self):
        # Datenverarbeitung vor dem Einfügen in die Datenbank
        # Beispiel: Name normalisieren (Leerzeichen entfernen und ersten Buchstaben groß schreiben)
        self.name = self.name.strip().title()
        # Beispiel: E-Mail normalisieren (Leerzeichen entfernen und in Kleinbuchstaben umwandeln)
        self.email = self.email.strip().lower()