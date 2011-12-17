import xlwt
from xlrd import open_workbook
from PyQt4.QtCore import *


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
            if type(cell) == QString:
                # cast to QVariable
                # TODO: do this better
                cell = QVariant(cell)
            self.ws.write( rowNr, colNr, unicode(cell.toString()) )
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


