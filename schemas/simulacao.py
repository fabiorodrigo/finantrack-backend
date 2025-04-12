from pydantic import BaseModel, Field

class SimulacaoBase(BaseModel):
    moeda: str = Field(..., example="USD", description="Código da moeda estrangeira")
    valor_brl: float = Field(..., gt=0, example=100.0, description="Valor em reais a ser convertido")
    valor_convertido: float = Field(..., gt=0, example=20.0, description="Valor convertido para a moeda desejada")
    cotacao: float = Field(..., gt=0, example=5.0, description="Cotação usada para a conversão")


# Requisições de criação
class SimulacaoCreate(SimulacaoBase):
    class Config:
        schema_extra = {
            "example": {
                "moeda": "USD",
                "valor_brl": 250.00,
                "valor_convertido": 49.50,
                "cotacao": 5.05
            }
        }


# Requisições de atualização (requer id)
class SimulacaoUpdate(SimulacaoBase):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "moeda": "EUR",
                "valor_brl": 500.00,
                "valor_convertido": 93.45,
                "cotacao": 5.35
            }
        }


# Resposta da API
class SimulacaoResponse(SimulacaoUpdate):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "moeda": "BTC",
                "valor_brl": 1000.00,
                "valor_convertido": 0.0021,
                "cotacao": 478000.00
            }
        }
