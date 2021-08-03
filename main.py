from model.wrk import *


if __name__ == '__main__':
    # for x in WrkFactory.getInstance():
    #     print(x)

    wrk = WrkFactory.get_instance(wrk_seconds=[10], wrk_collections=[100])
    for x in wrk:
        if isinstance(x, WrkGroup):
            x.run()
            print(x.get_markdown())

    # print(wrk.getCmd())
    # print(wrk[0].get_markdown())
    # print(wrk[0].get_markdown())
    # wrk.run()n
    # print(wrk.getQps())





