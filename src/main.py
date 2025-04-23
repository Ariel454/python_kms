# src/main.py

from fastapi import FastAPI
from src.shared.app_config import AppConfig
from src.shared.di_container import DIContainer

# Ajuste del path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Variable global que uvicorn necesita
app = FastAPI()

# 🔧 Configuración e inyección de dependencias
app_config = AppConfig()
di_container = DIContainer(config=app_config, app=app)

# 🏁 Ejecutar con: python3 src/main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
