import sys
import backend as bk
from PyQt5 import QtGui, QtCore, QtWidgets


class Controller:
    def __init__(self):
        self.mainwindow = MainAppWindow()
        self.centrality = CentralityWindow()
        self.accessibility = AccessibilityWindow()

    def open_main(self):
        self.mainwindow.switch_window2.connect(self.open_cent)
        self.mainwindow.switch_window3.connect(self.open_access)
        self.centrality.hide()
        self.accessibility.hide()
        self.mainwindow.show()

    def open_cent(self):
        self.centrality.switch_window.connect(self.open_main)
        self.mainwindow.hide()
        self.centrality.show()

    def open_access(self):
        self.accessibility.switch_window.connect(self.open_main)
        self.mainwindow.hide()
        self.accessibility.show()


class MainAppWindow(QtWidgets.QFrame):

    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        super(MainAppWindow, self).__init__()

        self.mainwindow = MainWindow()
        self.mainwindow.setupUi(self)
        self.mainwindow.CentralityAnalysisButton.clicked.connect(
            self.open_cent_handler
            )
        self.mainwindow.AccessibilityAnalysisButton.clicked.connect(
            self.open_access_handler
            )

    def open_cent_handler(self):
        self.switch_window2.emit()

    def open_access_handler(self):
        self.switch_window3.emit()


class CentralityWindow(QtWidgets.QFrame):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(CentralityWindow, self).__init__()
        self.centrality = Centrality()
        self.centrality.setupUi(self)
        self.centrality.BackButton.clicked.connect(self.open_main_handler)

    def open_main_handler(self):
        self.switch_window.emit()


class AccessibilityWindow(QtWidgets.QFrame):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(AccessibilityWindow, self).__init__()
        self.accessibility = Accessibility()
        self.accessibility.setupUi(self)
        self.accessibility.BackButton.clicked.connect(self.open_main_handler)

    def open_main_handler(self):
        self.switch_window.emit()


