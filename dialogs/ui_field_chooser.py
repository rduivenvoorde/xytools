# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/ui_field_chooser.ui'
#
# Created: Fri Dec 13 17:45:45 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FieldChooser(object):
    def setupUi(self, FieldChooser):
        FieldChooser.setObjectName(_fromUtf8("FieldChooser"))
        FieldChooser.setWindowModality(QtCore.Qt.ApplicationModal)
        FieldChooser.resize(400, 298)
        FieldChooser.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(FieldChooser)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(25, 20, 25, 20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(FieldChooser)
        self.label.setMargin(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.selectButtonsLayout = QtGui.QHBoxLayout()
        self.selectButtonsLayout.setSpacing(40)
        self.selectButtonsLayout.setContentsMargins(25, 0, 25, 0)
        self.selectButtonsLayout.setObjectName(_fromUtf8("selectButtonsLayout"))
        self.selectAll = QtGui.QPushButton(FieldChooser)
        self.selectAll.setObjectName(_fromUtf8("selectAll"))
        self.selectButtonsLayout.addWidget(self.selectAll)
        self.unselectAll = QtGui.QPushButton(FieldChooser)
        self.unselectAll.setObjectName(_fromUtf8("unselectAll"))
        self.selectButtonsLayout.addWidget(self.unselectAll)
        self.verticalLayout.addLayout(self.selectButtonsLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.fieldList = QtGui.QListWidget(FieldChooser)
        self.fieldList.setObjectName(_fromUtf8("fieldList"))
        self.verticalLayout.addWidget(self.fieldList)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttons = QtGui.QDialogButtonBox(FieldChooser)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(FieldChooser)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("accepted()")), FieldChooser.accept)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("rejected()")), FieldChooser.reject)
        QtCore.QMetaObject.connectSlotsByName(FieldChooser)

    def retranslateUi(self, FieldChooser):
        FieldChooser.setWindowTitle(QtGui.QApplication.translate("FieldChooser", "XYTools - Save as Excel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FieldChooser", "Choose fields:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAll.setText(QtGui.QApplication.translate("FieldChooser", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.unselectAll.setText(QtGui.QApplication.translate("FieldChooser", "Unselect All", None, QtGui.QApplication.UnicodeUTF8))

