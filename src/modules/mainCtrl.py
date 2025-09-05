import pyautogui
import tempfile 
import qrcode
import webbrowser
import os
import socket



class CTL : 
    def __init__ (self) : 
        pass


    def pressKey (self , row) : 
        if row == "next" : 
            pyautogui.press("right")
        else : 
            pyautogui.press("left")



    def qr (self) :
        try : 
            path = tempfile.gettempdir()
            url = f"http://{getPrivateIp()}:8001"

            file_path = os.path.join(path, f"prictl.png")

            q = qrcode.make(url)
            q.save(file_path)
            webbrowser.open(file_path)

            return True

        except Exception as e : 
            return False



    def getPrivateIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip
