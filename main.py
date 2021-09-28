import sys

from model.wrk import *


if __name__ == '__main__':
    script_names = []
    if len(sys.argv) != 1:
        for i in range(1, len(sys.argv)):
            script_names.append(sys.argv[i])

    benchmark_suite = BenchmarkSuiteFactory.get_instance_by_scripts(script_names)
    benchmark_suite.exec()





