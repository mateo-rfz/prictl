import tempfile
import os





class Generaotr  : 
    def __init__ (self , code : str = "1111") :
        self.page = self.__readInfoPageFile()
        self.code = code

        path = tempfile.gettempdir()
        self.path = os.path.join(path, "prictlInfo.html") 



        self.qrPath = os.path.join(path , "prictl.png")
        
        self.__gnr()
        self.__saveReadyToUseInfoPage()

 



    def __readInfoPageFile (self) : 
        with open("templates/info.html" , "r") as file : 
            file = file.read()

        return file



    def __saveReadyToUseInfoPage (self) : 
        with open(self.path , "w") as file : 
            file.write(self.page)
        






    def __gnr (self) :
        self.page = self.page.replace("%%%%" , self.code).replace("&&&&" , self.qrPath)




