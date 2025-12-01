import sys
import os

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
# import speech_recognition as sr
import pyttsx3

from models import models
from widgets import dialog

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

        # Setup trang CRUD
        self.setup_CRUD_page()

        # Setup engine TTS
        self.tts_engine = pyttsx3.init()
        
        # Hiển thị cửa sổ ra màn hình
        self.show()

    def setup_CRUD_page(self):
        # Hiển thị danh sách anime
        anime_titles = self.dtb.get_title_list()
        self.ui.animeList.addItems(anime_titles)
        self.ui.animeList.setCurrentRow(0)

        # Khiến tất cả các nút "nói"
        all_buttons = self.findChildren(QPushButton)
        for button in all_buttons:
            button.clicked.connect(lambda _, b=button: self.speak_text(b))

        # Xử lý các button
        self.ui.addButton.clicked.connect(self.add)
        self.ui.editButton.clicked.connect(self.edit)
        self.ui.removeButton.clicked.connect(self.delete)

    
    def speak_text(self, button:QPushButton):
        # Phương thức text to speech
        self.tts_engine.say(button.text())
        self.tts_engine.runAndWait()

    def on_homeButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_rankButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_CRUDButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_exitButton_clicked(self):
        QApplication.quit()

    ### CRUD methods
    def add(self):
        curr_index = self.ui.animeList.currentRow()

        # Tạo Dialog Add
        add_dialog = dialog.AddDialog()
        # Nếu nhấn nút OK trên dialog
        if add_dialog.exec():
            # Lấy dữ liệu từ dialog
            inputs = add_dialog.return_input_fields()
            # Thêm item vào List Widget
            self.ui.animeList.insertItem(curr_index, inputs["title"])
            # Thêm dữ liệu vào database
            self.dtb.add_item(inputs)

    def edit(self):
        # Lấy item đang chọn
        curr_index = self.ui.animeList.currentRow()
        item = self.ui.animeList.item(curr_index)
        item_title = item.text()
        edit_item = self.dtb.get_first_item_by_title(item_title)

        # Tạo Dialog Edit 
        if item is not None:
            edit_dialog = dialog.EditDialog(edit_item)
            # Nếu nhấn nút OK trên dialog
            if edit_dialog.exec():
                # Lấy dữ liệu từ dialog
                inputs = edit_dialog.return_input_fields()
                # Sửa lại tên item trên List Widget
                item.setText(inputs["title"])
                # Sửa dữ liệu trong database
                self.dtb.edit_item(item_title, inputs)

    def delete(self):
        # Lấy item đang chọn
        curr_index = self.ui.animeList.currentRow()
        item = self.ui.animeList.item(curr_index)
        item_title = item.text()
        
        # Tạo Message Box confirm
        if item is not None:
            choice = QMessageBox.question(self, "Remove Anime",
                                            "Do you want to remove this anime?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Nếu chọn nút "Yes"
            if choice == QMessageBox.StandardButton.Yes:
                # Xoá item khỏi List Widget
                item = self.ui.animeList.takeItem(curr_index)
                # Xoá dữ liệu trong database
                self.dtb.delete_item(item_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)

    sys.exit(app.exec())
