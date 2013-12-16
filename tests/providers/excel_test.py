'''
Created on 13/12/2013

@author: victorzinho
'''
import unittest
import os
import tempfile
from providers.excel import Reader, Writer

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
SAMPLE = os.path.join(DATA_DIR, 'sample.xls')
EMPTY = os.path.join(DATA_DIR, 'empty.xls')


class Test(unittest.TestCase):
    def testReadCorrectFile(self):
        reader = Reader(SAMPLE)
        rows = reader.openFile()

        # 6 rows
        assert len(rows) == 6
        for row in rows:
            # 3 columns
            assert len(row) == 3

    def testReadEmptyFile(self):
        reader = Reader(EMPTY)
        rows = reader.openFile()
        assert len(rows) == 0

    def testWriteCorrectFile(self):
        _, filename = tempfile.mkstemp('.xls')
        writer = Writer(filename)
        row0 = ['ID', 'NUMBER']
        row1 = ['0', '42']
        writer.writeAttributeRow(0, row0)
        writer.writeAttributeRow(1, row1)
        writer.saveFile()

        reader = Reader(filename)
        rows = reader.openFile()
        assert len(rows) == 2
        assert rows[0] == row0
        assert rows[1] == row1

        os.remove(filename)

    def testWriteEmptyFile(self):
        _, filename = tempfile.mkstemp('.xls')
        writer = Writer(filename)
        writer.saveFile()

        reader = Reader(filename)
        rows = reader.openFile()
        assert len(rows) == 0

        os.remove(filename)

    def testWriteNullCell(self):
        _, filename = tempfile.mkstemp('.xls')
        writer = Writer(filename)
        row0 = ['ID', 'NUMBER']
        row1 = ['0', None]
        writer.writeAttributeRow(0, row0)
        writer.writeAttributeRow(1, row1)
        writer.saveFile()

        reader = Reader(filename)
        rows = reader.openFile()
        assert rows[1][1] == 'NULL'

        os.remove(filename)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
