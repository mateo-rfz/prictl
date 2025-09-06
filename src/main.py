#web server imports
from fastapi import (FastAPI , Request , Response , Cookie)
from fastapi import templating
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



# run fastapi app
import uvicorn



#local modules 
from modules import mainCtrl
from modules import infoPageGenerator




ctl = mainCtrl.CTL()



app = FastAPI()
templates = Jinja2Templates(directory="templates")










@app.get("/")
def main(request: Request , code_cookie: str = Cookie(None, alias="code") , row: str = None , code: str = None):

    #read generated pcode from file
    pcode = ctl.readCode()

    if code == pcode:
        """
        check code for auth and if valid 
        app set coockie
        """
        response = templates.TemplateResponse("home.html", {"request": request})
        response.set_cookie(key="code", value= str(pcode) , max_age=100000, path="/")
        return response

    
    # check coockie value to pcode
    if code_cookie == pcode:
        if row in ("next", "prev"):
            ctl.pressKey(row)
        return templates.TemplateResponse("home.html", {"request": request})


    return templates.TemplateResponse("login.html", {"request": request})







@app.get("/health") 
def health () : 
    return 200






if __name__ == "__main__" :
    ctl.randomCodeGenerator()
    pcode = ctl.readCode()
    infoPageGenerator.Generaotr(str(pcode))
    ctl.qrCreator(servicePort=10001)
    uvicorn.run("main:app" , host="0.0.0.0" , port=10001 , reload=False)
