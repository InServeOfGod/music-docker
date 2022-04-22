from PyQt5.QtWidgets import QMenu

from views.Actions import Actions


class Menus(Actions):
    def __init__(self, controller):
        super(Menus, self).__init__(controller)
        self.controller = controller
        self.win = self.controller.mainWindow

        self.media = QMenu("&Medya")
        self.playback = QMenu("&Oynatma")
        self.sound = QMenu("&Ses")
        self.view = QMenu("&Görünüm")
        self.help = QMenu("&Yardım")

        self._actions()
        self.shortcuts()

    def _actions(self):
        media_actions = [self.media_open, self.media_refresh, self.media_exit]
        playback_actions = [self.playback_play, self.playback_pause, self.playback_stop, self.playback_prev,
                            self.playback_next]
        sound_actions = [self.sound_increase, self.sound_decrease, self.sound_mute]
        view_actions = [self.view_full, self.view_menu, self.view_toolbar, self.view_dark]
        help_actions = [self.help_help, self.help_about]

        for media_action in media_actions:
            self.media.addAction(media_action)

        for playback_action in playback_actions:
            self.playback.addAction(playback_action)

        for sound_action in sound_actions:
            self.sound.addAction(sound_action)

        for view_action in view_actions:
            self.view.addAction(view_action)

        for help_action in help_actions:
            self.help.addAction(help_action)

    def main(self):
        menubar = self.win.menuBar()
        menubar.addMenu(self.media)
        menubar.addMenu(self.playback)
        menubar.addMenu(self.sound)
        menubar.addMenu(self.view)
        menubar.addMenu(self.help)
