class Clovek:
    def __init__(self, cele_jmeno, datum_narozeni, kontaktni_cislo, mesto, zeme, adresa_bydliste):
        self._cele_jmeno = cele_jmeno
        self._datum_narozeni = datum_narozeni
        self._kontaktni_cislo = kontaktni_cislo
        self._mesto = mesto
        self._zeme = zeme
        self._adresa_bydliste = adresa_bydliste

    # Metody pro nastavení hodnot (settery)
    def set_cele_jmeno(self, cele_jmeno):
        self._cele_jmeno = cele_jmeno

    def set_datum_narozeni(self, datum_narozeni):
        self._datum_narozeni = datum_narozeni

    def set_kontaktni_cislo(self, kontaktni_cislo):
        self._kontaktni_cislo = kontaktni_cislo

    def set_mesto(self, mesto):
        self._mesto = mesto

    def set_zeme(self, zeme):
        self._zeme = zeme

    def set_adresa_bydliste(self, adresa_bydliste):
        self._adresa_bydliste = adresa_bydliste

    # Metody pro získání hodnot (gettery)
    def get_cele_jmeno(self):
        return self._cele_jmeno

    def get_datum_narozeni(self):
        return self._datum_narozeni

    def get_kontaktni_cislo(self):
        return self._kontaktni_cislo

    def get_mesto(self):
        return self._mesto

    def get_zeme(self):
        return self._zeme

    def get_adresa_bydliste(self):
        return self._adresa_bydliste

    # Metoda pro výstup dat
    def print_info(self):
        print(f"Celé jméno: {self.get_cele_jmeno()}")
        print(f"Datum narození: {self.get_datum_narozeni()}")
        print(f"Kontaktní číslo: {self.get_kontaktni_cislo()}")
        print(f"Město: {self.get_mesto()}")
        print(f"Země: {self.get_zeme()}")
        print(f"Adresa bydliště: {self.get_adresa_bydliste()}")

    # Metoda pro vstup dat
    def input_info(self):
        self.set_cele_jmeno(input("Zadejte celé jméno: "))
        self.set_datum_narozeni(input("Zadejte datum narození (např. 1.1.1990): "))
        self.set_kontaktni_cislo(input("Zadejte kontaktní číslo: "))
        self.set_mesto(input("Zadejte město: "))
        self.set_zeme(input("Zadejte zemi: "))
        self.set_adresa_bydliste(input("Zadejte adresu bydliště: "))

# Ukázka použití třídy
clovek = Clovek("Jan Novák", "1.1.1990", "123456789", "Praha", "Česká republika", "Náměstí 1")
clovek.print_info()

# Umožnění uživateli zadat nové informace
clovek.input_info()
clovek.print_info()
