from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def convert(v: float, f: str, t: str) -> float:
    """Convert v of unit f to d of unit t, return d """
    coef = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34,
            "mg": 0.001, "g": 1, "kg": 1000, "oz": 28.3495, "lb": 453.592,
            "c": lambda c: c, "f": lambda f: (f-32) * 5/9, "k": lambda k: k - 273.15, 
            "cc": lambda c: c, "cf": lambda c: c * 9/5 + 32, "ck": lambda c: c + 273.15
    }
    

    if f not in coef or t not in coef:
        raise ValueError(f"Unsupported units: from {f} to {t}")
    elif f in ("c", "f", "k"): # then temperatures
        base: float = coef[f](v)
        dest: float = coef[f"c{t}"](base)
    else:
        base: float = v * coef[f]
        dest: float = base / coef[t]
    return dest

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request, unit_type: str = "length"):
    return templates.TemplateResponse(name="result.html", request=request, context= {"unit_type": unit_type})

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
