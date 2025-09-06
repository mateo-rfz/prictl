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
