class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        strumenti = {}
        try:
            with open(file_path, "r") as f:
                linee = f.readlines()
                for linea in linee:
                    linea = linea.strip()
                    if not linea:
                        continue
                    parti = linea.split(";")
                    if len(parti) == 5:
                        C1 = parti[0]
                        C2 = parti[1]
                        C3 = parti[2]
                        C4 = int(parti[3])
                        C5 = float(parti[4])
            return strumenti
        except FileNotFoundError:

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