class MainWindow(object):
    def setupUi(self, MainFrame):
        MainFrame.setObjectName("MainFrame")
        MainFrame.setFixedSize(870, 230)
        MainFrame.setWindowIcon(QtGui.QIcon("interface.ico"))
        MainFrame.setFrameShape(QtWidgets.QFrame.Box)

        # Fonts
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)

        font2 = QtGui.QFont()
        font2.setFamily("Palatino Linotype")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)

        font3 = QtGui.QFont()
        font3.setFamily("Palatino Linotype")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)

        # Labels
        self.ChooseAnalysisLabel = QtWidgets.QLabel(MainFrame)
        self.ChooseAnalysisLabel.setGeometry(QtCore.QRect(310, 20, 251, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.ChooseAnalysisLabel.setPalette(palette)
        self.ChooseAnalysisLabel.setFont(font2)
        self.ChooseAnalysisLabel.setAutoFillBackground(False)
        self.ChooseAnalysisLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Buttons
        self.CentralityAnalysisButton = QtWidgets.QPushButton(MainFrame)
        self.CentralityAnalysisButton.setGeometry(QtCore.QRect(350, 100,
                                                               181, 31))
        self.CentralityAnalysisButton.setFont(font3)

        self.AccessibilityAnalysisButton = QtWidgets.QPushButton(MainFrame)
        self.AccessibilityAnalysisButton.setGeometry(QtCore.QRect(350, 140,
                                                                  181, 31))
        self.AccessibilityAnalysisButton.setFont(font3)

        self.retranslateUi(MainFrame)
        QtCore.QMetaObject.connectSlotsByName(MainFrame)

    def retranslateUi(self, MainFrame):
        _translate = QtCore.QCoreApplication.translate
        MainFrame.setWindowTitle(_translate("MainFrame", "SATRAP"))
        self.CentralityAnalysisButton.setText(_translate(
            "MainFrame",
            "Centrality Analysis")
            )
        self.AccessibilityAnalysisButton.setText(_translate(
            "MainFrame",
            "Accessibility Analysis")
            )
        self.ChooseAnalysisLabel.setText(_translate("MainFrame",
                                                    "Choose Analysis"))


class Centrality(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(870, 230)
        Frame.setWindowIcon(QtGui.QIcon("interface.ico"))

        # Fonts
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setUnderline(False)

        font2 = QtGui.QFont()
        font2.setFamily("Palatino Linotype")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)

        self.verticalline = QtWidgets.QFrame(Frame)
        self.verticalline.setGeometry(QtCore.QRect(600, 0, 20, 231))
        self.verticalline.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalline.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Labels
        self.PolyBoundaryLabel = QtWidgets.QLabel(Frame)
        self.PolyBoundaryLabel.setGeometry(QtCore.QRect(20, 50, 181, 21))
        self.PolyBoundaryLabel.setFont(font)
        self.PolyBoundaryLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.RegionNameLabel = QtWidgets.QLabel(Frame)
        self.RegionNameLabel.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.RegionNameLabel.setFont(font)
        self.RegionNameLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.TransportationModeLabel = QtWidgets.QLabel(Frame)
        self.TransportationModeLabel.setGeometry(QtCore.QRect(20, 110,
                                                              181, 21))
        self.TransportationModeLabel.setFont(font)
        self.TransportationModeLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.WebMapLabel = QtWidgets.QLabel(Frame)
        self.WebMapLabel.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.WebMapLabel.setFont(font)
        self.WebMapLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.ShpOutputLabel = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel.setGeometry(QtCore.QRect(20, 170, 181, 21))
        self.ShpOutputLabel.setFont(font)
        self.ShpOutputLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.DataInputLabel = QtWidgets.QLabel(Frame)
        self.DataInputLabel.setGeometry(QtCore.QRect(640, 80, 111, 21))
        self.DataInputLabel.setFont(font)
        self.DataInputLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.AnalysisMethodLabel = QtWidgets.QLabel(Frame)
        self.AnalysisMethodLabel.setGeometry(QtCore.QRect(640, 110, 111, 21))
        self.AnalysisMethodLabel.setFont(font)
        self.AnalysisMethodLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        # TextBoxes
        self.PolyBoundaryBox = QtWidgets.QLineEdit(Frame)
        self.PolyBoundaryBox.setGeometry(QtCore.QRect(210, 50, 271, 20))

        self.RegionNameBox = QtWidgets.QLineEdit(Frame)
        self.RegionNameBox.setGeometry(QtCore.QRect(210, 80, 221, 20))
        self.RegionNameBox.setEnabled(False)

        self.RegionNumberBox = QtWidgets.QLineEdit(Frame)
        self.RegionNumberBox.setGeometry(QtCore.QRect(440, 80, 41, 20))
        self.RegionNumberBox.setEnabled(False)

        self.TransportationModeBox = QtWidgets.QLineEdit(Frame)
        self.TransportationModeBox.setGeometry(QtCore.QRect(210, 110, 271, 20))

        self.WebMapBox = QtWidgets.QLineEdit(Frame)
        self.WebMapBox.setGeometry(QtCore.QRect(210, 140, 271, 20))

        self.ShpOutputBox = QtWidgets.QLineEdit(Frame)
        self.ShpOutputBox.setGeometry(QtCore.QRect(210, 170, 271, 20))

        # Buttons
        self.BackButton = QtWidgets.QPushButton(Frame)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 149, 24))
        self.BackButton.setFont(font)

        self.HelpButton = QtWidgets.QPushButton(Frame)
        self.HelpButton.setGeometry(QtCore.QRect(720, 0, 149, 24))
        self.HelpButton.setFont(font)
        self.HelpButton.clicked.connect(self.getHelp)

        self.PolyBrowse = QtWidgets.QPushButton(Frame)
        self.PolyBrowse.setGeometry(QtCore.QRect(490, 50, 75, 21))
        self.PolyBrowse.setFont(font)
        self.PolyBrowse.clicked.connect(self.openFile)

        self.WebMapOutputBrowse = QtWidgets.QPushButton(Frame)
        self.WebMapOutputBrowse.setGeometry(QtCore.QRect(490, 140, 75, 21))
        self.WebMapOutputBrowse.setFont(font)
        self.WebMapOutputBrowse.clicked.connect(self.saveWebmap)

        self.ShpOutputBrowse = QtWidgets.QPushButton(Frame)
        self.ShpOutputBrowse.setGeometry(QtCore.QRect(490, 170, 75, 21))
        self.ShpOutputBrowse.setFont(font)
        self.ShpOutputBrowse.clicked.connect(self.saveShapefile)

        self.Execute = QtWidgets.QPushButton(Frame)
        self.Execute.setGeometry(QtCore.QRect(730, 180, 121, 41))
        self.Execute.setFont(font2)
        self.Execute.clicked.connect(self.returnedFunction)

        # Comboboxes
        self.DataInputSelection = QtWidgets.QComboBox(Frame)
        self.DataInputSelection.setGeometry(QtCore.QRect(760, 80, 91, 22))
        self.DataInputSelection.setFont(font)
        self.DataInputSelection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DataInputSelection.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow
            )
        self.DataInputSelection.addItem("Boundary")
        self.DataInputSelection.addItem("Region Name")
        self.DataInputSelection.currentIndexChanged.connect(
            self.methodSelection
            )

        self.AnalysisMethodSelection = QtWidgets.QComboBox(Frame)
        self.AnalysisMethodSelection.setGeometry(QtCore.QRect(760, 110,
                                                              91, 22))
        self.AnalysisMethodSelection.setFont(font)
        self.AnalysisMethodSelection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalysisMethodSelection.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow
            )
        self.AnalysisMethodSelection.addItem("Degree")
        self.AnalysisMethodSelection.addItem("Betweenness")
        self.AnalysisMethodSelection.addItem("Closeness")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def checkValid(self):
        if not self.ShpOutputBox.text():
            return "s", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Shapefile Output \
