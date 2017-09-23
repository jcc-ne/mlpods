""" First execute ./build_test_docker.sh to build test_pod docker image """

import sys
sys.path.insert(0, '../')

from funpod import FunPod
import unittest
import os


class TestFunPod(unittest.TestCase):
    def setUp(self):
        kwargs = {'volumes': {os.getcwd(): {'bind': '/app', 'mode': 'rw'}}}
        self.funpod = FunPod('test_pod', **kwargs)
        self.funpod_connector = self.funpod.connector

    @unittest.skip("demonstrating skipping")
    def test_fileobj(self):
        f = open('test1.txt', 'r')
        gen = self.funpod_connector.client_generator(fileobj=f)
        self.assertEqual(gen.next().strip(), '1')
        self.assertEqual(gen.next().strip(), '2')
        self.assertEqual(gen.next(), '3')
        f.close()

    def test_volume_mount(self):
        with open('test1.txt', 'w') as f:
            f.write('1\n2\n3')
        gen = self.funpod_connector.client_generator(filepath='test1.txt',
                                                     start_pod=False)
        self.assertEqual(gen.next().strip(), '1')
        self.assertEqual(gen.next().strip(), '2')
        self.assertEqual(gen.next(), '3')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
