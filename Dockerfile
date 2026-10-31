# ------------------------------------------------------------------------------
# Imagen base: Python 3.10 en versión slim basada en Debian/Linux
# Mantiene el contenedor ligero, rápido y estable para desarrollo
# ------------------------------------------------------------------------------
FROM python:3.10-slim

# Evita que Python escriba archivos .pyc en el disco del contenedor
ENV PYTHONDONTWRITEBYTECODE=1

# Permite que la salida de la consola (logs y prints) se muestre en tiempo real
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Actualización de dependencias del sistema e instalación de herramientas base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Actualizar el gestor de paquetes pip a su versión más reciente
RUN pip install --upgrade pip

# Copiar únicamente el archivo de requisitos para aprovechar el caché de Docker
COPY requirements.txt /app/

# Instalar las dependencias del proyecto (Django y librerías requeridas)
RUN pip install -r requirements.txt

# Copiar el resto del código fuente del proyecto local al contenedor
COPY . /app/

# Exponer el puerto por defecto en el que se ejecuta el servidor de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]