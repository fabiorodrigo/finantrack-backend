from fastapi import FastAPI, HTTPException
from typing import List
from schemas.simulacao import SimulacaoCreate, SimulacaoUpdate, SimulacaoResponse
from model import simulacao

app = FastAPI(title="FinanTrack API")

@app.get("/")
def home():
    return {"mensagem": "API FinanTrack ativa"}

@app.get("/simulacoes", response_model=List[SimulacaoResponse])
def get_all():
    return simulacao.listar_simulacoes()

@app.post("/simulacao", response_model=SimulacaoResponse)
def criar(sim: SimulacaoCreate):
    return simulacao.criar_simulacao(sim)

@app.put("/simulacao/{id}", response_model=SimulacaoResponse)
def atualizar(id: int, sim: SimulacaoCreate):
    if not simulacao.existe_simulacao(id):
        raise HTTPException(status_code=404, detail="Simulação não encontrada")
    return simulacao.atualizar_simulacao(id, sim)

@app.delete("/simulacao/{id}", status_code=204)
def deletar(id: int):
    if not simulacao.existe_simulacao(id):
        raise HTTPException(status_code=404, detail="Simulação não encontrada")
    simulacao.deletar_simulacao(id)
