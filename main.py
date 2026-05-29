from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

#this will find the static file directory and other front end stuff
app.mount("/static", StaticFiles(directory="static"), name="static")

#where my html files to get
templates = Jinja2Templates(directory="templates") #i called the template folder here


#homepage html stuff
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    #this is where i pass the html file
    return templates.TemplateResponse(request=request, name="index.html")

#receiving "of pdf 
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    #try to read filename
    filename = file.filename
    
    #pdf extration, AI, Anki code will go
    return{
        "message": f"Successfully received file {filename}",
        "status": "success",
    }