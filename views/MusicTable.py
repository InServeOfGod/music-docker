from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTreeView, QAbstractItemView


class MusicTable(QTreeView):
    def __init__(self, controller):
        super(MusicTable, self).__init__()

        self.controller = controller

        self.titles = self.controller.model.musics_table_titles
        self.title_size = len(self.titles)
        self.tableModel = QStandardItemModel(0, self.title_size)

    def main(self):
        for i in range(self.title_size):
            self.tableModel.setHeaderData(i, Qt.Horizontal, self.titles[i])

        self.setModel(self.tableModel)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selectionModel().selectionChanged.connect(self.controller.selected)
