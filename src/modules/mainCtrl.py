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



class CTL : 
    def __init__ (self) : 
        pass


    def pressKey (self , row) :
        """
        Press a keyboard key using the pyautogui module to navigate between slides.

        Parameters:
        row (str): 'next' to move to the next slide, any other value to move to the previous slide.
        """

        if row == "next" : 
            pyautogui.press("right")
        else : 
            pyautogui.press("left")



    def qrCreator (self , servicePort : int = 10001) :
        """
        Generate a QR code for a webpage URL based on the local IP and given port,
        save it as 'prictl.png' in the system temporary directory, 
        and automatically open it with the default image viewer
        """

        try : 
            path = tempfile.gettempdir()
            url = f"http://{self.getPrivateIp()}:{servicePort}"

            file_path = os.path.join(path, f"prictl.png")

            q = qrcode.make(url)
            q.save(file_path)


            infoPagePath = os.path.join(path, f"prictlInfo.html")
            webbrowser.open(infoPagePath)

            return True

        except Exception as e : 
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
        code = ""
        for _ in range(4) : 
            code = code + str(random.randint(0 , 9))

        path = tempfile.gettempdir()
        path = os.path.join(path, "priper_code.txt")
        with open(path , "w") as file : 
            file.write(code)


        return code





    def readCode (self) : 
        try :   
            path = tempfile.gettempdir()
            path = os.path.join(path, "priper_code.txt")

            with open(path , "r") as file : 
               file = file.read() 

            return file

        except Exception as e : 
            return None


        
