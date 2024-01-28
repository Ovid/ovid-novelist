from PyQt6.QtGui import QShortcut, QKeySequence

def add_shortcuts(window):
    fonts = window.fonts
    QShortcut(QKeySequence("Ctrl+B"), window, fonts.setBoldText)
    QShortcut(QKeySequence("Ctrl+I"), window, fonts.setItalicText)
    QShortcut(QKeySequence("Ctrl+U"), window, fonts.setUnderlineText)
    QShortcut(QKeySequence("Ctrl+T"), window, fonts.setStrikeThroughText)
    QShortcut(QKeySequence("Ctrl+Shift+C"), window, fonts.clearFormatting)
