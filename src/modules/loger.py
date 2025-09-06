import datetime 



class Loger : 
    def __init__ (self , logFileName = "prictl_log.log") : 
        self.now = None 
        # update value with __updateTime()

        self.file = open(logFileName , "a")



    def __del__ (self) : 
        self.file.close()


    
    def __updateTime (self) : 
        self.now = datetime.datetime.now()




    def add (self , action , *p) : 
        # call __updateTime to update self.now variable
        self.__updateTime()

        try : 
            self.file.write(f"{self.now} : {action} - {p}\n")
        
        except Exception as e : 
            print(e)
            return False
