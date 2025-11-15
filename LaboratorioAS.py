# app.py o LaboratorioAS.py
from fastapi import FastAPI

app = FastAPI(
    title="API de Valery Tribales y Eilin Carrillo",
    description="Ejemplo con parámetros por dominio (query)",
    version="1.0.1"
)

@app.get("/")
async def root():
    return {"mensaje": "¡Bienvenidos a la API de Valery Tribales, Eilin Carrillo y Karla Vargas!"}

# Ruta que recibe parámetro por URL (query)
@app.get("/hello")
async def decir_hola(name: str = "invitado"):
    return {"saludo": f"Hola, {name}! Te saludan Valery Tribales, Eilin Carrillo y Karla Vargas "}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run("LaboratorioAS:app", host="0.0.0.0", port=port)





