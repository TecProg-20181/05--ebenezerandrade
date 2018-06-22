import unittest
from diskspace import *
DIR = "/home/ebenezer/TecProg/05--ebenezerandrade/test/03--ebenezerandrade

class DiskspaceTests(unittest.TestCase):
    
    # test case byts of block size of B
    def test_bytes_to_readable(self):
        blocks = 0
        result = bytes_to_readable(blocks)
        self.assertEqual('0.00B', result)

    # test case byts of block size of B
    def test_bytes_to_readable_B(self):
        blocks = 1
        result = bytes_to_readable(blocks)
        self.assertEqual('512.00B', result)

    # test case byts of block size of Kb
    def test_bytes_to_readable_Kb(self):
        blocks = 1000
        result = bytes_to_readable(blocks)
        self.assertEqual('500.00Kb', result)
    
    # test case byts of block size of Mb
    def test_bytes_to_readable_Mb(self):
        blocks = 10000
        result = bytes_to_readable(blocks)
        self.assertEqual('4.88Mb', result)

    # test case byts of block size of Gb
    def test_bytes_to_readable_Gb(self):
        blocks = 10000000
        result = bytes_to_readable(blocks)
        self.assertEqual('4.77Gb', result)

    # test case byts of block size of Tb
    def test_bytes_to_readable_Tb(self):
        blocks = 10000000000
        result = bytes_to_readable(blocks)
        self.assertEqual('4.66Tb', result)
        
if __name__ == "__main__":
     unittest.main()

        
    

