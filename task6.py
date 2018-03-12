"""task6"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
import sys
import site
import os
import json
import pip
import yaml


class MyClass(object):
    """class information"""
    def startup(self):
        """Self names"""
        self.version = None
        self.virtual_env = None
        self.exec_loc = None
        self.pip_loc = None
        self.path = None
        self.packages = None
        self.site_pack_loc = None

    def __init__(self):
        """init information"""
        self.version = str(sys.version)
        self.virtual_env = str(sys.prefix)
        self.exec_loc = str(sys.executable)
        self.pip_loc = str(pip.__path__)
        self.path = str(os.environ['PATH'])
        self.packages = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
        self.site_pack_loc = str(site.getsitepackages())

# def Writefile(self):
# """write to file"""
# f = open("test.txt", "w")
# f.write ("\tThe Python version is: " + self.version + "\n")
# f.write ("\tThe Python name :" + self.name + "\n")
# f.write ("\tThe Python virtual environment is :" + self.virtual_env + "\n")
# f.write ("\tThe Python executable location is :" + self.exec_loc + "\n")
# f.write ("\tpip_loc:" + self.pip_loc + "\n")
# f.write ("\tpackages:" + self.packages + "\n")
# f.write ("\tThe Python Site packages:" + self.site_pack_loc + "\n")
# f.close()

    def WriteJson(self):
        '''write to json file'''
        data = {
            'The Python version is': str(self.version),
            'The Python virtual environment is': self.virtual_env,
            'The Python executable location is': self.exec_loc,
            'The Python pip location is': self.pip_loc,
            'The PYTHONPATH are': self.path,
            'The Python packages are': self.packages,
            'The Python Site packages is located': self.site_pack_loc
            }
        f = open('data.json', 'w')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()
        print("json file was created")

    def WriteYaml(self):
        '''write to yaml file'''
        data = {
            'The Python version is': str(self.version),
            'The Python virtual environment is': self.virtual_env,
            'The Python executable location is': self.exec_loc,
            'The Python pip location is': self.pip_loc,
            'The PYTHONPATH are': self.path,
            'The Python packages are': self.packages,
            'The Python Site packages is located': self.site_pack_loc
            }
        with open('data.yaml', 'w') as ya:
            yaml.dump(data, ya, default_flow_style=False)
            ya.write("\n")
        print("yaml file was created")


trulala = MyClass()
trulala.WriteYaml()
trulala.WriteJson()
