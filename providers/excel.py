import xlwt
from xlrd import open_workbook
from PyQt4.QtCore import *
from qgis.core import *


class Reader:

    #fileName = '/home/richard/temp/prov/prov.xls'
    fileName = ''

    wb = None
    ws = None

    def __init__(self, filename):
        self.fileName = filename

    def openFile(self):
        wb = open_workbook(self.fileName)
        rows = []
        for s in wb.sheets():
            #print 'Sheet:',s.name
            #print '#rows:',s.nrows
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row,col).value)
                #print ','.join(values)
                rows.append(values)
        return rows

class Writer:

    fileName = '/tmp/example2.xls'

    wb = None
    ws = None

    def __init__(self, filename):
        self.fileName = filename
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('Qgis Attributes')

    def writeAttributeRow(self, rowNr, attributes):
        colNr = 0
        for cell in attributes:
            # QGIS2.0 does not have QVariants anymore, only for <2.0:
            if QGis.QGIS_VERSION_INT < 10900:
                cell = QVariant(cell)
                if cell.canConvert(QVariant.Int) and cell.toInt()[1]:
                    cell = cell.toInt()[0]
                elif cell.canConvert(QVariant.Double) and cell.toDouble()[1]:
                    cell = cell.toDouble()[0]
                else:
                    cell = unicode(cell.toString())
            # handle NULL values by writing 'NULL'
            if cell == NULL:
                cell = 'NULL'
            self.ws.write( rowNr, colNr, cell )
            colNr = colNr+1

    def saveFile(self):
        self.wb.save(self.fileName)

    def openFile(self):
        wb = open_workbook('/home/richard/temp/prov/prov.xls')
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row,col).value)


