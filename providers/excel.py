import xlwt
from xlrd import open_workbook
from PyQt4.QtCore import QVariant
from qgis.core import QGis


class Reader:
    def __init__(self, filename):
        self.fileName = filename

    def openFile(self):
        wb = open_workbook(self.fileName)
        rows = []
        for sheet in wb.sheets():
            for index in range(sheet.nrows):
                row = sheet.row(index)
                values = map(lambda cell: cell.value, row)
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
            if not cell:
                cell = ''
            else:
                cell = unicode(cell)
                try:
                    cell = float(cell)
                except:
                    pass

            self.ws.write(rowNr, colNr, cell)
            colNr = colNr + 1

    def saveFile(self):
        self.wb.save(self.fileName)
