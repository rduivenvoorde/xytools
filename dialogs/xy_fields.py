"""
/***************************************************************************
 XyToolsDialog
                                 A QGIS plugin
 Tools for managing tabular data with x y columns
                             -------------------
        begin                : 2011-08-19
        copyright            : (C) 2011 by Richard Duivenvoorde
        email                : richard@duif.net
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

from PyQt4.QtGui import QDialog
from ui_xy_fields import Ui_XyFields


# create the dialog for zoom to point
class XyFieldsDialog(QDialog):

    def __init__(self, comboMsg, fieldNames, layerName):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_XyFields()
        self.ui.setupUi(self)

        # fill dropdowns
        fieldNames.insert(0, comboMsg)
        self.ui.cmbXcoord.clear()
        self.ui.cmbYcoord.clear()
        self.ui.cmbXcoord.addItems(fieldNames)
        self.ui.cmbYcoord.addItems(fieldNames)
        self.ui.groupxy.setTitle("Current layer: '" + layerName + "'")

    def getXindex(self):
        # because first one is caption
        return self.ui.cmbXcoord.currentIndex() - 1

    def getYindex(self):
        # because first one is caption
        return self.ui.cmbYcoord.currentIndex() - 1
