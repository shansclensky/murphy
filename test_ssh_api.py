import unittest
from ssh_api import wait_for_device_avaialbility

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_wait_for_device_avaialbility(self):
       check_avail, ssh_conn = wait_for_device_avaialbility(hostname="10.0.4.14",username="cirros",key_filename="/root/repo/testkey.pem")
       print check_avail
       self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

