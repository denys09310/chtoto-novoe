from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui import Ui_MainWindow
import os 

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filenames = None
        self.image = None
        self.ui.floder_btn.clicked.connect(self.choose_floder)

    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith('.png') or filename.endswith(".jpg") or filename.endswith("jpeg"):
                images.append(filename)
        self.ui.image_list.clear()
        self.ui.image_list.addItems(images)

        self.ui.image_list.addItems(images)

    def choose_floder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("ERROR kfvjbhafiaiwFDGladfjsdkajfjljgfjgdsabjcvfhjwvDFKJGEjkgdsJKFd;uoidufsdhukfsdIFL:Y;yiosdFuDFS;ugidfs;oufsd:UfsDHLIfS:HKFSH:I;oiysdfugioDSFg;usdfg;usDFiug;dsfU:GIDSFGUo;sdF:HUf:UHdf:HUd;hFhu;xcjzhjchisdfheuwfguisuGIGUISDHUUGFEWGYUDYUFEUWFVEUFyufGUIAIUGHGugifeauoigruhrifetven")
            message.exec_()

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

