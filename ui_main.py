# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maincPwwYy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(51, 54, 69);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 50))
        self.Top_Bar.setStyleSheet(
            u"QFrame {\n" "	background-color: rgb(40, 42, 54);\n" "}"
        )
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.label_title = QLabel(self.Top_Bar)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Hack Nerd Font")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(
            u"QLabel {\n" "	color: #f5f6f9;\n" "	padding-left: 0px;\n" "}"
        )

        self.horizontalLayout.addWidget(self.label_title)

        self.btn_editor = QPushButton(self.Top_Bar)
        self.btn_editor.setObjectName(u"btn_editor")
        self.btn_editor.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"Hack Nerd Font")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_editor.setFont(font1)
        self.btn_editor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editor.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(140, 184, 255);\n"
            "}"
        )
        self.btn_editor.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_editor)

        self.btn_ejecutar = QPushButton(self.Top_Bar)
        self.btn_ejecutar.setObjectName(u"btn_ejecutar")
        self.btn_ejecutar.setMinimumSize(QSize(0, 50))
        self.btn_ejecutar.setFont(font1)
        self.btn_ejecutar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ejecutar.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(140, 184, 255);\n"
            "}"
        )
        self.btn_ejecutar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_ejecutar)

        self.btn_reportes = QPushButton(self.Top_Bar)
        self.btn_reportes.setObjectName(u"btn_reportes")
        self.btn_reportes.setMinimumSize(QSize(0, 50))
        self.btn_reportes.setFont(font1)
        self.btn_reportes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reportes.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(140, 184, 255);\n"
            "}"
        )
        self.btn_reportes.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_reportes)

        self.btn_acerca_de = QPushButton(self.Top_Bar)
        self.btn_acerca_de.setObjectName(u"btn_acerca_de")
        self.btn_acerca_de.setMinimumSize(QSize(0, 50))
        self.btn_acerca_de.setFont(font1)
        self.btn_acerca_de.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acerca_de.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(140, 184, 255);\n"
            "}"
        )
        self.btn_acerca_de.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btn_acerca_de)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.console = QTextEdit(self.page_1)
        self.console.setObjectName(u"console")
        self.console.setEnabled(True)
        font2 = QFont()
        font2.setFamily(u"Hack Nerd Font")
        font2.setPointSize(12)
        self.console.setFont(font2)
        self.console.setStyleSheet(
            u"QTextEdit {\n"
            "	color: rgb(255, 255, 255);\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.console.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.console.setLineWrapMode(QTextEdit.NoWrap)
        self.console.setReadOnly(True)
        self.console.setTabStopWidth(self.console.fontMetrics().width(' ') * 4)

        self.gridLayout.addWidget(self.console, 1, 1, 1, 1)

        self.label_consola = QLabel(self.page_1)
        self.label_consola.setObjectName(u"label_consola")
        self.label_consola.setMinimumSize(QSize(0, 40))
        self.label_consola.setFont(font)
        self.label_consola.setStyleSheet(u"QLabel {\n" "	color: #f5f6f9;\n" "}")

        self.gridLayout.addWidget(self.label_consola, 0, 1, 1, 1)

        self.editor = QTextEdit(self.page_1)
        self.editor.setObjectName(u"editor")
        font3 = QFont()
        font3.setFamily(u"Hack Nerd Font")
        font3.setPointSize(12)
        font3.setKerning(True)
        self.editor.setFont(font3)
        self.editor.setStyleSheet(
            u"QTextEdit {\n"
            "	color: rgb(255, 255, 255);\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.editor.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.editor.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.editor.setLineWrapMode(QTextEdit.NoWrap)
        self.editor.setTabStopWidth(self.editor.fontMetrics().width(' ') * 4)

        self.gridLayout.addWidget(self.editor, 1, 0, 1, 1)

        self.label_editor = QLabel(self.page_1)
        self.label_editor.setObjectName(u"label_editor")
        self.label_editor.setMinimumSize(QSize(0, 40))
        self.label_editor.setFont(font)
        self.label_editor.setStyleSheet(u"QLabel {\n" "	color: #f5f6f9;\n" "}")

        self.gridLayout.addWidget(self.label_editor, 0, 0, 1, 1)

        self.verticalLayout_7.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Reportes_Bar = QFrame(self.page_2)
        self.Reportes_Bar.setObjectName(u"Reportes_Bar")
        self.Reportes_Bar.setMaximumSize(QSize(16777215, 50))
        self.Reportes_Bar.setFrameShape(QFrame.StyledPanel)
        self.Reportes_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Reportes_Bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_simbolos = QPushButton(self.Reportes_Bar)
        self.btn_simbolos.setObjectName(u"btn_simbolos")
        self.btn_simbolos.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamily(u"Hack Nerd Font")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_simbolos.setFont(font4)
        self.btn_simbolos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_simbolos.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: #f1fa8c;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.btn_simbolos)

        self.btn_errores = QPushButton(self.Reportes_Bar)
        self.btn_errores.setObjectName(u"btn_errores")
        self.btn_errores.setMinimumSize(QSize(0, 50))
        self.btn_errores.setFont(font4)
        self.btn_errores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_errores.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: #f1fa8c;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.btn_errores)

        self.btn_bases = QPushButton(self.Reportes_Bar)
        self.btn_bases.setObjectName(u"btn_bases")
        self.btn_bases.setMinimumSize(QSize(0, 50))
        self.btn_bases.setFont(font4)
        self.btn_bases.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bases.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: #f1fa8c;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.btn_bases)

        self.btn_tablas = QPushButton(self.Reportes_Bar)
        self.btn_tablas.setObjectName(u"btn_tablas")
        self.btn_tablas.setMinimumSize(QSize(0, 50))
        self.btn_tablas.setFont(font4)
        self.btn_tablas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tablas.setStyleSheet(
            u"QPushButton {\n"
            "	color: rgb(40, 42, 54);\n"
            "	background-color: rgb(108, 124, 150);\n"
            "	border-radius: 15px;\n"
            "	border: 1px solid;\n"
            "	margin: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: #f1fa8c;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.btn_tablas)

        self.verticalLayout_6.addWidget(self.Reportes_Bar)

        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.page_4)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 0)
        self.label_simbolos = QLabel(self.page_4)
        self.label_simbolos.setObjectName(u"label_simbolos")
        font5 = QFont()
        font5.setFamily(u"Hack Nerd Font")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_simbolos.setFont(font5)
        self.label_simbolos.setStyleSheet(u"color: #f5f6f9;")
        self.label_simbolos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_simbolos)

        self.table_simbolos = QTableWidget(self.page_4)
        if self.table_simbolos.columnCount() < 6:
            self.table_simbolos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_simbolos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_simbolos.setObjectName(u"table_simbolos")
        font6 = QFont()
        font6.setFamily(u"Hack Nerd Font")
        font6.setPointSize(10)
        self.table_simbolos.setFont(font6)
        self.table_simbolos.setStyleSheet(
            u"QTableWidget {\n"
            "	background-color: rgb(51, 54, 69);\n"
            "	selection-background-color: rgb(108, 124, 150);\n"
            "	color: #f5f6f9;\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.table_simbolos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_simbolos.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_simbolos)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 15, 0, 0)
        self.label_errores = QLabel(self.page_5)
        self.label_errores.setObjectName(u"label_errores")
        self.label_errores.setFont(font5)
        self.label_errores.setStyleSheet(u"color: #f5f6f9;")
        self.label_errores.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_errores)

        self.table_errores = QTableWidget(self.page_5)
        if self.table_errores.columnCount() < 6:
            self.table_errores.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_errores.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.table_errores.setObjectName(u"table_errores")
        self.table_errores.setFont(font6)
        self.table_errores.setStyleSheet(
            u"QTableWidget {\n"
            "	background-color: rgb(51, 54, 69);\n"
            "	selection-background-color: rgb(108, 124, 150);\n"
            "	color: #f5f6f9;\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.table_errores.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.table_errores)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_4 = QVBoxLayout(self.page_6)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.label_bases = QLabel(self.page_6)
        self.label_bases.setObjectName(u"label_bases")
        self.label_bases.setFont(font5)
        self.label_bases.setStyleSheet(u"color: #f5f6f9;")
        self.label_bases.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_bases)

        self.table_bases = QTableWidget(self.page_6)
        if self.table_bases.columnCount() < 4:
            self.table_bases.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_bases.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_bases.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_bases.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_bases.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.table_bases.setObjectName(u"table_bases")
        self.table_bases.setFont(font6)
        self.table_bases.setStyleSheet(
            u"QTableWidget {\n"
            "	background-color: rgb(51, 54, 69);\n"
            "	selection-background-color: rgb(108, 124, 150);\n"
            "	color: #f5f6f9;\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.table_bases.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.table_bases)

        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_3 = QVBoxLayout(self.page_7)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.label_tablas = QLabel(self.page_7)
        self.label_tablas.setObjectName(u"label_tablas")
        self.label_tablas.setFont(font5)
        self.label_tablas.setStyleSheet(u"color: #f5f6f9;")
        self.label_tablas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_tablas)

        self.table_tablas = QTableWidget(self.page_7)
        if self.table_tablas.columnCount() < 4:
            self.table_tablas.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_tablas.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_tablas.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_tablas.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_tablas.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.table_tablas.setObjectName(u"table_tablas")
        self.table_tablas.setFont(font6)
        self.table_tablas.setStyleSheet(
            u"QTableWidget {\n"
            "	background-color: rgb(51, 54, 69);\n"
            "	selection-background-color: rgb(108, 124, 150);\n"
            "	color: #f5f6f9;\n"
            "	border: 2px solid #282a36;\n"
            "}"
        )
        self.table_tablas.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_tablas)

        self.stackedWidget_2.addWidget(self.page_7)

        self.verticalLayout_6.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_datos = QLabel(self.page_3)
        self.label_datos.setObjectName(u"label_datos")
        font7 = QFont()
        font7.setFamily(u"Hack Nerd Font")
        font7.setPointSize(18)
        self.label_datos.setFont(font7)
        self.label_datos.setStyleSheet(
            u"QLabel {\n" "	color: #f5f6f9;\n" "	border: 2px solid #282a36;\n" "}"
        )
        self.label_datos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_datos)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"DB-Rust", None)
        )
        self.label_title.setText(
            QCoreApplication.translate("MainWindow", u"DB-RUST", None)
        )
        self.btn_editor.setText(
            QCoreApplication.translate("MainWindow", u" Editor", None)
        )
        self.btn_ejecutar.setText(
            QCoreApplication.translate("MainWindow", u" Ejecutar", None)
        )
        self.btn_reportes.setText(
            QCoreApplication.translate("MainWindow", u" Reportes", None)
        )
        self.btn_acerca_de.setText(
            QCoreApplication.translate("MainWindow", u" Acerca de", None)
        )
        self.console.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"david_maldo:~/Proyecto 1$ ", None
            )
        )
        self.label_consola.setText(
            QCoreApplication.translate("MainWindow", u"Consola", None)
        )
        self.label_editor.setText(
            QCoreApplication.translate("MainWindow", u"Entrada", None)
        )
        self.btn_simbolos.setText(
            QCoreApplication.translate("MainWindow", u"Tabla de S\u00edmbolos", None)
        )
        self.btn_errores.setText(
            QCoreApplication.translate("MainWindow", u"Tabla de Errores", None)
        )
        self.btn_bases.setText(
            QCoreApplication.translate("MainWindow", u"Bases de Datos Existentes", None)
        )
        self.btn_tablas.setText(
            QCoreApplication.translate("MainWindow", u"Tablas de Base de Datos", None)
        )
        self.label_simbolos.setText(
            QCoreApplication.translate("MainWindow", u"Tabla de S\u00edmbolos", None)
        )
        ___qtablewidgetitem = self.table_simbolos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"ID", None)
        )
        ___qtablewidgetitem1 = self.table_simbolos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Tipo S\u00edmbolo", None)
        )
        ___qtablewidgetitem2 = self.table_simbolos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Tipo Dato", None)
        )
        ___qtablewidgetitem3 = self.table_simbolos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"\u00c1mbito", None)
        )
        ___qtablewidgetitem4 = self.table_simbolos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Fila", None)
        )
        ___qtablewidgetitem5 = self.table_simbolos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None)
        )
        self.label_errores.setText(
            QCoreApplication.translate("MainWindow", u"Tabla de Errores", None)
        )
        ___qtablewidgetitem6 = self.table_errores.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", u"No.", None)
        )
        ___qtablewidgetitem7 = self.table_errores.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None)
        )
        ___qtablewidgetitem8 = self.table_errores.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"\u00c1mbito", None)
        )
        ___qtablewidgetitem9 = self.table_errores.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Fila", None)
        )
        ___qtablewidgetitem10 = self.table_errores.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None)
        )
        ___qtablewidgetitem11 = self.table_errores.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"Fecha y Hora", None)
        )
        self.label_bases.setText(
            QCoreApplication.translate(
                "MainWindow", u"Tabla de Bases de Datos Existentes", None
            )
        )
        ___qtablewidgetitem12 = self.table_bases.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"No.", None)
        )
        ___qtablewidgetitem13 = self.table_bases.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"Nombre", None)
        )
        ___qtablewidgetitem14 = self.table_bases.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"No. Tablas", None)
        )
        ___qtablewidgetitem15 = self.table_bases.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindow", u"Fila", None)
        )
        self.label_tablas.setText(
            QCoreApplication.translate("MainWindow", u"Tablas de Base de Datos", None)
        )
        ___qtablewidgetitem16 = self.table_tablas.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate("MainWindow", u"No.", None)
        )
        ___qtablewidgetitem17 = self.table_tablas.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindow", u"Nombre Tabla", None)
        )
        ___qtablewidgetitem18 = self.table_tablas.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("MainWindow", u"Nombre Base de Datos", None)
        )
        ___qtablewidgetitem19 = self.table_tablas.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate("MainWindow", u"Fila", None)
        )
        self.label_datos.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Informaci\u00f3n:\n"
                "\n"
                "David Augusto Maldonado Hurtarte\n"
                "201908312\n"
                "OLC2 Secci\u00f3n D\n"
                "2do Semestre 2020",
                None,
            )
        )

    # retranslateUi
