from PySide6.QtWidgets import (
    QGroupBox, QVBoxLayout, QListWidget, QPushButton
)


class ObjectPanel(QGroupBox):
    def __init__(self):
        super().__init__("Objects")

        layout = QVBoxLayout()

        self.list = QListWidget()
        self.list.addItem("Charge +1e-6 C @ (0,0)")
        self.list.addItem("Charge -1e-6 C @ (1,0)")

        add_btn = QPushButton("Add Charge")
        remove_btn = QPushButton("Remove Selected")

        layout.addWidget(self.list)
        layout.addWidget(add_btn)
        layout.addWidget(remove_btn)

        self.setLayout(layout)
