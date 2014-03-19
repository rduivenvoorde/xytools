from PyQt4.QtCore import Qt, SIGNAL, QObject
from PyQt4.QtGui import QDialog, QListWidgetItem
from ui_field_chooser import Ui_FieldChooser


class FieldChooserDialog(QDialog):

    def __init__(self, fieldNames):
        QDialog.__init__(self)

        self.ui = Ui_FieldChooser()
        self.ui.setupUi(self)

        self.items = []
        self.ui.fieldList.clear()
        for fieldName in fieldNames:
            item = QListWidgetItem()
            item.setText(fieldName)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.ui.fieldList.addItem(item)
            self.items.append(item)

        QObject.connect(self.ui.unselectAll,
                SIGNAL("clicked()"), self.unselectAll)
        QObject.connect(self.ui.selectAll,
                SIGNAL("clicked()"), self.selectAll)

    def selectAll(self):
        for item in self.items:
            item.setCheckState(Qt.Checked)

    def unselectAll(self):
        for item in self.items:
            item.setCheckState(Qt.Unchecked)

    def getSelectedFields(self):
        selected = filter(lambda item: item.checkState() == Qt.Checked,
                          self.items)
        return map(lambda item: item.text(), selected)
