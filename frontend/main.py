from mainwindow import Ui_MainWindow
from netw.hamming import HammingNetw
from utils.img2matrix import ImageConvertor
from utils.utils import normalize
from netw.parser import from_array

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.actionAdd_figure, SIGNAL("triggered()"), self.add_figure)
        self.connect(self.actionRecognize_figure, SIGNAL("triggered()"), self.recognize_figure)
        self.connect(self.trainButton, SIGNAL("pressed()"), self.train)
        self.connect(self.imagesListWidget, SIGNAL("currentRowChanged(int)"), self.show_image)
        self.figures = []

    def add_figure(self):
        pathes = QFileDialog.getOpenFileNames(self, self.tr("Select images"), QDir.currentPath(), "Images (*.png *.xpm *.jpg)")
        for path in pathes:
            self.figures.append(path)
            item = QListWidgetItem(path)
            item.setData(Qt.UserRole, QVariant(len(self.figures)-1))
            self.imagesListWidget.addItem(item)

    def train(self):
        if len(self.figures)>0:
            w,h = 0,0
            ic = ImageConvertor(str(self.figures[0]))
            arr = ic.get_array()
            w = len(arr[0])
            h = len(arr[1])
            self.nw = HammingNetw(w*h, len(self.figures))
            for figure in self.figures:
                ic = ImageConvertor(str(figure))
                array = from_array(ic.get_array(), '*')
                self.nw.train(normalize(array))
            self.statusBar().showMessage("Network trained")

    def recognize_figure(self):
        path = QFileDialog.getOpenFileName(self, self.tr("Open figure to recognize"), QDir.currentPath(), "Images (*.png *.xpm *.jpg)")
        if path:
            self.__show_img(self.recognizeImageLabel, path)
            self.__start_recognition(path)

    def __start_recognition(self, path):
        ic = ImageConvertor(str(path))
        array = from_array(ic.get_array(),'*')
        res = self.nw.forward(normalize(array))
        if res[0]:
            msg = "Image recognized in %d iterations" % res[2]
            self.statusBar().showMessage(self.tr(msg))
            recognized_path = self.figures[res[1]]
            self.__show_img(self.recognizedImageLabel, recognized_path)
        else:
            msg = "Image not recognized after %d iterations" % res[2]
            self.statusBar().showMessage(self.tr(msg))

    def show_image(self, index):
        item = self.imagesListWidget.item(index)
        fig_index = item.data(Qt.UserRole).toInt()[0]
        self.__show_img(self.ImageListLabel, self.figures[fig_index])

    def __show_img(self, label, path):
        image = QImage(path)
        image = image.scaled(QSize(50, 50), Qt.KeepAspectRatio)
        label.setPixmap(QPixmap.fromImage(image))


import sys
if __name__=="__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


