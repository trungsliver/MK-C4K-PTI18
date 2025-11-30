import sys
import os

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

from models import models


class MainWindow(QMainWindow):
    # Định nghĩa vị trí của các file ui
    UI_LOCATION = os.path.join("ui/main_window1.ui")
    STYLE_LOCATION = os.path.join("ui/style_main1.qss")
    def __init__(self, parent:QApplication):
        super(MainWindow, self).__init__()
        self.app = parent

        # Load file giao diện .ui và .qss
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        with open(self.STYLE_LOCATION, "r") as style_file:
            style_config = style_file.read()
        self.setStyleSheet(style_config)

        # Hiển thị trang CRUD
        self.ui.stackedWidget.setCurrentIndex(2)

        # Tạo database
        self.dtb = models.AnimeDatabase()
        self.dtb.load_data()
        # Hiển thị danh sách anime
        anime_titles = self.dtb.get_title_list()
        self.ui.animeList.addItems(anime_titles)

        # Hiển thị cửa sổ ra màn hình
        self.show()

    def on_homeButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_rankButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_CRUDButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_exitButton_clicked(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)

    sys.exit(app.exec())
