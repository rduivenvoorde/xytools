import uno
from com.sun.star.beans import PropertyValue 
import os
import sys
import os.path as osp
import time

from PyQt4.QtCore import *


# http://www.logilab.org/blogentry/6130

def _uno_init(_try_start=True):
    """init python-uno bridge infrastructure"""
    try:
        # Get the uno component context from the PyUNO runtime
        local_context = uno.getComponentContext()
        # Get the local Service Manager
        local_service_manager = local_context.ServiceManager
        # Create the UnoUrlResolver on the Python side.
        local_resolver = local_service_manager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context)
        # Connect to the running OpenOffice.org and get its context.
        context = local_resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        # Get the ServiceManager object
        service_manager = context.ServiceManager
        # Create the Desktop instance
        desktop = service_manager.createInstance("com.sun.star.frame.Desktop")
        return service_manager, desktop
    except Exception, exc:
        if exc.__class__.__name__.endswith('NoConnectException') and _try_start:
            #logging.info('Trying to start UNO server')
            #status = os.system('soffice -invisible -accept="socket,host=localhost,port=2002;urp;"')
            status = os.system('soffice -accept="socket,host=localhost,port=2002;urp;"')
            time.sleep(2)
            #logging.info('status = %d', status)
            return _uno_init(False)
        else:
            #logging.exception("UNO server not started, you should fix that now. "
            #                  "`soffice \"-accept=socket,host=localhost,port=2002;urp;\"` "
            #                  "or maybe `unoconv -l` might suffice")
            raise

class Reader:

    fileName = ''

    def __init__(self, filename):
        #self.fileName = 'file://'+'/home/richard/temp/testje.ods'
        self.fileName = unicode('file://'+filename)

    def openFile(self):
        service_manager, desktop = _uno_init()
        rows = []
        try:
            # load the Document
            # load it hidden, see http://www.sethanil.com/python-for-friends/5
            p=PropertyValue()
            p.Name = 'Hidden'
            p.Value = True
            properties=(p,)
            document = desktop.loadComponentFromURL(self.fileName, "_blank", 0, properties)
            #document = desktop.loadComponentFromURL(self.fileName, "_blank", 0, ())
            controller = document.getCurrentController()
            sheets = document.getSheets()
            #print 'found %d sheets'% sheets.getCount()
            ## iterate on all the spreadsheets in the document
            #enumeration = sheets.createEnumeration()
            #while enumeration.hasMoreElements():
            #    sheet = enumeration.nextElement()
            #    name = sheet.getName()
            #    print "sheet: %s " % name
            enumeration = sheets.createEnumeration()
            sheet = enumeration.nextElement()
            # http://www.experts-exchange.com/Software/Office_Productivity/Office_Suites/Star_OpenOffice/StarOffice_Calc/Q_26238468.html
            # determining the used area
            cursor = sheet.createCursor()
            cursor.gotoStartOfUsedArea(False)
            cursor.gotoEndOfUsedArea(True)
            rangeaddress = cursor.getRangeAddress()
            rows = cursor.getDataArray()
        except Exception:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            document.close(True)
        return rows


class Writer:
    pass
#    fileName = '/tmp/example2.xls'
#
#    wb = None
#    ws = None
#
#    def __init__(self, filename):
#        self.fileName = filename
#        self.wb = xlwt.Workbook()
#        self.ws = self.wb.add_sheet('Qgis Attributes')
#
#    def writeAttributeRow(self, rowNr, attributes):
#        colNr = 0
#        for cell in attributes:
#            if type(cell) == QString:
#                # cast to QVariable
#                # TODO: do this better
#                cell = QVariant(cell)
#            self.ws.write( rowNr, colNr, unicode(cell.toString()) )
#            colNr = colNr+1
#
#    def saveFile(self):
#        self.wb.save(self.fileName)
#
#    def openFile(self):
#        wb = open_workbook('/home/richard/temp/prov/prov.xls')
#        for s in wb.sheets():
#            #print 'Sheet:',s.name
#            for row in range(s.nrows):
#                values = []
#                for col in range(s.ncols):
#                    values.append(s.cell(row,col).value)
#            #print ','.join(values)
#            #print
#

