from fastapi import (FastAPI , Request)

from fastapi import templating
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn



#local modules 
from modules import mainCtrl



app = FastAPI()
templates = Jinja2Templates(directory="templates")




@app.get("/")
def main (request : Request , row = None) : 
    if row == None : 
        return templates.TemplateResponse("home.html" , {"request":request})

    if row == "next" or row == "prev":
        mainCtrl.CTL().pressKey(row)
    












if __name__ == "__main__" : 
    uvicorn.run("main:app" , host="0.0.0.0" , port=8001 , reload=True)
