import xlwt

from datetime import datetime
from PyQt4.QtCore import *


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




    def test(self):
        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0

        style1 = xlwt.XFStyle()
        style1.num_format_str = 'D-MMM-YY'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')

        ws.write(0, 0, 'Test', style0)
        ws.write(1, 0, datetime.now(), style1)
        ws.write(2, 0, 1)
        ws.write(2, 1, 1)
        ws.write(2, 2, xlwt.Formula("A3+B3"))
        ws.write(2, 3, 'kaas')

        wb.save('/tmp/example2.xls')


