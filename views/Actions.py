from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction


class Actions:
    def __init__(self, controller):
        self.controller = controller
        self.model = self.controller.model

        self.media_open = QAction(self.model.open_icon, "Medya Aç")
        self.media_refresh = QAction(self.model.refresh_icon, "Yenile")
        self.media_exit = QAction(self.model.exit_icon, "Çık")

        self.playback_play = QAction(self.model.play_icon, "Oynat")
        self.playback_pause = QAction(self.model.pause_icon, "Duraklat")
        self.playback_stop = QAction(self.model.stop_icon, "Durdur")
        self.playback_prev = QAction(self.model.prev_icon, "Önceki")
        self.playback_next = QAction(self.model.next_icon, "Sonraki")

        self.sound_increase = QAction(self.model.increase_icon, "Sesi Arttır")
        self.sound_decrease = QAction(self.model.decrease_icon, "Sesi Azalt")
        self.sound_mute = QAction(self.model.mute_icon, "Sesi Sustur")

        self.view_full = QAction(self.model.full_icon, "Tam Ekran")
        self.view_menu = QAction(self.model.menu_icon, "Menü Göster/Gizle")
        self.view_toolbar = QAction(self.model.toolbar_icon, "Araç Çubuğu Göster/Gizle")
        self.view_dark = QAction(self.model.dark_icon, "Gece görünümü")

        self.help_help = QAction(self.model.help_icon, "Yardım")
        self.help_about = QAction(self.model.about_icon, "Hakkında")

        self.disable()
        self._checks()
        self._triggers()

    def disable(self):
        self.playback_play.setEnabled(True)
        self.playback_pause.setEnabled(False)
        self.playback_stop.setEnabled(False)
        self.playback_prev.setEnabled(False)
        self.playback_next.setEnabled(False)

    def enable(self):
        self.playback_play.setEnabled(False)
        self.playback_pause.setEnabled(True)
        self.playback_stop.setEnabled(True)
        self.playback_prev.setEnabled(True)
        self.playback_next.setEnabled(True)

    def shortcuts(self):
        self.media_open.setShortcut(QKeySequence("Ctrl+O"))
        self.media_exit.setShortcut(QKeySequence("Alt+F4"))

        self.playback_play.setShortcut(QKeySequence("K"))
        self.playback_pause.setShortcut(QKeySequence("J"))
        self.playback_stop.setShortcut(QKeySequence("S"))
        self.playback_prev.setShortcut(QKeySequence("P"))
        self.playback_next.setShortcut(QKeySequence("N"))

        self.sound_increase.setShortcut(QKeySequence("+"))
        self.sound_decrease.setShortcut(QKeySequence("-"))
        self.sound_mute.setShortcut(QKeySequence("M"))

        self.view_full.setShortcut(QKeySequence("F11"))
        self.view_menu.setShortcut(QKeySequence("Ctrl+Shift+M"))
        self.view_toolbar.setShortcut(QKeySequence("Ctrl+Shift+T"))
        self.view_dark.setShortcut(QKeySequence("Ctrl+Shift+D"))

        self.help_help.setShortcut(QKeySequence("Ctrl+H"))
        self.help_about.setShortcut(QKeySequence("Ctrl+Shift+O"))

    def _checks(self):
        self.view_full.setCheckable(True)
        self.view_full.setChecked(False)

        self.view_menu.setCheckable(True)
        self.view_menu.setChecked(True)

        self.view_toolbar.setCheckable(True)
        self.view_toolbar.setChecked(True)

        self.view_dark.setCheckable(True)
        self.view_dark.setChecked(False)

    def _triggers(self):
        self.media_open.triggered.connect(self.controller.action_media_open)
        self.media_refresh.triggered.connect(self.controller.reload_tables)
        self.media_exit.triggered.connect(self.controller.action_media_exit)

        self.playback_play.triggered.connect(self.controller.action_play)
        self.playback_pause.triggered.connect(self.controller.action_pause)
        self.playback_stop.triggered.connect(self.controller.action_stop)
        self.playback_prev.triggered.connect(self.controller.action_prev)
        self.playback_next.triggered.connect(self.controller.action_next)

        self.sound_increase.triggered.connect(self.controller.action_increase_sound)
        self.sound_decrease.triggered.connect(self.controller.action_decrease_sound)
        self.sound_mute.triggered.connect(self.controller.action_mute_sound)

        self.view_full.triggered.connect(self.controller.action_view_full)
        self.view_menu.triggered.connect(self.controller.action_view_menu)
        self.view_toolbar.triggered.connect(self.controller.action_view_toolbar)
        self.view_dark.triggered.connect(self.controller.action_view_dark)

        self.help_help.triggered.connect(self.controller.action_help_help)
        self.help_about.triggered.connect(self.controller.action_help_about)
