import datetime
import unittest


from model.wrk import BenchmarkSuite


class WrkTest(unittest.TestCase):

    def setUp(self):
        suite = BenchmarkSuite()
        self.suite = suite

    def tearDown(self):
        pass

    def test_benchmark_suitek(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S.%f')
        print(str(now))

