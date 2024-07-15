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


class Mesto:
    def __init__(self, nazev_mesta, nazev_regionu, nazev_zeme, pocet_obyvatel, psc, smerove_cislo_oblasti):
        self._nazev_mesta = nazev_mesta
        self._nazev_regionu = nazev_regionu
        self._nazev_zeme = nazev_zeme
        self._pocet_obyvatel = pocet_obyvatel
        self._psc = psc
        self._smerove_cislo_oblasti = smerove_cislo_oblasti

    # Metody pro nastavení hodnot (settery)
    def set_nazev_mesta(self, nazev_mesta):
        self._nazev_mesta = nazev_mesta

    def set_nazev_regionu(self, nazev_regionu):
        self._nazev_regionu = nazev_regionu

    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_pocet_obyvatel(self, pocet_obyvatel):
        self._pocet_obyvatel = pocet_obyvatel

    def set_psc(self, psc):
        self._psc = psc

    def set_smerove_cislo_oblasti(self, smerove_cislo_oblasti):
        self._smerove_cislo_oblasti = smerove_cislo_oblasti

    # Metody pro získání hodnot (gettery)
    def get_nazev_mesta(self):
        return self._nazev_mesta

    def get_nazev_regionu(self):
        return self._nazev_regionu

    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_pocet_obyvatel(self):
        return self._pocet_obyvatel

    def get_psc(self):
        return self._psc

    def get_smerove_cislo_oblasti(self):
        return self._smerove_cislo_oblasti

    # Metoda pro výstup dat
    def print_info(self):
        print(f"Název města: {self.get_nazev_mesta()}")
        print(f"Název regionu: {self.get_nazev_regionu()}")
        print(f"Název země: {self.get_nazev_zeme()}")
        print(f"Počet obyvatel: {self.get_pocet_obyvatel()}")
        print(f"PSČ: {self.get_psc()}")
        print(f"Směrové číslo oblasti: {self.get_smerove_cislo_oblasti()}")

    # Metoda pro vstup dat
    def input_info(self):
        self.set_nazev_mesta(input("Zadejte název města: "))
        self.set_nazev_regionu(input("Zadejte název regionu: "))
        self.set_nazev_zeme(input("Zadejte název země: "))
        self.set_pocet_obyvatel(int(input("Zadejte počet obyvatel: ")))
        self.set_psc(input("Zadejte PSČ: "))
        self.set_smerove_cislo_oblasti(input("Zadejte směrové číslo oblasti: "))

# Ukázka použití třídy
mesto = Mesto("Praha", "Praha", "Česká republika", 1300000, "11000", "2")
mesto.print_info()

# Umožnění uživateli zadat nové informace
mesto.input_info()
mesto.print_info()

class Zeme:
    def __init__(self, nazev_zeme, kontinent, pocet_obyvatel, volaci_kod, hlavni_mesto, nazvy_mest):
        self._nazev_zeme = nazev_zeme
        self._kontinent = kontinent
        self._pocet_obyvatel = pocet_obyvatel
        self._volaci_kod = volaci_kod
        self._hlavni_mesto = hlavni_mesto
        self._nazvy_mest = nazvy_mest

    # Metody pro nastavení hodnot (settery)
    def set_nazev_zeme(self, nazev_zeme):
        self._nazev_zeme = nazev_zeme

    def set_kontinent(self, kontinent):
        self._kontinent = kontinent

    def set_pocet_obyvatel(self, pocet_obyvatel):
        self._pocet_obyvatel = pocet_obyvatel

    def set_volaci_kod(self, volaci_kod):
        self._volaci_kod = volaci_kod

    def set_hlavni_mesto(self, hlavni_mesto):
        self._hlavni_mesto = hlavni_mesto

    def set_nazvy_mest(self, nazvy_mest):
        self._nazvy_mest = nazvy_mest

    # Metody pro získání hodnot (gettery)
    def get_nazev_zeme(self):
        return self._nazev_zeme

    def get_kontinent(self):
        return self._kontinent

    def get_pocet_obyvatel(self):
        return self._pocet_obyvatel

    def get_volaci_kod(self):
        return self._volaci_kod

    def get_hlavni_mesto(self):
        return self._hlavni_mesto

    def get_nazvy_mest(self):
        return self._nazvy_mest

    # Metoda pro výstup dat
    def print_info(self):
        print(f"Název země: {self.get_nazev_zeme()}")
        print(f"Kontinent: {self.get_kontinent()}")
        print(f"Počet obyvatel: {self.get_pocet_obyvatel()}")
        print(f"Volací kód: {self.get_volaci_kod()}")
        print(f"Hlavní město: {self.get_hlavni_mesto()}")
        print(f"Názvy měst: {', '.join(self.get_nazvy_mest())}")

    # Metoda pro vstup dat
    def input_info(self):
        self.set_nazev_zeme(input("Zadejte název země: "))
        self.set_kontinent(input("Zadejte kontinent: "))
        self.set_pocet_obyvatel(int(input("Zadejte počet obyvatel: ")))
        self.set_volaci_kod(input("Zadejte volací kód: "))
        self.set_hlavni_mesto(input("Zadejte hlavní město: "))
        self.set_nazvy_mest(input("Zadejte názvy měst (oddělené čárkou): ").split(','))

# Ukázka použití třídy
zeme = Zeme("Česká republika", "Evropa", 10650000, "+420", "Praha", ["Brno", "Ostrava", "Plzeň"])
zeme.print_info()

# Umožnění uživateli zadat nové informace
zeme.input_info()
zeme.print_info()