Folder must be specified.")
        elif (
                self.DataInputSelection.currentText() == "Boundary" and
                (
                    not self.PolyBoundaryBox.text() or
                    self.PolyBoundaryBox.text()[-4:] != ".shp"
                    )
                ):
            return "p", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Boundary data must \
be specified.")
        elif (
                self.DataInputSelection.currentText() == "Region Name"
                and not self.RegionNameBox.text()
                ):
            return "n", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Region name must \
be specified.")
        else:
            return "t", "t"

    def returnedFunction(self):
        signal, result = self.checkValid()
        validList = ["s", "p", "n"]
        if signal not in validList:
            try:
                funcs = {"Degree": self.degreeCentrality,
                         "Betweenness": self.betweennessCentrality,
                         "Closeness": self.closenessCentrality}
                function = funcs[self.AnalysisMethodSelection.currentText()]
                return function()
            except KeyError:
                return QtWidgets.QMessageBox.warning(None, "Error",
                                                     "Inputted name \
is not available in OSM database.")
            except TypeError:
                return QtWidgets.QMessageBox.warning(None, "Error",
                                                     "Geometry must \
be a polygon.")
            except:
                return QtWidgets.QMessageBox.warning(None, "Error",
                                                     "Unexpected Error")

    def findG(self):
        if self.DataInputSelection.currentText() == "Boundary":

            if len(self.TransportationModeBox.text()):
                G = bk.networkFromPolygon(self.PolyBoundaryBox.text(),
                                          self.TransportationModeBox.text())

                if isinstance(G, str):

                    return QtWidgets.QMessageBox.warning(
                        None, "Error",
                        "Polygon is not topologically valid.")

            else:
                G = bk.networkFromPolygon(self.PolyBoundaryBox.text())

                if isinstance(G, str):

                    return QtWidgets.QMessageBox.warning(
                        None, "Error",
                        "Polygon is not topologically valid.")

        elif self.DataInputSelection.currentText() == "Region Name":

            if (
                    len(self.TransportationModeBox.text()) and
                    len(self.RegionNumberBox.text())
                    ):
                G = bk.networkFromPlaceName(
                    self.RegionNameBox.text(),
                    networkType=self.TransportationModeBox.text(),
                    whichResult=self.RegionNumberBox.text()
                    )

            elif (len(self.TransportationModeBox.text()) and
                  not len(self.RegionNumberBox.text())):
                G = bk.networkFromPlaceName(
                    self.RegionNameBox.text(),
                    networkType=self.TransportationModeBox.text(),
                    )

            elif (not len(self.TransportationModeBox.text()) and
                  len(self.RegionNumberBox.text())):
                G = bk.networkFromPlaceName(
                    self.RegionNameBox.text(),
                    whichResult=self.RegionNumberBox.text()
                    )

            elif (not len(self.TransportationModeBox.text()) and
                  not len(self.RegionNumberBox.text())):
                G = bk.networkFromPlaceName(self.RegionNameBox.text())

        return G

    def degreeCentrality(self):
        G = self.findG()
        if len(self.WebMapBox.text()):
            returnmsg = bk.degreeCentrality(G, self.ShpOutputBox.text(),
                                            self.WebMapBox.text())
            if returnmsg == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')
        else:
            returnmsg2 = bk.degreeCentrality(G, self.ShpOutputBox.text())
            if returnmsg2 == "G":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

    def betweennessCentrality(self):
        G = self.findG()
        if len(self.WebMapBox.text()):
            returnmsg = bk.betweennessCentrality(G, self.ShpOutputBox.text(),
                                                 self.WebMapBox.text())
            if returnmsg == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')
        else:
            returnmsg2 = bk.betweennessCentrality(G, self.ShpOutputBox.text())
            if returnmsg2 == "G":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

    def closenessCentrality(self):
        G = self.findG()
        if len(self.WebMapBox.text()):
            returnmsg = bk.closenessCentrality(G, self.ShpOutputBox.text(),
                                               self.WebMapBox.text())
            if returnmsg == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')
        else:
            returnmsg2 = bk.closenessCentrality(G, self.ShpOutputBox.text())
            if returnmsg2 == "G":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

    def methodSelection(self):
        if self.DataInputSelection.currentText() == "Boundary":
            self.PolyBoundaryBox.setEnabled(True)
            self.PolyBrowse.setEnabled(True)
            self.RegionNameBox.setEnabled(False)
            self.RegionNumberBox.setEnabled(False)
        elif self.DataInputSelection.currentText() == "Region Name":
            self.PolyBoundaryBox.setEnabled(False)
            self.PolyBrowse.setEnabled(False)
            self.RegionNameBox.setEnabled(True)
            self.RegionNumberBox.setEnabled(True)

    def getHelp(self):
        QtWidgets.QMessageBox.about(None, "About", "* Input polygon boundary \
data should be in polygon type shapefile format \n\
* Region name should be checked first on \
https://nominatim.openstreetmap.org. \n\
* If there is no region name on the website search, region's network \
is unaccessible. \n\
* Choose the path where the road network of the area of interest and \
the result of the analysis is stored via 'Shapefile Output Folder' \n\
* Choose the path where the interactive map is stored via 'Interactive \
Map Output Path'. \n\
* Available transportation modes on OSM database are; \n\
        'drive' - get drivable public streets (but not service roads) \n\
        'drive_service' - get drivable public streets, including service \
roads \n\
        'walk' - get all streets and paths that pedestrians can use \
(this network type ignores one-way directionality) \n\
        'bike' - get all streets and paths that cyclists can use\n\
        'all' - download all (non-private) OSM streets and paths\n\
        'all_private' - download all OSM streets and paths, including \
private-access ones")

    def openFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName()
        self.PolyBoundaryBox.setText(str(name[0]))

    def saveWebmap(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, "Select Directory",
                                                     "interactivemap.html",
                                                     "HTML Files (*.html)")
        self.WebMapBox.setText(str(path[0]))

    def saveShapefile(self):
        path2 = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                           "Select Directory")
        self.ShpOutputBox.setText(path2)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Centrality"))
        self.BackButton.setText(_translate("Frame", "Back"))
        self.HelpButton.setText(_translate("Frame", "Help"))
        self.PolyBoundaryLabel.setText(_translate("Frame",
                                                  "Polygon Boundary of Area"))
        self.RegionNameLabel.setText(_translate("Frame",
                                                "Region Name/Result Number"))
        self.TransportationModeLabel.setText(_translate("Frame",
                                                        "Transportation Mode \
(*)"))
        self.WebMapLabel.setText(_translate("Frame",
                                            "Interactive Map \
Output Path (*)"))
        self.ShpOutputLabel.setText(_translate("Frame",
                                               "Shapefile Output Folder"))
        self.DataInputLabel.setText(_translate("Frame", "Data Input Method"))
        self.DataInputSelection.setItemText(0, _translate("Frame",
                                                          "Boundary"))
        self.DataInputSelection.setItemText(1, _translate("Frame",
                                                          "Region Name"))
        self.AnalysisMethodLabel.setText(_translate("Frame", "Analysis \
Method"))
        self.AnalysisMethodSelection.setItemText(0, _translate("Frame",
                                                               "Degree"))
        self.AnalysisMethodSelection.setItemText(1, _translate("Frame",
                                                               "Betweenness"))
        self.AnalysisMethodSelection.setItemText(2, _translate("Frame",
                                                               "Closeness"))
        self.PolyBrowse.setText(_translate("Frame", "Browse"))
        self.WebMapOutputBrowse.setText(_translate("Frame", "Browse"))
        self.ShpOutputBrowse.setText(_translate("Frame", "Browse"))
        self.Execute.setText(_translate("Frame", "Execute"))


