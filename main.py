import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from Analyzer.parser import parser
from Instruction.FunctionDeclaration import FunctionDeclaration
from Instruction.FunctionCall import FunctionCall
from Instruction.NewStruct import NewStruct
from Instruction.Println import CONSOLE_CONTENT
from Util.Error import ERRORS_
from Util.Scope import Scope
from Util.Symbol import SYMBOLS

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configuracion
        self.setUpIcons()
        self.setUpNavBar()
        self.setUpReportesBar()
        self.setUpTables()

        self.show()

    def ejecutar(self):
        input = self.ui.editor.toPlainText()
        self.ui.console.clear()
        self.ui.console.append("david_maldo:~/Proyecto 1$")
        CONSOLE_CONTENT.clear()
        SYMBOLS.clear()
        ERRORS_.clear()
        if input != "":
            ast = parser.parse(input, tracking=True)
            g_scope = Scope(None, "Global")
            for node in ast:
                if isinstance(node, FunctionDeclaration):
                    node.execute(g_scope)
                elif isinstance(node, NewStruct):
                    node.execute(g_scope)
            main = FunctionCall(0, 0, "main", [])
            main.execute(g_scope)
            for output in CONSOLE_CONTENT:
                self.ui.console.append(f"$ {output}")
        else:
            self.ui.console.append(f"$ Aún no ha ingresado código para analizar!")

    def setUpIcons(self):
        self.setWindowIcon(QtGui.QIcon("./assets/user-astronaut-solid.svg"))
        self.ui.btn_editor.setIcon(QtGui.QIcon("./assets/code-solid.svg"))
        self.ui.btn_ejecutar.setIcon(QtGui.QIcon("./assets/circle-play-solid.svg"))
        self.ui.btn_reportes.setIcon(QtGui.QIcon("./assets/file-lines-solid.svg"))
        self.ui.btn_acerca_de.setIcon(QtGui.QIcon("./assets/circle-info-solid.svg"))

    def setUpNavBar(self):
        # Editor Page
        self.ui.btn_editor.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        )

        # Ejecutar
        self.ui.btn_ejecutar.clicked.connect(lambda: self.ejecutar())

        # Reportes Page
        self.ui.btn_reportes.clicked.connect(lambda: self.reportesAction())

        # Acerca de Page
        self.ui.btn_acerca_de.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        )

    def setUpReportesBar(self):
        # Simbolos Page
        self.ui.btn_simbolos.clicked.connect(lambda: self.simbolosAction())

        # Errores Page
        self.ui.btn_errores.clicked.connect(lambda: self.erroresAction())

        # Bases Page
        self.ui.btn_bases.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        )

        # Tablas Page
        self.ui.btn_tablas.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7)
        )

    def setUpTables(self):
        afont = QtGui.QFont()
        afont.setFamily("Hack Nerd Font")
        afont.setPointSize(10)

        # Tabla Simbolos
        header1 = self.ui.table_simbolos.horizontalHeader()
        header1.setSectionResizeMode(0, QHeaderView.Stretch)
        header1.setSectionResizeMode(1, QHeaderView.Stretch)
        header1.setSectionResizeMode(2, QHeaderView.Stretch)
        header1.setSectionResizeMode(3, QHeaderView.Stretch)
        header1.setSectionResizeMode(4, QHeaderView.Stretch)
        header1.setSectionResizeMode(5, QHeaderView.Stretch)
        header1.setFont(afont)

        # Tabla Errores
        header2 = self.ui.table_errores.horizontalHeader()
        header2.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(1, QHeaderView.Stretch)
        header2.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header2.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header2.setFont(afont)

        # Tabla Bases
        header3 = self.ui.table_bases.horizontalHeader()
        header3.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(1, QHeaderView.Stretch)
        header3.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header3.setFont(afont)

        # Tabla Tablas
        header4 = self.ui.table_tablas.horizontalHeader()
        header4.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header4.setSectionResizeMode(1, QHeaderView.Stretch)
        header4.setSectionResizeMode(2, QHeaderView.Stretch)
        header4.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header4.setFont(afont)

    def setSymbols(self):
        self.ui.table_simbolos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.table_simbolos.setRowCount(len(SYMBOLS))
        for i, symbol in enumerate(SYMBOLS):
            self.ui.table_simbolos.setItem(i, 0, QTableWidgetItem(symbol.id))
            self.ui.table_simbolos.setItem(i, 1, QTableWidgetItem(symbol.type2))
            self.ui.table_simbolos.setItem(i, 2, QTableWidgetItem(symbol.type.fullname))
            self.ui.table_simbolos.setItem(i, 3, QTableWidgetItem(symbol.env))
            self.ui.table_simbolos.setItem(i, 4, QTableWidgetItem(str(symbol.line)))
            self.ui.table_simbolos.setItem(i, 5, QTableWidgetItem(str(symbol.col)))

    def reportesAction(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.setSymbols()

    def simbolosAction(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        self.setSymbols()

    def erroresAction(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)
        self.ui.table_errores.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.table_errores.setRowCount(len(ERRORS_))
        for i, err in enumerate(ERRORS_):
            self.ui.table_errores.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui.table_errores.setItem(i, 1, QTableWidgetItem(err.description))
            self.ui.table_errores.setItem(i, 2, QTableWidgetItem(err.env))
            self.ui.table_errores.setItem(i, 3, QTableWidgetItem(str(err.line)))
            self.ui.table_errores.setItem(i, 4, QTableWidgetItem(str(err.column)))
            self.ui.table_errores.setItem(i, 5, QTableWidgetItem(err.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
