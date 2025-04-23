# Dockerfile

FROM python:3.13-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

# Puerto en el que corre FastAPI (por defecto 8000)
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
