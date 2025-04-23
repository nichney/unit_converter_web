from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse(name="result.html", request=request)

@app.post("/", response_class=HTMLResponse)
async def handle_convertion(request: Request, value: float = Form(), from_unit: str = Form(), to_unit: str = Form()):
    converted = value*2 # TODO: make the conversion function
    result = f"{value} {from_unit} = {converted} {to_unit}"
    return templates.TemplateResponse(
            name="result.html", request=request, context={"result": result}
            )
