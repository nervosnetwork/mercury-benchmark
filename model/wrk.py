import os


class WrkScript(object):
    def __init__(self, script_name, script_dir):
        self.__script_name = script_name
        self.__script_dir = script_dir
        self.__wrk_script = 'wrk -t16 -c{} -d{}s -T1s --script={} --latency http://8.210.169.63:8116'

    def get_script_path(self):
        return os.path.join(self.__script_dir, self.__script_name)

    def get_cmd(self, seconds=60, collections=300):
        path = self.get_script_path()
        return self.__wrk_script.format(collections, seconds, path)


class WrkGroup(WrkScript):
    def __init__(self, name, script_name, script_dir):
        self.__name = name
        self.__group = []
        self.__markdown = "## {}\n### 压测脚本\n```lua\n{}\n```\n\n### 压测命令\n```shell\n$ {}\n" \
                          "```\n\n {} \n\n### 压测结果\n {} \n\n"

        super(WrkGroup, self).__init__(script_name, script_dir)

    def get_script_file(self):
        path = self.get_script_path()
        with open(path, "r") as f:
            data = f.read()  # 读取文件
            return data

    def append(self, wrk):
        self.__group.append(wrk)

    def get_markdown(self):
        data = ""
        for x in self.__group:
            if isinstance(x, Wrk):
                data = data + x.get_markdown()

        return self.__markdown.format(self.__name, self.get_script_file(), self.get_cmd(), data,
                                      self.get_table())

    def get_table(self):
        collection_group = {}
        seconds = {}
        for x in self.__group:
            if isinstance(x, Wrk):
                if x.collections not in collection_group:
                    collection_group[x.collections] = []
                if x.seconds not in seconds:
                    seconds[x.seconds] = x.seconds

                collection_group.get(x.collections).append(x)

        # todo 重构为根据 key 来决定表头内容
        # header = "|  | 1min | 5min | 15min |\n| --- | --- | --- | --- |\n"
        # table = table.join(header)

        header = "|  | "
        header_separator = "| --- |"
        for x in seconds:
            header = header + str(x) + "seconds | "
            header_separator = header_separator + " --- |"

        table = header + "\n" + header_separator + "\n"

        for collections in collection_group.keys():
            line = "| " + str(collections) + " | "
            for x in collection_group.get(collections):
                if isinstance(x, Wrk):
                    line = line + str(x.get_qps()) + " | "

            table = table + line + "\n"

        return table

    def run(self):
        for x in self.__group:
            if isinstance(x, Wrk):
                x.run()


class Wrk(WrkScript):

    def __init__(self, seconds, collections, script_name, script_dir):
        self.__seconds = seconds
        self.__collections = collections
        self.__result = ""
        self.__markdown = "### {} seconds {} collections\n```shell\n\n {} \n\n```\n\n"

        super(Wrk, self).__init__(script_name, script_dir)

    def get_qps(self):
        if self.__result == "":
            return 0.0
        lines = self.__result.splitlines()
        qps = lines[len(lines) - 2]
        return float(qps.replace("Requests/sec:", "").strip())

    def get_markdown(self):
        return self.__markdown.format(self.__seconds, self.__collections, self.__result)

    def run(self):
        cmd = self.get_cmd(self.__seconds, self.__collections)
        process = os.popen(cmd)
        output = process.read()
        process.close()

        self.__result = output

    @property
    def seconds(self):
        return self.__seconds

    @property
    def collections(self):
        return self.__collections


class WrkFactory(object):
    # todo 重构为读取文件
    script_names = ["get_balance.lua"]
    script_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "script")
    wrk_instance = []

    @classmethod
    def get_instance(cls, wrk_seconds=[60, 300, 900], wrk_collections=[300, 1000]):
        if len(cls.wrk_instance) == 0:
            for x in cls.script_names:
                group = WrkGroup(name=x, script_name=x, script_dir=cls.script_dir)
                cls.wrk_instance.append(group)
                for y in wrk_seconds:
                    for z in wrk_collections:
                        wrk = Wrk(seconds=y, collections=z, script_name=x, script_dir=cls.script_dir)
                        group.append(wrk)

        return cls.wrk_instance
