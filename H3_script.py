
import time
import psutil
import datetime
import json
import config


class MyClass(object):
	"""class information"""
#	def startup(self):
#		self.cpu_per = None
#		self.used_mem = None
#		self.virtual_mem = None
#		self.disk_usage = None
#		self.net_count =None
#		self.boot = None
#		self.counter = 0

	def __init__(self):
		self.cpu_per=str(psutil.cpu_percent(interval=None))
		self.used_mem=str(psutil.virtual_memory())
		self.virtual_mem=str(psutil.virtual_memory().percent)
		self.disk_usage=str(psutil.disk_usage('/'))
		self.net_count=str(psutil.net_io_counters())
		self.boot = str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
		self.counter=3;

 
	def Writefile(self, counter):
		self.counter += 1
		"""write to file"""
		f = open("test.txt", "a")
		f.write ("t\t\t\t\t\t\t\SNAPSHOT" + str(self.counter))
		f.write ("\tcpu_percent:" + self.cpu_per + "\n")
		f.write ("\tmem_used.total;" + self.used_mem + "\n")
		f.write ("\tvirtual_memory:" + self.virtual_mem + "\n")
		f.write ("\tdisk_usage:" + self.disk_usage + "\n")
		f.write ("\tnet_io_counters:" + self.net_count + "\n")
		f.write ("\tdatetime:" + self.boot + "\n")
		print(self.counter);
		f.close()

	def WriteJson(self, counter):
		self.counter += 1
		'''write to json file'''
		data = {'SNAPSHOT': str(self.counter), 'cpu_percent' : self.cpu_per,'mem_used.total': self.used_mem, 'virtual_memory': self.virtual_mem, 'disk_usage': self.disk_usage, 'net_io_counters' : self.net_count, 'datetime' : self.boot}
		f = open('data.json', 'a')
		json.dump(data, f, indent=4, ensure_ascii=False)
		print(self.counter);
		f.close()


trulala = MyClass()
#trulala.Writefile()
#trulala.WriteJson();


while True:
#    trulala.__init__()
    obj = MyClass();
    counter=0;
    if config.Ftype == "txt":
       trulala.Writefile(counter)
    else:
        trulala.WriteJson(counter)
    if trulala.counter >= config.checks:
        break
    time.sleep(config.sleep)

























