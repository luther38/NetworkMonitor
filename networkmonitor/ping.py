import platform
#from subprocess import DEVNULL, STDOUT, call, run
import subprocess

from .terminal import TerminalOutput

class Ping:

    def __init__(self):
        self.Status:str = ''
        self.ms:int     = -1
        self.URI:str    = ''
        pass

    def PingHost(self, hostname:str):

        self.URI = hostname

        self.__CleanURI()

        cmd = self.__GetCommand()

        #return call(cmd, stdout=DEVNULL, stderr=STDOUT)
        try:
            d = subprocess.run(cmd, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)

            self.__ProcessReturnCode(d.returncode)
            self.__ProcessTravelTime(d.stdout)
            #d = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            #print(d)
            
        except:
            pass

    def __CleanURI(self):
        if self.URI.lower().__contains__('http') == True:
            self.URI = self.URI.replace("http://", "")
        
        if self.URI.lower().__contains__('https://') == True:
            self.URI = self.URI.replace()

    def __GetCommand(self):
        if platform.system().lower() == "windows":       
            param = '-n'
        else:
            param = '-c'
        pass

        return ['ping', param, '1', self.URI]
 
    def __ProcessReturnCode(self, returncode:int ):
        if returncode == 0:
            self.Status = 'Online'        
        else:
            self.Status = 'Offline'

    def __ProcessTravelTime(self, stdout:str):
        if platform.system().lower() == 'windows':
            pass
        else:
            i = stdout.find("time=",0, stdout.__len__())
            print(i)