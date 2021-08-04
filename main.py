from model.wrk import *


if __name__ == '__main__':
    benchmark_suite = BenchmarkSuiteFactory.get_instance()
    benchmark_suite.exec()





