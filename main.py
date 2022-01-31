import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from quiz_ui import Ui_MainWindow

KYSYMYKSET_JA_VASTAUKSET = [
    (
        "Mistä Python-ohjelmointikieli on saanut nimensä?",
        "käärmeestä",
        "laulusta",
        "*TV-sarjasta",
        "elokuvasta",
    ),
    (
        "Paljonko on 5*5?",
        "22",
        "*25",
        "27",
        "35",
    ),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vaihda_kysymys_ja_vastaukset(0)
        self.kytke_napit()

    def vaihda_kysymys_ja_vastaukset(self, indeksi):
        tekstit = KYSYMYKSET_JA_VASTAUKSET[indeksi]
        uudet_tekstit = []
        for (numero, teksti) in enumerate(tekstit):
            if teksti.startswith("*"):
                teksti = teksti[1:]
                self.oikea_vastaus = numero
            uudet_tekstit.append(teksti)
        self.aseta_tekstit(uudet_tekstit)

    def aseta_tekstit(self, tekstit):
        self.aseta_kysymys(tekstit[0])
        self.aseta_nappien_tekstit(tekstit[1:])

    def aseta_nappien_tekstit(self, tekstit):
        (t1, t2, t3, t4) = tekstit
        self.ui.button1.setText(t1)
        self.ui.button2.setText(t2)
        self.ui.button3.setText(t3)
        self.ui.button4.setText(t4)

    def aseta_kysymys(self, kysymys):
        self.ui.label.setText(kysymys)

    def kytke_napit(self):
        self.ui.button1.clicked.connect(self.nappia_painettu)
        self.ui.button2.clicked.connect(self.nappia_painettu)
        self.ui.button3.clicked.connect(self.nappia_painettu)
        self.ui.button4.clicked.connect(self.nappia_painettu)

    def nappia_painettu(self):
        if self.sender() == self.ui.button1:
            nappi = 1
        elif self.sender() == self.ui.button2:
            nappi = 2
        elif self.sender() == self.ui.button3:
            nappi = 3
        elif self.sender() == self.ui.button4:
            nappi = 4
        else:
            return

        if nappi == self.oikea_vastaus:
            print("Oikein!")

        print("PAINETTU NAPPIA")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
