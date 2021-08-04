import unittest

from model.config import WrkConfig
from model.wrk import WrkFactory, WrkGroup


class WrkTest(unittest.TestCase):

    def setUp(self):
        config = WrkConfig(node_url="http://8.210.169.63:8116", seconds=[10], collections=[300], threads=16, timeout=1)
        self.config = config

    def tearDown(self):
        pass

    def test_wak(self):
        wrk = WrkFactory.get_instance_by_config(self.config)
        for x in wrk:
            if isinstance(x, WrkGroup):
                x.run()
                print(x.get_markdown())

    def test_config(self):
        wrk = WrkFactory.get_instance()
        for x in wrk:
            if isinstance(x, WrkGroup):
                x.run()
                print(x.get_markdown())