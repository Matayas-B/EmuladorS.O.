'''
Created on Nov 27, 2015

@author: bequita
'''
import unittest

from Code.PCB import PCB

class Test(unittest.TestCase):

    def setUp(self):
        self.pcb = PCB("first", None, None)
        self.pcb2 = PCB("second", None, None)
        self.pcb3 = PCB("third", None, None)

    def test_assignPageToBlock(self):
        self.pcb.assignPageToBlock(2, 4)
        self.assertTrue(self.pcb.pagesTable.pagesToBlock[2] == (4,0))
        self.assertTrue(self.pcb.pcbID == 0)
        self.assertTrue(self.pcb2.pcbID == 1)
        self.assertTrue(self.pcb3.pcbID == 2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()