class Accessibility(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(870, 253)
        Frame.setWindowIcon(QtGui.QIcon("interface.ico"))

        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setUnderline(False)

        font2 = QtGui.QFont()
        font2.setFamily("Palatino Linotype")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)

        self.verticalline = QtWidgets.QFrame(Frame)
        self.verticalline.setGeometry(QtCore.QRect(600, 0, 20, 252))
        self.verticalline.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalline.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Labels
        self.OriginsLabel = QtWidgets.QLabel(Frame)
        self.OriginsLabel.setGeometry(QtCore.QRect(20, 40, 181, 21))
        self.OriginsLabel.setFont(font)
        self.OriginsLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.DestinationsLabel = QtWidgets.QLabel(Frame)
        self.DestinationsLabel.setGeometry(QtCore.QRect(20, 70, 181, 21))
        self.DestinationsLabel.setFont(font)
        self.DestinationsLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.WeightLabel = QtWidgets.QLabel(Frame)
        self.WeightLabel.setGeometry(QtCore.QRect(20, 100, 181, 21))
        self.WeightLabel.setFont(font)
        self.WeightLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.TransportationModeLabel = QtWidgets.QLabel(Frame)
        self.TransportationModeLabel.setGeometry(QtCore.QRect(20, 130,
                                                              181, 21))
        self.TransportationModeLabel.setFont(font)
        self.TransportationModeLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.ThresholdLabel = QtWidgets.QLabel(Frame)
        self.ThresholdLabel.setGeometry(QtCore.QRect(20, 160, 181, 21))
        self.ThresholdLabel.setFont(font)
        self.ThresholdLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.WebMapLabel = QtWidgets.QLabel(Frame)
        self.WebMapLabel.setGeometry(QtCore.QRect(20, 190, 181, 21))
        self.WebMapLabel.setFont(font)
        self.WebMapLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.ShpOutputLabel = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel.setGeometry(QtCore.QRect(20, 220, 181, 21))
        self.ShpOutputLabel.setFont(font)
        self.ShpOutputLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        self.AnalysisMethodLabel = QtWidgets.QLabel(Frame)
        self.AnalysisMethodLabel.setGeometry(QtCore.QRect(640, 110, 111, 21))
        self.AnalysisMethodLabel.setFont(font)
        self.AnalysisMethodLabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
            )

        # TextBoxes
        self.OriginsBox = QtWidgets.QLineEdit(Frame)
        self.OriginsBox.setGeometry(QtCore.QRect(210, 40, 271, 20))

        self.DestinationsBox = QtWidgets.QLineEdit(Frame)
        self.DestinationsBox.setGeometry(QtCore.QRect(210, 70, 271, 20))

        self.WeightBox = QtWidgets.QLineEdit(Frame)
        self.WeightBox.setGeometry(QtCore.QRect(210, 100, 271, 20))

        self.TransportationModeBox = QtWidgets.QLineEdit(Frame)
        self.TransportationModeBox.setGeometry(QtCore.QRect(210, 130, 271, 20))

        self.ThresholdBox = QtWidgets.QLineEdit(Frame)
        self.ThresholdBox.setGeometry(QtCore.QRect(210, 160, 271, 20))
        self.ThresholdBox.setEnabled(False)

        self.WebMapBox = QtWidgets.QLineEdit(Frame)
        self.WebMapBox.setGeometry(QtCore.QRect(210, 190, 271, 20))

        self.ShpOutputBox = QtWidgets.QLineEdit(Frame)
        self.ShpOutputBox.setGeometry(QtCore.QRect(210, 220, 271, 20))

        # Buttons
        self.BackButton = QtWidgets.QPushButton(Frame)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 149, 24))
        self.BackButton.setFont(font)

        self.HelpButton = QtWidgets.QPushButton(Frame)
        self.HelpButton.setGeometry(QtCore.QRect(720, 0, 149, 24))
        self.HelpButton.setFont(font)
        self.HelpButton.clicked.connect(self.getHelp)

        self.OriginsBrowse = QtWidgets.QPushButton(Frame)
        self.OriginsBrowse.setGeometry(QtCore.QRect(490, 40, 75, 21))
        self.OriginsBrowse.setFont(font)
        self.OriginsBrowse.clicked.connect(self.openFile)

        self.DestinationsBrowse = QtWidgets.QPushButton(Frame)
        self.DestinationsBrowse.setGeometry(QtCore.QRect(490, 70, 75, 21))
        self.DestinationsBrowse.setFont(font)
        self.DestinationsBrowse.clicked.connect(self.openFile2)

        self.WebMapOutputBrowse = QtWidgets.QPushButton(Frame)
        self.WebMapOutputBrowse.setGeometry(QtCore.QRect(490, 190, 75, 21))
        self.WebMapOutputBrowse.setFont(font)
        self.WebMapOutputBrowse.clicked.connect(self.saveWebmap)

        self.ShpOutputBrowse = QtWidgets.QPushButton(Frame)
        self.ShpOutputBrowse.setGeometry(QtCore.QRect(490, 220, 75, 21))
        self.ShpOutputBrowse.setFont(font)
        self.ShpOutputBrowse.clicked.connect(self.saveShapefile)

        self.Execute = QtWidgets.QPushButton(Frame)
        self.Execute.setGeometry(QtCore.QRect(730, 200, 121, 41))
        self.Execute.setFont(font2)
        self.Execute.clicked.connect(self.returnedFunction)

        # SelectionBoxes
        self.AnalysisMethodSelection = QtWidgets.QComboBox(Frame)
        self.AnalysisMethodSelection.setGeometry(QtCore.QRect(760, 110,
                                                              91, 22))
        self.AnalysisMethodSelection.setFont(font)
        self.AnalysisMethodSelection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalysisMethodSelection.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow
            )
        self.AnalysisMethodSelection.addItem("Potential")
        self.AnalysisMethodSelection.addItem("Daily")
        self.AnalysisMethodSelection.currentIndexChanged.connect(
            self.enableSelection
            )
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def checkValid(self):
        if not self.ShpOutputBox.text():
            return "s", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Shapefile Output \
