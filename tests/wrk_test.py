import unittest

from model.config import WrkConfig
from model.wrk import BenchmarkSuiteFactory, WrkGroup


class WrkTest(unittest.TestCase):

    def setUp(self):
        config = WrkConfig(node_url="http://8.210.169.63:8116", seconds=[10], collections=[300], threads=16, timeout=1)
        self.config = config

    def tearDown(self):
        pass

    def test_benchmark_suitek(self):
        benchmark_suite = BenchmarkSuiteFactory.get_instance_by_config(self.config)
        benchmark_suite.exec()

    @staticmethod
    def test_benchmark_suite_by_config():
        benchmark_suite = BenchmarkSuiteFactory.get_instance()
        benchmark_suite.exec()



