# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requeridos al contenedor
COPY main.py .
COPY urls.txt .

# Instala las dependencias
RUN pip install requests

# Comando para ejecutar el script
CMD ["python", "main.py"]