Folder must be specified.")
        elif (not self.OriginsBox.text() or
              self.OriginsBox.text()[-4:] != ".shp"):
            return "o", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Origins must \
be specified.")
        elif (not self.DestinationsBox.text() or
              self.DestinationsBox.text()[-4:] != ".shp"):
            return "d", QtWidgets.QMessageBox.warning(None, "Error",
                                                      "Destinations must \
be specified.")
        else:
            return "t", "t"

    def returnedFunction(self):
        signal, result = self.checkValid()
        validList = ["s", "o", "d"]
        if signal not in validList:
            try:
                funcs = {"Potential": self.potentialAccessibility,
                         "Daily": self.dailyAccessibility}
                function = funcs[self.AnalysisMethodSelection.currentText()]
                return function()
            except:
                raise

    def origdest(self):
        if len(self.TransportationModeBox.text()):
            route_geom, nodes, G_proj, o, d = bk.origindestination(
                self.OriginsBox.text(),
                self.DestinationsBox.text(),
                networkType=self.TransportationModeBox.text()
                )

        else:
            route_geom, nodes, G_proj, o, d = bk.origindestination(
                self.OriginsBox.text(),
                self.DestinationsBox.text()
                )

        return route_geom, nodes, G_proj, o, d

    def potentialAccessibility(self):
        route_geom, nodes, G_proj, o, d = self.origdest()

        if (
                len(self.WebMapBox.text()) and
                len(self.WeightBox.text())
                ):
            returnmsg = bk.potentialAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                self.WeightBox.text(),
                self.WebMapBox.text()
                )

            if returnmsg == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg2 = bk.potentialAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                1, self.WebMapBox.text()
                )

            if returnmsg2 == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (not len(self.WebMapBox.text()) and
              len(self.WeightBox.text())):
            returnmsg3 = bk.potentialAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                weight=self.WeightBox.text()
                )

            if returnmsg3 == "P":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

        elif (not len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg4 = bk.potentialAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text()
                )

            if returnmsg4 == "P":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

    def dailyAccessibility(self):
        route_geom, nodes, G_proj, o, d = self.origdest()

        if (
                len(self.ThresholdBox.text()) and
                len(self.WebMapBox.text()) and
                len(self.WeightBox.text())
                ):
            returnmsg = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                self.WeightBox.text(),
                self.ThresholdBox.text(),
                self.WebMapBox.text()
                )

            if returnmsg == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (len(self.ThresholdBox.text()) and
              not len(self.WebMapBox.text()) == 0 and
              len(self.WeightBox.text())):
            returnmsg2 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                weight=self.WeightBox.text(),
                threshold=self.ThresholdBox.text()
                )

            if returnmsg2 == "D":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

        elif (len(self.ThresholdBox.text()) and
              len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg3 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                1, self.ThresholdBox.text(),
                self.WebMapBox.text()
                )

            if returnmsg3 == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (not len(self.ThresholdBox.text()) and
              len(self.WebMapBox.text()) and
              len(self.WeightBox.text())):
            returnmsg4 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                self.WeightBox.text(), 3000,
                self.WebMapBox.text()
                )

            if returnmsg4 == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (not len(self.ThresholdBox.text()) and
              len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg5 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(), 1,
                3000, self.WebMapBox.text()
                )

            if returnmsg5 == "I":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 via interactive map successfully')

        elif (not len(self.ThresholdBox.text()) and
              not len(self.WebMapBox.text()) and
              len(self.WeightBox.text())):
            returnmsg6 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                weight=self.WeightBox.text(),
                threshold=3000
                )

            if returnmsg6 == "D":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

        elif (len(self.ThresholdBox.text()) and
              not len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg7 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text(),
                1, threshold=self.ThresholdBox.text()
                )

            if returnmsg7 == "D":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

        elif (not len(self.ThresholdBox.text()) and
              not len(self.WebMapBox.text()) and
              not len(self.WeightBox.text())):
            returnmsg8 = bk.dailyAccessibility(
                route_geom, nodes, G_proj, o, d,
                self.ShpOutputBox.text()
                )

            if returnmsg8 == "D":
                return QtWidgets.QMessageBox.information(None,
                                                         'Done!',
                                                         'Operation performed\
 successfully')

    def enableSelection(self):
        if self.AnalysisMethodSelection.currentText() == "Potential":
            self.ThresholdBox.setEnabled(False)
        elif self.AnalysisMethodSelection.currentText() == "Daily":
            self.ThresholdBox.setEnabled(True)

    def getHelp(self):
        QtWidgets.QMessageBox.about(None, "About", "* Input origins \
and destinations data should be in point type shapefile format \n\
* Weight column name of destinations must be entered as text, \
otherwise default value 1 is used in calculations \n\
* Choose the path where the road network of the area of interest and \
the result of the analysis is stored via 'Shapefile Output Folder' \n\
* Choose the path where the interactive map is stored via 'Interactive \
Map Output Path'. \n\
* Available transportation modes on OSM database are;\n\
        'drive' - get drivable public streets (but not service roads)\n\
        'drive_service' - get drivable public streets, including service \
roads\n\
        'walk' - get all streets and paths that pedestrians can use (this \
network type ignores one-way directionality)\n\
        'bike' - get all streets and paths that cyclists can use\n\
        'all' - download all (non-private) OSM streets and paths\n\
        'all_private' - download all OSM streets and paths, including \
private-access ones")

    def openFile(self):
        orig = QtWidgets.QFileDialog.getOpenFileName()
        orig_text = str(orig[0])
        self.OriginsBox.setText(orig_text)

    def openFile2(self):
        dest = QtWidgets.QFileDialog.getOpenFileName()
        dest_text = str(dest[0])
        self.DestinationsBox.setText(dest_text)

    def saveWebmap(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, "Select Directory",
                                                     "interactivemap.html",
                                                     "HTML Files (*.html)")
        self.WebMapBox.setText(str(path[0]))

    def saveShapefile(self):
        path2 = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                           "Select Directory")
        self.ShpOutputBox.setText(path2)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Accessibility"))
        self.BackButton.setText(_translate("Frame", "Back"))
        self.HelpButton.setText(_translate("Frame", "Help"))
        self.OriginsLabel.setText(_translate("Frame", "Origins"))
        self.DestinationsLabel.setText(_translate("Frame", "Destinations"))
        self.WeightLabel.setText(_translate("Frame", "Weight Column (*)"))
        self.TransportationModeLabel.setText(_translate("Frame",
                                                        "Transportation Mode \
(*)"))
        self.ThresholdLabel.setText(_translate("Frame",
                                               "Distance Threshold (m)"))
        self.WebMapLabel.setText(_translate("Frame",
                                            "Interactive Map Output Path (*)"))
        self.ShpOutputLabel.setText(_translate("Frame",
                                               "Shapefile Output Folder"))
        self.AnalysisMethodLabel.setText(_translate("Frame",
                                                    "Analysis Method"))
        self.AnalysisMethodSelection.setItemText(0, _translate("Frame",
                                                               "Potential"))
        self.AnalysisMethodSelection.setItemText(1, _translate("Frame",
                                                               "Daily"))
        self.OriginsBrowse.setText(_translate("Frame", "Browse"))
        self.DestinationsBrowse.setText(_translate("Frame", "Browse"))
        self.WebMapOutputBrowse.setText(_translate("Frame", "Browse"))
        self.ShpOutputBrowse.setText(_translate("Frame", "Browse"))
        self.Execute.setText(_translate("Frame", "Execute"))


def main():

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("SATRAP")
    mywindow = Controller()
    mywindow.open_main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
