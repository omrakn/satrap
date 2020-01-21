import sys
import backend as bk
from PyQt5 import QtGui, QtCore, QtWidgets

class Controller:
    
    def __init__(self):
        self.mainwindow = MainAppWindow()
        self.getstudyarea = GsaWindow()
        self.centrality = CentralityWindow()
        self.accessibility = AccessibilityWindow()
    
    def open_main(self):
        self.mainwindow.switch_window1.connect(self.open_gsa)
        self.mainwindow.switch_window2.connect(self.open_cent)
        self.mainwindow.switch_window3.connect(self.open_access)
        self.getstudyarea.hide()
        self.centrality.hide()
        self.accessibility.hide()
        self.mainwindow.show()
        
    def open_gsa(self):
        self.getstudyarea.switch_window.connect(self.open_main)
        self.mainwindow.hide()
        self.getstudyarea.show()
        
    def open_cent(self):
        self.centrality.switch_window.connect(self.open_main)
        self.mainwindow.hide()
        self.centrality.show()
            
    def open_access(self):
        self.accessibility.switch_window.connect(self.open_main)
        self.mainwindow.hide()
        self.accessibility.show()
        
class MainAppWindow(QtWidgets.QFrame):
    
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    
    def __init__(self):
        super(MainAppWindow, self).__init__()
        
        self.mainwindow = MainWindow()
        self.mainwindow.setupUi(self)
        self.mainwindow.GetStudyAreaButton.clicked.connect(self.open_gsa_handler)
        self.mainwindow.CentralityAnalysisButton.clicked.connect(self.open_cent_handler)
        self.mainwindow.AccessibilityAnalysisButton.clicked.connect(self.open_access_handler)
        
    def open_gsa_handler(self):
        self.switch_window1.emit()
        
    def open_cent_handler(self):
        self.switch_window2.emit()
        
    def open_access_handler(self):
        self.switch_window3.emit()
        
class GsaWindow(QtWidgets.QFrame):
    
    switch_window = QtCore.pyqtSignal()
    
    def __init__(self):
        super(GsaWindow,self).__init__()
        self.getstudyarea = GetStudyArea()
        self.getstudyarea.setupUi(self)
        self.getstudyarea.BackButton.clicked.connect(self.open_main_handler)

    def open_main_handler(self):
        self.switch_window.emit()

class CentralityWindow(QtWidgets.QFrame):
    
    switch_window = QtCore.pyqtSignal()
    
    def __init__(self):
        super(CentralityWindow,self).__init__()
        self.centrality = Centrality()
        self.centrality.setupUi(self)
        self.centrality.BackButton.clicked.connect(self.open_main_handler)

    def open_main_handler(self):
        self.switch_window.emit()
        
class AccessibilityWindow(QtWidgets.QFrame):
    
    switch_window = QtCore.pyqtSignal()
    
    def __init__(self):
        super(AccessibilityWindow,self).__init__()
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ChooseAnalysisLabel.setPalette(palette)
        self.ChooseAnalysisLabel.setFont(font2)
        self.ChooseAnalysisLabel.setAutoFillBackground(False)
        self.ChooseAnalysisLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Buttons
        self.GetStudyAreaButton = QtWidgets.QPushButton(MainFrame)
        self.GetStudyAreaButton.setGeometry(QtCore.QRect(0, 0, 161, 31))
        self.GetStudyAreaButton.setFont(font)
        
        self.CentralityAnalysisButton = QtWidgets.QPushButton(MainFrame)
        self.CentralityAnalysisButton.setGeometry(QtCore.QRect(350, 100, 181, 31))
        self.CentralityAnalysisButton.setFont(font3)
        
        self.AccessibilityAnalysisButton = QtWidgets.QPushButton(MainFrame)
        self.AccessibilityAnalysisButton.setGeometry(QtCore.QRect(350, 140, 181, 31))
        self.AccessibilityAnalysisButton.setFont(font3)
        
        self.retranslateUi(MainFrame)
        QtCore.QMetaObject.connectSlotsByName(MainFrame)

    def retranslateUi(self, MainFrame):
        _translate = QtCore.QCoreApplication.translate
        MainFrame.setWindowTitle(_translate("MainFrame", "SATRAP"))
        self.ChooseAnalysisLabel.setText(_translate("MainFrame", "Choose Analysis"))
        self.GetStudyAreaButton.setText(_translate("MainFrame", "Get Study Area"))
        self.CentralityAnalysisButton.setText(_translate("MainFrame", "Centrality Analysis"))
        self.AccessibilityAnalysisButton.setText(_translate("MainFrame", "Accessibility Analysis"))
        
