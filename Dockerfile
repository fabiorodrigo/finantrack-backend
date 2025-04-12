# Usamos a imagem oficial do Python 3.11 com tamanho reduzido
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container como /app
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala todas as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos e pastas do projeto para o diretório de trabalho do container
COPY . .

# Comando para iniciar a aplicação com Uvicorn (servidor ASGI)
# app:app → refere-se ao arquivo app.py e à instância FastAPI chamada `app`
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
