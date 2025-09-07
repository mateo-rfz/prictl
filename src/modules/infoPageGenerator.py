# use for find temp dir on systems
import tempfile

# use for combine filename and path
import os



#local import 
from modules import loger
from modules import mainCtrl




class Generaotr  : 
    def __init__ (self , code : str = "1111") :
        self.log = loger.Loger()

        # read raw pageInfo from templates/info.html
        self.page = self.__readInfoPageFile()
       
        # pincode for auth
        self.code = code
        self.exitUrl = f"http://{mainCtrl.CTL().getPrivateIp()}:{mainCtrl.CTL().servicePort}/exit"

        tempDirPath = tempfile.gettempdir()
        self.tempDirPath = os.path.join(tempDirPath, "prictlInfo.html") 



        self.qrPath = os.path.join(tempDirPath , "prictl.png")
        
        self.__generator()
        self.__saveReadyToUseInfoPage()

 



    def __readInfoPageFile (self) : 
        try : 
            with open("templates/info.html" , "r") as file : 
                file = file.read()

            return file

        except Exception as e :
            self.log.add("ERROR IN READ RAW INFO PAGE" , e)
            return ""



    def __saveReadyToUseInfoPage (self) : 
        try : 
            with open(self.tempDirPath , "w") as file : 
                file.write(self.page)

            return True

        except Exception as e : 
            self.log.add("ERROR IN MAKE READY TO USE PAGE INFO" , e)
            return False
        





    
    def __generator (self) :
        self.page = self.page.replace("%%%%" , self.code).replace("&&&&" , self.qrPath).replace("LINK" , self.exitUrl)