class GetStudyArea(object):
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
        
        # Labels
        self.RegionNameLabel = QtWidgets.QLabel(Frame)
        self.RegionNameLabel.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.RegionNameLabel.setFont(font)
        self.RegionNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        self.ShpOutputLabel = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel.setGeometry(QtCore.QRect(20, 110, 181, 21))
        self.ShpOutputLabel.setFont(font)
        self.ShpOutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        self.ShpOutputLabel2 = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel2.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.ShpOutputLabel2.setFont(font)
        self.ShpOutputLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        # TextBoxes
        self.RegionNameBox = QtWidgets.QLineEdit(Frame)
        self.RegionNameBox.setGeometry(QtCore.QRect(210, 80, 221, 20))

        self.RegionNumberBox = QtWidgets.QLineEdit(Frame)
        self.RegionNumberBox.setGeometry(QtCore.QRect(440, 80, 41, 20))

        self.ShpOutputBox1 = QtWidgets.QLineEdit(Frame)
        self.ShpOutputBox1.setGeometry(QtCore.QRect(210, 110, 271, 20))
        
        self.ShpOutputBox2 = QtWidgets.QLineEdit(Frame)
        self.ShpOutputBox2.setGeometry(QtCore.QRect(210, 140, 271, 20))

        # Buttons
        self.BackButton = QtWidgets.QPushButton(Frame)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 149, 24))
        self.BackButton.setFont(font)
        
        self.HelpButton = QtWidgets.QPushButton(Frame)
        self.HelpButton.setGeometry(QtCore.QRect(720, 0, 149, 24))
        self.HelpButton.setFont(font)
        self.HelpButton.clicked.connect(self.getHelp)
        
        self.ShpOutputBrowse = QtWidgets.QPushButton(Frame)
        self.ShpOutputBrowse.setGeometry(QtCore.QRect(490, 110, 75, 21))
        self.ShpOutputBrowse.setFont(font)
        self.ShpOutputBrowse.clicked.connect(self.saveShapefile)
        
        self.ExecuteButton = QtWidgets.QPushButton(Frame)
        self.ExecuteButton.setGeometry(QtCore.QRect(730, 180, 121, 41))
        self.ExecuteButton.setFont(font2)
        self.ExecuteButton.clicked.connect(self.getPoly)
        
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        
    def getHelp(self):
        QtWidgets.QMessageBox.about(None, "About", "* Region name should be checked first on https://nominatim.openstreetmap.org. \n\
* If there is no region name on the website search, region's network is unaccessible.")
        
    def getPoly(self):
        try:
            if len(self.RegionNumberBox.text()) > 0:
                bk.getPolyData(self.RegionNameBox.text(), self.ShpOutputBox1.text(), self.ShpOutputBox2.text(), whichResult=self.RegionNumberBox.text())
            elif len(self.RegionNumberBox.text()) == 0:
                bk.getPolyData(self.RegionNameBox.text(), self.ShpOutputBox1.text(), self.ShpOutputBox2.text())
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Valid Output Location should be entered")
        except ValueError:
            QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Valid Region Name/Number should be entered")
        
    def saveShapefile(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        self.ShpOutputBox1.setText(path)
        
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Get Study Area"))
        self.ExecuteButton.setText(_translate("Frame", "Execute"))
        self.ShpOutputLabel2.setText(_translate("Frame", "Shapefile Output Name"))
        self.RegionNameLabel.setText(_translate("Frame", "Region Name/Result Number"))
        self.HelpButton.setText(_translate("Frame", "Help"))
        self.BackButton.setText(_translate("Frame", "Back"))
        self.ShpOutputLabel.setText(_translate("Frame", "Shapefile Output Folder"))
        self.ShpOutputBrowse.setText(_translate("Frame", "Browse"))

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
        self.PolyBoundaryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.RegionNameLabel = QtWidgets.QLabel(Frame)
        self.RegionNameLabel.setGeometry(QtCore.QRect(20, 80, 181, 21))
        self.RegionNameLabel.setFont(font)
        self.RegionNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.TransportationModeLabel = QtWidgets.QLabel(Frame)
        self.TransportationModeLabel.setGeometry(QtCore.QRect(20, 110, 181, 21))
        self.TransportationModeLabel.setFont(font)
        self.TransportationModeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        self.WebMapLabel = QtWidgets.QLabel(Frame)
        self.WebMapLabel.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.WebMapLabel.setFont(font)
        self.WebMapLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        self.ShpOutputLabel = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel.setGeometry(QtCore.QRect(20, 170, 181, 21))
        self.ShpOutputLabel.setFont(font)
        self.ShpOutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.DataInputLabel = QtWidgets.QLabel(Frame)
        self.DataInputLabel.setGeometry(QtCore.QRect(640, 80, 111, 21))
        self.DataInputLabel.setFont(font)
        self.DataInputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.AnalysisMethodLabel = QtWidgets.QLabel(Frame)
        self.AnalysisMethodLabel.setGeometry(QtCore.QRect(640, 110, 111, 21))
        self.AnalysisMethodLabel.setFont(font)
        self.AnalysisMethodLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
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
        self.DataInputSelection.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.DataInputSelection.addItem("Boundary")
        self.DataInputSelection.addItem("Region Name")
        self.DataInputSelection.currentIndexChanged.connect(self.methodSelection)
        
        self.AnalysisMethodSelection = QtWidgets.QComboBox(Frame)
        self.AnalysisMethodSelection.setGeometry(QtCore.QRect(760, 110, 91, 22))
        self.AnalysisMethodSelection.setFont(font)
        self.AnalysisMethodSelection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalysisMethodSelection.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.AnalysisMethodSelection.addItem("Degree")
        self.AnalysisMethodSelection.addItem("Betweenness")
        self.AnalysisMethodSelection.addItem("Closeness")
        
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def getHelp(self):
        QtWidgets.QMessageBox.about(None, "About", "* Input polygon boundary data should be in polygon type shapefile format \n\
* Region name should be checked first on https://nominatim.openstreetmap.org. \n\
* If there is no region name on the website search, region's network is unaccessible. \n\
* Choose the path where the road network of the area of interest and the result of the analysis is stored in shapefile format via 'Shapefile Output Folder' \n\
* Choose the path where the webmap that is generated by the result of analysis is stored via 'Webmap Output Path'. \n\
* Available transportation modes on OSM database are;\n\
        'drive' - get drivable public streets (but not service roads)\n\
        'drive_service' - get drivable public streets, including service roads\n\
        'walk' - get all streets and paths that pedestrians can use (this network type ignores one-way directionality)\n\
        'bike' - get all streets and paths that cyclists can use\n\
        'all' - download all (non-private) OSM streets and paths\n\
        'all_private' - download all OSM streets and paths, including private-access ones")
        
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
    
    def returnedFunction(self):
        try:
            funcs = {"Degree": self.degreeCentrality,
                     "Betweenness": self.betweennessCentrality,
                     "Closeness": self.closenessCentrality}
            function = funcs[self.AnalysisMethodSelection.currentText()]
            return function()
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Valid output path should be entered")
        except:
            if len(self.ShpOutputBox.text()) == 0:
                QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Enter output path.")
            else:
                QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Region name / Polygon boundary should be entered in valid format.")

    def degreeCentrality(self):
        print("Calculating Degree Centrality..")
        G = self.findG()
        if len(self.WebMapBox.text()) > 0:
            bk.degreeCentrality(G, self.ShpOutputBox.text(), self.WebMapBox.text())
        else:
            bk.degreeCentrality(G, self.ShpOutputBox.text())
            
    def betweennessCentrality(self):
        print("Calculating Betweenness..")
        G = self.findG()
        if len(self.WebMapBox.text()) > 0:
            bk.betweennessCentrality(G, self.ShpOutputBox.text(), self.WebMapBox.text())
        else:
            bk.betweennessCentrality(G, self.ShpOutputBox.text())
        
    def closenessCentrality(self):
        print("Calculating Closeness..")
        G = self.findG()
        if len(self.WebMapBox.text()) > 0:
            bk.closenessCentrality(G, self.ShpOutputBox.text(), self.WebMapBox.text())
        else:
            bk.closenessCentrality(G, self.ShpOutputBox.text())

    def openFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName()
        self.PolyBoundaryBox.setText(str(name[0]))

    def saveWebmap(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, "Select Directory", "webmap.html", "HTML Files (*.html)")
        self.WebMapBox.setText(str(path[0]))
        
    def saveShapefile(self):
        path2 = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        self.ShpOutputBox.setText(path2)

    def findG(self):
        if self.DataInputSelection.currentText() == "Boundary":
            if len(self.TransportationModeBox.text()) > 0:
                G = bk.networkFromPolygon(self.PolyBoundaryBox.text(), self.TransportationModeBox.text())
            else:
                G = bk.networkFromPolygon(self.PolyBoundaryBox.text())
        elif self.DataInputSelection.currentText() == "Region Name":
            if len(self.TransportationModeBox.text()) > 0 and len(self.RegionNumberBox.text()) > 0:
                G = bk.networkFromPlaceName(self.RegionNameBox.text(), networkType=self.TransportationModeBox.text(),
                                            whichResult=self.RegionNumberBox.text())
            elif len(self.TransportationModeBox.text()) > 0 and len(self.RegionNumberBox.text()) == 0:
                G = bk.networkFromPlaceName(self.RegionNameBox.text(), networkType=self.TransportationModeBox.text())
            elif len(self.TransportationModeBox.text()) == 0 and len(self.RegionNumberBox.text()) > 0:
                G = bk.networkFromPlaceName(self.RegionNameBox.text(), whichResult=self.RegionNumberBox.text())
            else:
                G = bk.networkFromPlaceName(self.RegionNameBox.text())
        return G
            
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Centrality"))
        self.TransportationModeLabel.setText(_translate("Frame", "Transportation Mode (Optional)"))
        self.ShpOutputBrowse.setText(_translate("Frame", "Browse"))
        self.WebMapLabel.setText(_translate("Frame", "Webmap Output Path (Optional)"))
        self.Execute.setText(_translate("Frame", "Execute"))
        self.PolyBrowse.setText(_translate("Frame", "Browse"))
        self.DataInputSelection.setItemText(0, _translate("Frame", "Boundary"))
        self.DataInputSelection.setItemText(1, _translate("Frame", "Region Name"))
        self.HelpButton.setText(_translate("Frame", "Help"))
        self.AnalysisMethodSelection.setItemText(0, _translate("Frame", "Degree"))
        self.AnalysisMethodSelection.setItemText(1, _translate("Frame", "Betweenness"))
        self.AnalysisMethodSelection.setItemText(2, _translate("Frame", "Closeness"))
        self.PolyBoundaryLabel.setText(_translate("Frame", "Polygon Boundary of Area"))
        self.WebMapOutputBrowse.setText(_translate("Frame", "Browse"))
        self.ShpOutputLabel.setText(_translate("Frame", "Shapefile Output Folder"))
        self.AnalysisMethodLabel.setText(_translate("Frame", "Analysis Method"))
        self.DataInputLabel.setText(_translate("Frame", "Data Input Method"))
        self.RegionNameLabel.setText(_translate("Frame", "Region Name/Result Number"))
        self.BackButton.setText(_translate("Frame", "Back"))
        
class Accessibility(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(870, 230)
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
        self.verticalline.setGeometry(QtCore.QRect(600, 0, 20, 231))
        self.verticalline.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalline.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        # Labels
        self.OriginsLabel = QtWidgets.QLabel(Frame)
        self.OriginsLabel.setGeometry(QtCore.QRect(20, 40, 181, 21))
        self.OriginsLabel.setFont(font)
        self.OriginsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        self.DestinationsLabel = QtWidgets.QLabel(Frame)
        self.DestinationsLabel.setGeometry(QtCore.QRect(20, 70, 181, 21))
        self.DestinationsLabel.setFont(font)
        self.DestinationsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.TransportationModeLabel = QtWidgets.QLabel(Frame)
        self.TransportationModeLabel.setGeometry(QtCore.QRect(20, 100, 181, 21))
        self.TransportationModeLabel.setFont(font)
        self.TransportationModeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.ThresholdLabel = QtWidgets.QLabel(Frame)
        self.ThresholdLabel.setGeometry(QtCore.QRect(20, 130, 181, 21))
        self.ThresholdLabel.setFont(font)
        self.ThresholdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.WebMapLabel = QtWidgets.QLabel(Frame)
        self.WebMapLabel.setGeometry(QtCore.QRect(20, 160, 181, 21))
        self.WebMapLabel.setFont(font)
        self.WebMapLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.ShpOutputLabel = QtWidgets.QLabel(Frame)
        self.ShpOutputLabel.setGeometry(QtCore.QRect(20, 190, 181, 21))
        self.ShpOutputLabel.setFont(font)
        self.ShpOutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.AnalysisMethodLabel = QtWidgets.QLabel(Frame)
        self.AnalysisMethodLabel.setGeometry(QtCore.QRect(640, 100, 111, 21))
        self.AnalysisMethodLabel.setFont(font)
        self.AnalysisMethodLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        # TextBoxes
        self.OriginsBox = QtWidgets.QLineEdit(Frame)
        self.OriginsBox.setGeometry(QtCore.QRect(210, 40, 271, 20))
        
        self.DestinationsBox = QtWidgets.QLineEdit(Frame)
        self.DestinationsBox.setGeometry(QtCore.QRect(210, 70, 271, 20))

        self.TransportationModeBox = QtWidgets.QLineEdit(Frame)
        self.TransportationModeBox.setGeometry(QtCore.QRect(210, 100, 271, 20))
        
        self.ThresholdBox = QtWidgets.QLineEdit(Frame)
        self.ThresholdBox.setGeometry(QtCore.QRect(210, 130, 271, 20))
        self.ThresholdBox.setEnabled(False)
        
        self.WebMapBox = QtWidgets.QLineEdit(Frame)
        self.WebMapBox.setGeometry(QtCore.QRect(210, 160, 271, 20))
        
        self.ShpOutputBox = QtWidgets.QLineEdit(Frame)
        self.ShpOutputBox.setGeometry(QtCore.QRect(210, 190, 271, 20))
        
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
        self.WebMapOutputBrowse.setGeometry(QtCore.QRect(490, 160, 75, 21))
        self.WebMapOutputBrowse.setFont(font)
        self.WebMapOutputBrowse.clicked.connect(self.saveWebmap)
        
        self.ShpOutputBrowse = QtWidgets.QPushButton(Frame)
        self.ShpOutputBrowse.setGeometry(QtCore.QRect(490, 190, 75, 21))
        self.ShpOutputBrowse.setFont(font)
        self.ShpOutputBrowse.clicked.connect(self.saveShapefile)
        
        self.Execute = QtWidgets.QPushButton(Frame)
        self.Execute.setGeometry(QtCore.QRect(730, 180, 121, 41))
        self.Execute.setFont(font2)
        self.Execute.clicked.connect(self.returnedFunction)
        
        # SelectionBoxes
        self.AnalysisMethodSelection = QtWidgets.QComboBox(Frame)
        self.AnalysisMethodSelection.setGeometry(QtCore.QRect(760, 100, 91, 22))
        self.AnalysisMethodSelection.setFont(font)
        self.AnalysisMethodSelection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalysisMethodSelection.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.AnalysisMethodSelection.addItem("Potential")
        self.AnalysisMethodSelection.addItem("Daily")
        self.AnalysisMethodSelection.currentIndexChanged.connect(self.enableSelection)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def getHelp(self):
        QtWidgets.QMessageBox.about(None, "About", "* Input origins and destinations data should be in point type shapefile format \n\
* Choose the path where the road network of the area of interest and the result of the analysis is stored in shapefile format via 'Shapefile Output Folder' \n\
* Choose the path where the webmap that is generated by the result of analysis is stored via 'Webmap Output Path'. \n\
* Available transportation modes on OSM database are;\n\
        'drive' - get drivable public streets (but not service roads)\n\
        'drive_service' - get drivable public streets, including service roads\n\
        'walk' - get all streets and paths that pedestrians can use (this network type ignores one-way directionality)\n\
        'bike' - get all streets and paths that cyclists can use\n\
        'all' - download all (non-private) OSM streets and paths\n\
        'all_private' - download all OSM streets and paths, including private-access ones")
        
    def enableSelection(self):
        if self.AnalysisMethodSelection.currentText() == "Potential":
            self.ThresholdBox.setEnabled(False)
        elif self.AnalysisMethodSelection.currentText() == "Daily":
            self.ThresholdBox.setEnabled(True)

    def returnedFunction(self):
        try:
            funcs = {"Potential": self.potentialAccessibility,
                     "Daily": self.dailyAccessibility}
            function = funcs[self.AnalysisMethodSelection.currentText()]
            return function()
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Valid output path should be entered")
        except:
            if len(self.ShpOutputBox.text()) == 0:
                QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Enter output path.")
            else:
                QtWidgets.QMessageBox.critical(None, "Error", "ERROR: Origins and destinations should be entered in valid format.")

    def origdest(self):
        if len(self.TransportationModeBox.text()) > 0:
            route_geom, nodes, G_proj = bk.origindestination(self.OriginsBox.text(), self.DestinationsBox.text(), 
            self.TransportationModeBox.text())
        else:
            route_geom, nodes, G_proj = bk.origindestination(self.OriginsBox.text(), self.DestinationsBox.text())
        return route_geom, nodes, G_proj
    
    def potentialAccessibility(self):
        route_geom, nodes, G_proj = self.origdest()
        if len(self.WebMapBox.text()) > 0:
            bk.potentialAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text(),
                                      self.WebMapBox.text())
        else:
            bk.potentialAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text())
            
    def dailyAccessibility(self):
        route_geom, nodes, G_proj = self.origdest()
        if len(self.ThresholdBox.text()) > 0 and len(self.WebMapBox.text()) > 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text(), self.ThresholdBox.text(),
                                  self.WebMapBox.text())
        elif len(self.ThresholdBox.text()) > 0 and len(self.WebMapBox.text()) > 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text(), self.ThresholdBox.text())
        elif len(self.ThresholdBox.text()) == 0 and len(self.WebMapBox.text()) == 0:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text(), 3000,
                                  self.WebMapBox.text())
        else:
            bk.dailyAccessibility(route_geom, nodes, G_proj, self.ShpOutputBox.text())
            
    def openFile(self):
        orig = QtWidgets.QFileDialog.getOpenFileName()
        orig_text = str(orig[0])
        self.OriginsBox.setText(orig_text)
        
    def openFile2(self):
        dest = QtWidgets.QFileDialog.getOpenFileName()
        dest_text = str(dest[0])
        self.DestinationsBox.setText(dest_text)
        
    def saveWebmap(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, "Select Directory", "webmap.html", "HTML Files (*.html)")
        self.WebMapBox.setText(str(path[0]))
        
    def saveShapefile(self):
        path2 = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        self.ShpOutputBox.setText(path2)
        
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Accessibility"))
        self.Execute.setText(_translate("Frame", "Execute"))
        self.DestinationsLabel.setText(_translate("Frame", "Destinations"))
        self.WebMapOutputBrowse.setText(_translate("Frame", "Browse"))
        self.AnalysisMethodLabel.setText(_translate("Frame", "Analysis Method"))
        self.OriginsLabel.setText(_translate("Frame", "Origins"))
        self.AnalysisMethodSelection.setItemText(0, _translate("Frame", "Potential"))
        self.AnalysisMethodSelection.setItemText(1, _translate("Frame", "Daily"))
        self.TransportationModeLabel.setText(_translate("Frame", "Transportation Mode (Optional)"))
        self.WebMapLabel.setText(_translate("Frame", "Webmap Output Path (Optional)"))
        self.ShpOutputBrowse.setText(_translate("Frame", "Browse"))
        self.ThresholdLabel.setText(_translate("Frame", "Distance Threshold (m)"))
        self.BackButton.setText(_translate("Frame", "Back"))
        self.DestinationsBrowse.setText(_translate("Frame", "Browse"))
        self.OriginsBrowse.setText(_translate("Frame", "Browse"))
        self.ShpOutputLabel.setText(_translate("Frame", "Shapefile Output Folder"))
        self.HelpButton.setText(_translate("Frame", "Help"))
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("SATRAP")
    mywindow = Controller()
    mywindow.open_main()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()