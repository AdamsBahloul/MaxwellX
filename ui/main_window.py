from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QToolBar, QLabel
)
from PySide6.QtCore import Qt

from panels.control_panel import ControlPanel
from panels.object_panel import ObjectPanel
from visualization.field_canvas import FieldCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MaxwellX")
        self.resize(1200, 800)

        self._create_toolbar()
        self._create_layout()

    def _create_toolbar(self):
        toolbar = QToolBar("Simulation")
        toolbar.setMovable(False)

        toolbar.addWidget(QLabel(" ▶ Run   ⏸ Pause   ⏹ Reset "))

        self.addToolBar(toolbar)

    def _create_layout(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        self.control_panel = ControlPanel()
        self.object_panel = ObjectPanel()
        self.canvas = FieldCanvas()

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.control_panel)
        left_layout.addWidget(self.object_panel)

        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(self.canvas.native, 4)
