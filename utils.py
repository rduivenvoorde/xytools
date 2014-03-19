'''
Created on 11/12/2013

@author: victorzinho
'''

from qgis.core import QGis


def fieldNames(layer):
    fields = layer.dataProvider().fields()

    if QGis.QGIS_VERSION_INT < 10900:
        from PyQt4.QtCore import QStringList
        fieldNames = QStringList()
        for field in fields.values():
            fieldNames.append(field.name())
    else:
        return map(lambda field: field.name(), fields)
