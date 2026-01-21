FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Inicia o servidor acessível externamente e em modo debug
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]