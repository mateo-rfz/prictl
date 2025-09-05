import keyboard






class CTL : 
    def __init__ (self) : 
        pass






    def pressKey (self , row) : 
        if row == "next" : 
            keyboard.send("right")
        else : 
            keyboard.send("left")
