# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1019, 585)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        font = QFont()
        font.setFamily(u"Script MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.actionAbrir.setFont(font)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGuardar.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamily(u"Pristina")
        font1.setPointSize(14)
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Id_spinBox = QSpinBox(self.groupBox)
        self.Id_spinBox.setObjectName(u"Id_spinBox")
        font2 = QFont()
        font2.setFamily(u"Rage Italic")
        font2.setPointSize(14)
        self.Id_spinBox.setFont(font2)

        self.gridLayout.addWidget(self.Id_spinBox, 0, 1, 1, 2)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 170, 127, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.Green_spinBox.setPalette(palette)
        self.Green_spinBox.setFont(font2)
        self.Green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Green_spinBox, 8, 1, 1, 2)

        self.Green = QLabel(self.groupBox)
        self.Green.setObjectName(u"Green")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.Green.setPalette(palette1)
        self.Green.setFont(font2)

        self.gridLayout.addWidget(self.Green, 8, 0, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setFont(font2)
        self.DestinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoY_spinBox, 4, 1, 1, 2)

        self.Id = QLabel(self.groupBox)
        self.Id.setObjectName(u"Id")
        self.Id.setFont(font2)

        self.gridLayout.addWidget(self.Id, 0, 0, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setFont(font2)

        self.gridLayout.addWidget(self.Velocidad_spinBox, 5, 1, 1, 2)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setFont(font2)
        self.OrigenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenY_spinBox, 2, 1, 1, 2)

        self.Color = QLabel(self.groupBox)
        self.Color.setObjectName(u"Color")
        palette2 = QPalette()
        brush4 = QBrush(QColor(85, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.Color.setPalette(palette2)
        self.Color.setFont(font2)

        self.gridLayout.addWidget(self.Color, 6, 0, 1, 1)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setFont(font2)
        self.DestinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoX_spinBox, 3, 1, 1, 2)

        self.Blue = QLabel(self.groupBox)
        self.Blue.setObjectName(u"Blue")
        palette3 = QPalette()
        brush5 = QBrush(QColor(0, 0, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.Blue.setPalette(palette3)
        self.Blue.setFont(font2)

        self.gridLayout.addWidget(self.Blue, 9, 0, 1, 1)

        self.Red = QLabel(self.groupBox)
        self.Red.setObjectName(u"Red")
        palette4 = QPalette()
        brush6 = QBrush(QColor(197, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.Red.setPalette(palette4)
        self.Red.setFont(font2)

        self.gridLayout.addWidget(self.Red, 7, 0, 1, 1)

        self.AgregarInicio = QPushButton(self.groupBox)
        self.AgregarInicio.setObjectName(u"AgregarInicio")
        font3 = QFont()
        font3.setFamily(u"Broadway")
        font3.setPointSize(12)
        self.AgregarInicio.setFont(font3)

        self.gridLayout.addWidget(self.AgregarInicio, 11, 0, 1, 3)

        self.AgregarFinal = QPushButton(self.groupBox)
        self.AgregarFinal.setObjectName(u"AgregarFinal")
        self.AgregarFinal.setFont(font3)
        self.AgregarFinal.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout.addWidget(self.AgregarFinal, 10, 0, 1, 3)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        brush8 = QBrush(QColor(0, 0, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.Blue_spinBox.setPalette(palette5)
        self.Blue_spinBox.setFont(font2)
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Blue_spinBox, 9, 1, 1, 2)

        self.DestinoY = QLabel(self.groupBox)
        self.DestinoY.setObjectName(u"DestinoY")
        self.DestinoY.setFont(font2)

        self.gridLayout.addWidget(self.DestinoY, 4, 0, 1, 1)

        self.Velocidad = QLabel(self.groupBox)
        self.Velocidad.setObjectName(u"Velocidad")
        self.Velocidad.setFont(font2)

        self.gridLayout.addWidget(self.Velocidad, 5, 0, 1, 1)

        self.OrigenY = QLabel(self.groupBox)
        self.OrigenY.setObjectName(u"OrigenY")
        self.OrigenY.setFont(font2)

        self.gridLayout.addWidget(self.OrigenY, 2, 0, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setFont(font2)
        self.OrigenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenX_spinBox, 1, 1, 1, 2)

        self.DestinoX = QLabel(self.groupBox)
        self.DestinoX.setObjectName(u"DestinoX")
        self.DestinoX.setFont(font2)

        self.gridLayout.addWidget(self.DestinoX, 3, 0, 1, 1)

        self.OrigenX = QLabel(self.groupBox)
        self.OrigenX.setObjectName(u"OrigenX")
        self.OrigenX.setFont(font2)

        self.gridLayout.addWidget(self.OrigenX, 1, 0, 1, 1)

        self.Mostrar = QPushButton(self.groupBox)
        self.Mostrar.setObjectName(u"Mostrar")
        self.Mostrar.setFont(font3)

        self.gridLayout.addWidget(self.Mostrar, 12, 0, 1, 3)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        palette6 = QPalette()
        brush9 = QBrush(QColor(185, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush9)
        brush10 = QBrush(QColor(185, 0, 0, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.Red_spinBox.setPalette(palette6)
        self.Red_spinBox.setFont(font2)
        self.Red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Red_spinBox, 7, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font2)

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Buscar = QLineEdit(self.tab_2)
        self.Buscar.setObjectName(u"Buscar")

        self.gridLayout_4.addWidget(self.Buscar, 1, 0, 1, 1)

        self.Buscar_Boton = QPushButton(self.tab_2)
        self.Buscar_Boton.setObjectName(u"Buscar_Boton")
        font4 = QFont()
        font4.setFamily(u"Broadway")
        font4.setPointSize(14)
        self.Buscar_Boton.setFont(font4)

        self.gridLayout_4.addWidget(self.Buscar_Boton, 1, 1, 1, 1)

        self.Mostrar_Tabla_Boton = QPushButton(self.tab_2)
        self.Mostrar_Tabla_Boton.setObjectName(u"Mostrar_Tabla_Boton")
        self.Mostrar_Tabla_Boton.setFont(font4)

        self.gridLayout_4.addWidget(self.Mostrar_Tabla_Boton, 1, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setPointSize(12)
        self.tableWidget.setFont(font5)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1019, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle("")
        self.Green.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.Id.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.Color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.Blue.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.Red.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.AgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.AgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.DestinoY.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.Velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.OrigenY.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.DestinoX.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.OrigenX.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.Mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de Particula", None))
        self.Buscar_Boton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Tabla_Boton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

