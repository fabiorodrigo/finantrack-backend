# 💱 FinanTrack – Simulador de Conversão de Moedas

O **FinanTrack** é uma aplicação web que permite simular a conversão de valores em reais (BRL) para moedas estrangeiras como **Dólar (USD)**, **Euro (EUR)** e **Bitcoin (BTC)**. O sistema utiliza cotações em tempo real através de uma API externa e permite salvar, editar e excluir simulações realizadas. Também é possível visualizar a evolução das moedas em um gráfico de histórico de cotações.

---

## 🧱 Estrutura do Projeto

```
FinanTrack/
├── finantrack-frontend/             # Repositório principal (este)
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.override.yml
│   └── README.md
│
├── finantrack-backend/             # Repositório auxiliar (API)
│   ├── app.py
│   ├── model/
│   ├── schemas/
│   ├── Dockerfile
│   └── requirements.txt
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados

### Passos

1. Clone os dois repositórios lado a lado:

```bash
git clone https://github.com/seu-usuario/finantrack-frontend.git
git clone https://github.com/seu-usuario/finantrack-backend.git
```

2. Acesse o diretório do frontend:

```bash
cd finantrack-frontend
```

3. Execute o projeto:

```bash
docker-compose up --build
```

4. Acesse em seu navegador:

- Interface Web: http://localhost:3000
- API (Swagger): http://localhost:8000/docs

---

## 🧪 Rotas da API

| Método | Rota                  | Descrição                            |
|--------|------------------------|----------------------------------------|
| GET    | /simulacoes            | Lista todas as simulações             |
| POST   | /simulacao             | Cria uma nova simulação               |
| PUT    | /simulacao/{id}        | Atualiza uma simulação existente      |
| DELETE | /simulacao/{id}        | Exclui uma simulação                  |

---

## 📌 Observações

- O banco de dados `simulacoes.db` é criado automaticamente na primeira execução.
- O `Dockerfile` já está configurado para rodar `uvicorn app:app`.

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.

---

## **Pós-Graduação em Engenharia de Software da PUC-Rio**.
- Disciplina: **Arquitetura de Software**
- Desenvolvido por **Fábio Araújo**  
📧 Email: fabiorodrigo.puc@gmail.com
