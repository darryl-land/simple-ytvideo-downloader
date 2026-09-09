import sys
import faulthandler
faulthandler.enable()
from PyQt6.QtCore import Qt, QProcess
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QMessageBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple YT Video Downloader")
        self.widget = QLineEdit()
        self.widget.setPlaceholderText("Enter your YouTube video URL")
        self.outputer = QTextEdit(self)
        self.outputer.setReadOnly(True)
        self.widget.returnPressed.connect(self.entereda)
        layout = QVBoxLayout()
        layoutb = QHBoxLayout()
        label = QLabel("Simple YT Video Downloader")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(self.outputer)
        layoutb.addWidget(self.widget)
        self.button = QPushButton("Download", self)
        self.button.clicked.connect(self.clickedy)
        layoutb.addWidget(self.button)
        midget = QWidget()
        midget.setLayout(layoutb)
        layout.addWidget(midget)
        self.cap = QCheckBox(text="Enable auto-generated english captions")
        layout.addWidget(self.cap)
        fidget = QWidget()
        fidget.setLayout(layout)
        self.setCentralWidget(fidget)
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.dod)
        self.process.finished.connect(self.donee)
    def dod(self):
        data = self.process.readAllStandardOutput().data().decode(errors='ignore')
        self.fodd(data)
    def fodd(self, text):
        self.outputer.insertPlainText(text)
    def entereda(self):
        print("Return pressed!")
        print(self.widget.text())
        theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.cap.isChecked():
            theresta.append("--embed-subs")
            theresta.append("--write-auto-subs")
            theresta.append("--sub-langs")
            theresta.append("en")
            theresta.append(self.widget.text())
        else:
            theresta.append(self.widget.text())
        thingyy = "stdbuf"
        print(thingyy, theresta)
        self.process.start(thingyy, theresta)
    def clickedy(self):
        print(self.widget.text())
        if self.process.state() == QProcess.ProcessState.Running:
            return
        theresta = ["-oL", "-eL", "yt-dlp", "-P","~/Videos/"]
        if self.process.state() == QProcess.ProcessState.Running:
            return
        if self.cap.isChecked():
            theresta.append("--embed-subs")
            theresta.append("--write-auto-subs")
            theresta.append("--sub-langs")
            theresta.append("en")
            theresta.append(self.widget.text())
        else:
            theresta.append(self.widget.text())
        thingyy = "stdbuf"
        print(thingyy, theresta)
        self.process.start(thingyy, theresta)
    def donee(self, exitcodde, exit_status):
        if exit_status == QProcess.ExitStatus.NormalExit:
            if exitcodde == 0:
                finga = QMessageBox.information(self, "Alert", "Done downloading video! Exited with exit code " + str(exitcodde))
            else:
                finga = QMessageBox.warning(self, "Alert", "Uh oh! Something went wrong. Exit code " + str(exitcodde))
        else:
            finga = QMessageBox.critical(self, "Alert", "Ahhh! Something went very very wrong!")
app = QApplication(sys.argv)
app.setWindowIcon(QIcon("unnamed.png"))
window = MainWindow()
window.show()
app.exec()
