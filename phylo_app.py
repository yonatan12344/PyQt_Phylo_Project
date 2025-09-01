import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Phylogenetic Tree Builder")
w.show()
return_code = app.exec_()
sys.exit(return_code)

print("Hi")
