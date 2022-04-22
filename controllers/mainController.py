import os
import time

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMessageBox

from model.model import Model
from views.MainWindow import MainWindow
from views.Menus import Menus
from views.MusicTable import MusicTable
from views.Toolbar import Toolbar


# todo : append stylesheets in order to make program dark or light
# todo : make buttons work


class MainController:
    def __init__(self):
        # model
        self.model = Model()

        # views
        self.mainWindow = MainWindow(self)
        self.menus = Menus(self)
        self.toolBar = Toolbar(self)
        self.table = MusicTable(self)

    # starters
    def main(self) -> None:
        self.mainWindow.main()
        self.menus.main()
        self.toolBar.main()
        self.table.main()

        self.mainWindow.setCentralWidget(self.table)

    # table loaders

    def remove_data(self) -> None:
        self.table.tableModel.setRowCount(0)

    def append_data(self, data: list) -> None:
        self.table.tableModel.insertRow(0)

        for datum in data:
            for i in range(len(datum)):
                self.table.tableModel.setData(self.table.tableModel.index(0, i), datum[i])

    def reload_tables(self) -> None:
        #  get data
        # remove old ones
        # load data into tables

        data = []
        files = self.model.music_files(self.model.directory)
        tmp_player = QMediaPlayer()

        for file in files:
            tmp_player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))

            name = os.path.basename(file).split('.mp3')[0]
            duration = tmp_player.duration()
            date = time.ctime(os.stat(file).st_ctime)
            datum = [name, duration, date]
            data.append(datum)

        self.remove_data()
        self.append_data(data)

    # table listeners
    def selected(self) -> None:
        table_model = self.table.model()
        indexes = self.table.selectedIndexes()

        if indexes:
            self.model.selected_row = indexes[0].row()
            self.model.selected_id = table_model.data(table_model.index(self.model.selected_row, 0))

            self.menus.enable()
            self.toolBar.enable()

    def action_media_open(self) -> None:
        pass

    def action_media_exit(self) -> bool:
        ask = QMessageBox.question(self.mainWindow, self.model.title, "Uygulamadan çıkmak istediğinize emin misiniz?",
                                   QMessageBox.Yes | QMessageBox.No)
        return True if ask == QMessageBox.Yes else False

    def action_play(self) -> None:
        self.toolBar.enable()
        self.menus.enable()
        self.model.mediaPlayer.play()

    def action_pause(self) -> None:
        if self.model.mediaPlayer.state() == QMediaPlayer.PlayingState:
            print(self.model.mediaPlayer.position())
            self.model.mediaPlayer.pause()
            self.toolBar.disable()
            self.menus.disable()

    def action_stop(self) -> None:
        if self.model.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.model.mediaPlayer.stop()
            self.toolBar.disable()
            self.menus.disable()

    def action_prev(self) -> None:
        pass

    def action_next(self) -> None:
        pass

    def action_increase_sound(self) -> None:
        self.model.mediaPlayer.setVolume(self.model.mediaPlayer.volume() + 5)

    def action_decrease_sound(self) -> None:
        self.model.mediaPlayer.setVolume(self.model.mediaPlayer.volume() - 5)

    def action_mute_sound(self) -> None:
        self.model.mediaPlayer.setMuted(True)

    def action_view_full(self) -> None:
        if self.mainWindow.isFullScreen():
            self.mainWindow.showNormal()

        else:
            self.mainWindow.showFullScreen()

    def action_view_menu(self) -> None:
        menubar = self.mainWindow.menuBar()
        menubar.setVisible(False if menubar.isVisible() else True)

    def action_view_toolbar(self) -> None:
        toolbar = self.toolBar.toolbar
        toolbar.setVisible(False if toolbar.isVisible() else True)

    def action_view_dark(self) -> None:
        if self.model.config.get('dark'):
            self.model.update("dark", False)

        else:
            self.model.update("dark", True)

        stylesheets = self.model.read_stylesheets()

        if stylesheets is not None:
            print(stylesheets)

    def action_help_help(self) -> None:
        QMessageBox.information(self.mainWindow, self.model.title,
                                "Program hakkında yardım için\ninserveofgod@gmail.com adresine mail gönderebilirsiniz",
                                QMessageBox.Ok)

    def action_help_about(self) -> None:
        QMessageBox.information(self.mainWindow, self.model.title,
                                "Bu program Python programalama dili ile PyQt5\n"
                                "kütüphanesi kullanılarak yapılmıştır.",
                                QMessageBox.Ok)
