

# Run in the terminal
if __name__ == '__main__':

    app = QApplication([])

    app.setStyle('Fusion')

    window = Window()

    window.show()

    window.setFixedSize(window.size())

    sys.exit(app.exec_())

