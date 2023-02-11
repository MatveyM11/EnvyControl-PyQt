import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QInputDialog, QSystemTrayIcon, QMenu
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
isHybrid = True

class EnvyControl(QWidget):


    def start_status(self):
        result = subprocess.check_output(['envycontrol', '-q'])
        sep = ': '
        status = result.strip().decode()
        status = status.split(sep, 1)[1]
        return status

    def quit(self):
        sys.exit()


    def nvidia_tray(self):
        icon_start = self.start_status()
        global isHybrid
        if icon_start == "hybrid" and isHybrid == True:
            password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
            if ok:
                self.run_command('nvidia', password)
                app_path = os.path.join(current_dir, "nvidia.png")
                icon = QtGui.QIcon(app_path)
                self.tray_icon.setIcon(QIcon(icon))
        else:
            status = "Try switching to hybrid mode first!"
            self.status_label.setText(status)
            isHybrid = False

    def integrated_tray(self):
        password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
        if ok:
            self.run_command('integrated', password)
            app_path = os.path.join(current_dir, "integrated_amd.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
            self.update_status()

    def hybrid_tray(self):
        password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
        if ok:
            self.run_command('hybrid', password)
            app_path = os.path.join(current_dir, "hybrid.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
            self.update_status()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('EnvyControl Qt')
        app_path = os.path.join(current_dir, "envycontrol.png")
        icon = QtGui.QIcon(app_path)
        self.setWindowIcon(icon)
        self.status_label = QLabel()
        self.update_status()

        integrated_button = QPushButton('Integrated')
        integrated_button.clicked.connect(self.on_integrated_clicked)

        hybrid_button = QPushButton('Hybrid')
        hybrid_button.clicked.connect(self.on_hybrid_clicked)

        nvidia_button = QPushButton('Nvidia')
        nvidia_button.clicked.connect(self.on_nvidia_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(self.status_label)
        vbox.addWidget(integrated_button)
        vbox.addWidget(hybrid_button)
        vbox.addWidget(nvidia_button)

        self.setLayout(vbox)

        self.tray_icon = QSystemTrayIcon(self)

        icon_start = self.start_status()
        if icon_start == "integrated":
            app_path = os.path.join(current_dir, "./integrated_amd.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
        elif icon_start == "hybrid":
            app_path = os.path.join(current_dir, "hybrid.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
        elif icon_start == "nvidia":
            app_path = os.path.join(current_dir, "nvidia.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))

        self.tray_icon.setVisible(True)
        self.tray_icon.show()
        print(icon_start)

        self.tray_menu = QMenu()
        self.tray_menu.addAction('Integrated', self.integrated_tray)
        self.tray_menu.addAction('Hybrid', self.hybrid_tray)
        self.tray_menu.addAction('Nvidia', self.nvidia_tray)
        self.tray_menu.addAction('Show', self.show)
        self.tray_menu.addAction('Quit',  self.quit)
        self.tray_icon.setContextMenu(self.tray_menu)

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def on_integrated_clicked(self):
        password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
        if ok:
            self.run_command('integrated', password)
            app_path = os.path.join(current_dir, "./integrated_amd.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
            self.update_status()

    def on_hybrid_clicked(self):
        password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
        if ok:
            self.run_command('hybrid', password)
            app_path = os.path.join(current_dir, "hybrid.png")
            icon = QtGui.QIcon(app_path)
            self.tray_icon.setIcon(QIcon(icon))
            self.update_status()

    def on_nvidia_clicked(self):
        icon_start = self.start_status()
        global isHybrid
        if icon_start == "hybrid" and isHybrid == True:
            password, ok = QInputDialog.getText(self, 'Password', 'Enter your sudo password:', QLineEdit.Password)
            if ok:
                self.run_command('nvidia', password)
                app_path = os.path.join(current_dir, "nvidia.png")
                icon = QtGui.QIcon(app_path)
                self.tray_icon.setIcon(QIcon(icon))
        else:
            status = "Try switching to hybrid mode first!"
            self.status_label.setText(status)
            isHybrid = False

    def update_status(self):
        result = subprocess.check_output(['envycontrol', '-q'])
        status = result.strip().decode()
        self.status_label.setText(status)

    def run_command(self, mode, password):
        p = subprocess.Popen(['sudo', '-S', 'envycontrol', '-s', mode], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate(input=password.encode())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    envy = EnvyControl()
    envy.show()
    sys.exit(app.exec_())
