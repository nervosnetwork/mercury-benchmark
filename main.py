from model.wrk import *


if __name__ == '__main__':
    wrk = WrkFactory.get_instance()
    for x in wrk:
        if isinstance(x, WrkGroup):
            x.run()
            print(x.get_markdown())





