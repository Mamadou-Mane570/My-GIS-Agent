from qgis.PyQt.QtWidgets import QAction


class GISAgentPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):

        self.action = QAction(
            "My GIS Agent",
            self.iface.mainWindow()
        )

        self.iface.addPluginToMenu(
            "My GIS Agent",
            self.action
        )

    def unload(self):

        if self.action:

            self.iface.removePluginMenu(
                "My GIS Agent",
                self.action
            )