'''
Created on 13/12/2013

@author: victorzinho
'''
import unittest
import utils
from qgis.core import QGis
from mock import Mock


class Test(unittest.TestCase):

    def testGetFieldNames(self):
        originalNames = ['ID', 'NAME']
        field0 = self._mockField(originalNames[0])
        field1 = self._mockField(originalNames[1])
        fields = [field0, field1]
        layer = Mock()
        layer.dataProvider().fields.return_value = fields
        fieldNames = utils.fieldNames(layer)

        assert fieldNames == originalNames

    def _mockField(self, name):
        field = Mock()
        field.name.return_value = name
        return field

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
