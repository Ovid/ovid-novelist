from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
)


class NewNovelDialog(QDialog):
    def __init__(self, author_collection, parent=None):
        super().__init__(parent)
        self.setup()

    def setup(self):
        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.genre_edit = QLineEdit()

        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Genre"))
        layout.addWidget(self.genre_edit)

        ok_button = QPushButton("Start Writing!")
        ok_button.clicked.connect(self.accept)
        ok_button.setEnabled(False)  # Disable the button initially

        layout.addWidget(ok_button)

        self.name_edit.textChanged.connect(
            self.check_input
        )  # Connect the textChanged signal to the check_input slot

        self.setLayout(layout)
        self.layout = layout
        self.ok_button = ok_button

    def check_input(self):
        # If the name_edit line edit is not empty, enable the button; otherwise, disable it
        self.ok_button.setEnabled(bool(self.name_edit.text()))
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)
