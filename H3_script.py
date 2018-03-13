"""homework"""
# pylint: disable=invalid-name
import time
import json
import psutil
import config


class MyClass(object):
    """class information"""
# def startup(self):
# self.cpu_per = None
# self.used_mem = None
# self.virtual_mem = None
# self.disk_usage = None
# self.net_count =None
# self.boot = None
# self.counter = 0

    def __init__(self):
        """init something"""
        self.cpu_per = str(psutil.cpu_percent(interval=None))
        self.used_mem = str(psutil.virtual_memory())
        self.virtual_mem = str(psutil.virtual_memory().percent)
        self.disk_usage = str(psutil.disk_usage('/'))
        self.net_count = str(psutil.net_io_counters())
        self.boot = str(time.ctime())
        self.counter = 1

    def Writefile(self):
        """write to file"""
        f = open("test.txt", "w")
        while True:
            f.write("\tSNAPSHOT" + str(self.counter))
            f.write("\tcpu_percent:" + self.cpu_per + "\n")
            f.write("\tmem_used.total;" + self.used_mem + "\n")
            f.write("\tvirtual_memory:" + self.virtual_mem + "\n")
            f.write("\tdisk_usage:" + self.disk_usage + "\n")
            f.write("\tnet_io_counters:" + self.net_count + "\n")
            f.write("\tdatetime:" + self.boot + "\n")
            print(str(self.counter))
            time.sleep(config.SLEEP)
            if self.counter == config.CHECKS:
                f.close()
                break
            self.counter += 1

    def WriteJson(self):
        '''write to json file'''
        f = open('data.json', 'w')
        while True:
            data = {
                'SNAPSHOT': str(self.counter),
                'cpu_percent': self.cpu_per,
                'mem_used.total': self.used_mem,
                'virtual_memory': self.virtual_mem,
                'disk_usage': self.disk_usage,
                'net_io_counters': self.net_count,
                'datetime': self.boot
            }
            json.dump(data, f, indent=4, ensure_ascii=False)
            print(str(self.counter))
            time.sleep(config.SLEEP)
            if self.counter == config.CHECKS:
                f.close()
                break
            self.counter += 1


TRULALA = MyClass()

if config.FTYPE == "txt":
    TRULALA.Writefile()
else:
    TRULALA.WriteJson()
