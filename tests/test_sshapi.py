import sys
import unittest
sys.path.append("/repo/ssh_api.py")
import wait_for_device_avaialbility
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_wait_for_device_avaialbility(self):
        check_avail= wait_for_device_avaialbility(hostname="10.0.4.16",port=22,username="cirros",key_filename="/root/repo/testkey.pem")
 
 
if __name__ == '__main__':
    unittest.main()
