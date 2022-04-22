from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QToolBar

from views.Actions import Actions


class Toolbar(Actions):
    def __init__(self, controller):
        super(Toolbar, self).__init__(controller)

        self.controller = controller
        self.win = self.controller.mainWindow
        self.toolbar = QToolBar()

        self._actions()

    def _actions(self):
        self.toolbar.addAction(self.playback_prev)
        self.toolbar.addAction(self.playback_stop)
        self.toolbar.addAction(self.playback_play)
        self.toolbar.addAction(self.playback_pause)
        self.toolbar.addAction(self.playback_next)

    def main(self):
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(16, 16))
        self.win.addToolBar(self.toolbar)
