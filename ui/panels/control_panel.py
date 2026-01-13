from PySide6.QtWidgets import (
    QGroupBox, QVBoxLayout, QLabel, QSlider
)
from PySide6.QtCore import Qt


class ControlPanel(QGroupBox):
    def __init__(self):
        super().__init__("Simulation Controls")

        layout = QVBoxLayout()

        self.time_label = QLabel("Time step: 0.01")
        self.time_slider = QSlider(Qt.Horizontal)
        self.time_slider.setRange(1, 100)
        self.time_slider.setValue(10)

        self.time_slider.valueChanged.connect(self._update_label)

        layout.addWidget(self.time_label)
        layout.addWidget(self.time_slider)

        layout.addStretch()
        self.setLayout(layout)

    def _update_label(self, value):
        self.time_label.setText(f"Time step: {value / 100:.2f}")
