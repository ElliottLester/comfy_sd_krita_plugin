import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTabWidget

from krita_comfy.config import Config
from krita_comfy.pages.txt2img import Txt2ImgPage
from krita_comfy.pages.img_combined import CombinedPage

"""Test App for GUI components
    This file is not part of the Krita plugin.
    this is a way to invoke the plugin pages
    outside of Krita to test and debug them directly.
 """

class Test_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cfg = Config()
        self.tabs: QTabWidget = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.txt2img = Txt2ImgPage()
        self.combined = CombinedPage()
        self.tabs.addTab(self.txt2img, "txt2img")
        self.tabs.addTab(self.combined, "combined")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test_Window()
    window.show()
    sys.exit(app.exec_())
