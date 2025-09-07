# use for press keyboard keys
import pyautogui

# use for find temporary dir for save qrcode picture
import tempfile 

# use for generate qrcode 
import qrcode

# use for open qrcode picture automatically
import webbrowser

# use for combine qrcode file name and store path
import os

# use for get local ip address
import socket

# use for generate pincode
import random



# local imports 
from modules import config
from modules import loger


class CTL : 
    def __init__ (self , servicePort : int = 10001) : 
        self.log = loger.Loger()
        self.servicePort = servicePort





    def pressKey (self , row) :
        """
        Press a keyboard key using the pyautogui module to navigate between slides.

        Parameters:
        row (str): 'next' to move to the next slide, any other value to move to the previous slide.
        """
        try : 
            if row == "next" : 
                pyautogui.press(config.NEXTKEY)
                self.log.add("EMULATE PRESS KEY" , f"press {config.NEXTKEY}")


            else : 
                pyautogui.press(config.PREVKEY)
                self.log.add("EMULATE PRESS KEY" , f"press {config.PREVKEY}")


        except Exception as e : 
            self.log.add("ERROR IN EMULATE PRESS KEY" , e)
            






    def qrCreator (self) :
        """
        Generate a QR code for a webpage URL based on the local IP and given port,
        save it as 'prictl.png' in the system temporary directory, 
        and automatically open it with the default image viewer
        """

        try : 
            tempDirPath = tempfile.gettempdir()
            url = f"http://{self.getPrivateIp()}:{self.servicePort}"

            qrCodePath = os.path.join(tempDirPath, f"prictl.png")
            

            q = qrcode.make(url)
            q.save(qrCodePath)

            self.log.add("SAVE QRCODE" , f"Path : {qrCodePath}")


            infoPagePath = os.path.join(tempDirPath, f"prictlInfo.html")

            self.log.add("SAVE PAGE INFO" , f"Path {infoPagePath}")

            #open default html viewer automatically
            webbrowser.open(infoPagePath)
            
            return True

        except Exception as e : 
            self.log.add("ERROR IN qrCreator()" , e) 
            return False






    def getPrivateIp (self):
        """
        Return the local IP address of the machine by creating a UDP socket
        and connecting to an external host (without sending data).
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            s.connect(("8.8.8.8", 80)) 
            ip = s.getsockname()[0] 

        finally:
            s.close()
            
        return ip









    def randomCodeGenerator (self) : 
        """
        Create random four-digit pincode to auth client by random module
        store pincode on prictl_code.txt
        """
        try : 
            code = ""
            for _ in range(4) : 
                code = code + str(random.randint(0 , 9))



            path = tempfile.gettempdir()
            path = os.path.join(path, "prictl_code.txt")


            with open(path , "w") as file : 
                file.write(code)
            

            self.log.add("SAVE PINCODE" , f"Path {path}")
            return code

        except Exception as e : 
            self.log.add("ERROR IN GENERATE PINCODE" , e)








    def readCode (self) :
        """
        Read pincode from prictl_code.txt
        """
        try :   
            path = tempfile.gettempdir()
            path = os.path.join(path, "prictl_code.txt")

            with open(path , "r") as file : 
               file = file.read() 
            
            self.log.add("READ PINCODE" , f"from {path}")
            return file

        except Exception as e : 
            self.log.add("ERROR IN READ PINCODE" , e)
            return None


