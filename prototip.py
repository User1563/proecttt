import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *



class MonitoringApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(uifile='hjol.py')

        self.b = {}
        self.d = []
        self.sett = set()
        self.selectedItemListWidget = None

        self.nm = {
            'Загрузка данных': [self.btnDownloadTab.clicked.connect(self.navigate), 1],
            'Визуализация данных': [self.btnVisualTab.clicked.connect(self.navigate), 2],
            'Анализ данных': [self.btnAnaLizetad.clicked.connect(self.navigate), 3],
            'Прогноз': [self.btnPredicTad.clicked.connect(self.navigate), 2],
            'Мониторинг': [self.btnMonitoringTad.clicked.connect(self.navigate), 1],
            'Экспорт': [self.btnExportTad.clicked.connect(self.navigate), 2]
        }


    def navigate(self):
        print(self.sunder().text(), self.navTad[self.sender().text()][1])
        self.tadWidget.fileDataRead(self.navTad[self.sender().text()][1])

        self.homeBtnDowloadTab.clicked.connect(self.homeGo)
        self.homeBtnVisualTab.clicked.connect(self.homeGo)
        self.homeBtnAnalisTab.clicked.connect(self.homeGo)
        self.homeBtnPredictTab.clicked.connect(self.homeGo)
        self.homeBtnmonitoringTab.clicked.connect(self.homeGo)

    def homeGo(self):
        self.tabWidget.fileDataRead(0)


app = QApplication(sys.argv)
ex = MonitoringApp()
ex.show()
sys.exit(app.exec())


