import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from cefpython3 import cefpython as cef
import platform

class CefWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.browser = None
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.start_chromium()

    def start_chromium(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.width(), self.height()]
        window_info.SetAsChild(int(self.winId()), rect)

        self.browser = cef.CreateBrowserSync(
            window_info,
            url="https://www.google.com"
        )

    def resizeEvent(self, event):
        if self.browser:
            cef.WindowUtils().OnSize(int(self.winId()), 0, 0, 0)

class WaveBrowse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WaveBrowse - Chromium Inside, PyQt Outside")
        self.setGeometry(100, 100, 1200, 800)

        self.browser_widget = CefWidget(self)
        self.setCentralWidget(self.browser_widget)

    def closeEvent(self, event):
        cef.QuitMessageLoop()
        event.accept()

def main():
    sys.excepthook = cef.ExceptHook
    cef_settings = {}
    if platform.system() == "Windows":
        cef_settings["multi_threaded_message_loop"] = False

    cef.Initialize(settings=cef_settings)

    app = QApplication(sys.argv)
    window = WaveBrowse()
    window.show()

    cef.MessageLoop()
    cef.Shutdown()

if __name__ == '__main__':
    main()