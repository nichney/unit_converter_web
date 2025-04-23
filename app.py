from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def convert(v: float, f: str, t: str) -> float:
    """Convert v of unit f to d of unit t, return d """
    coef = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.34}

    if f not in coef or t not in coef:
        raise ValueError(f"Unsupported units: from {f} to {t}")

    base: float = v * coef[f]
    dest: float = base / coef[t]
    return dest

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse(name="result.html", request=request)

@app.post("/", response_class=HTMLResponse)
async def handle_convertion(request: Request, value: float = Form(), from_unit: str = Form(), to_unit: str = Form()):
    try:
        converted = convert(value, from_unit, to_unit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = f"{value} {from_unit} = {converted} {to_unit}"
    return templates.TemplateResponse(
            name="result.html", request=request, context={"result": result}
            )
