"""
/***************************************************************************
 XyToolsDialog
                                 A QGIS plugin
 Tools for managing tabular data with x y columns
                             -------------------
        begin                : 2011-08-19
        copyright            : (C) 2011 by webmapper
        email                : richard@webmapper.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_xytools import Ui_XyTools
# create the dialog for zoom to point
class XyToolsDialog(QtGui.QDialog):

    def __init__(self, comboMsg, fieldMap, layerName):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_XyTools()
        self.ui.setupUi(self)
        # fill dropdowns
        fields = QtCore.QStringList()
        fields.append(comboMsg)
        for field in fieldMap.values():
            fields.append(field.name())
        self.ui.cmbXcoord.clear()
        self.ui.cmbYcoord.clear()
        self.ui.cmbXcoord.addItems(fields)
        self.ui.cmbYcoord.addItems(fields)
        self.ui.groupxy.setTitle("Current layer: '"+layerName+"'")

    def getXindex(self):
        return self.ui.cmbXcoord.currentIndex()-1 # because first one is caption

    def getYindex(self):
        return self.ui.cmbYcoord.currentIndex()-1 # because first one is caption
