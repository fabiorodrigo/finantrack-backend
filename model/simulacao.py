from model.base import cursor, conn
from schemas.simulacao import SimulacaoCreate, SimulacaoUpdate, SimulacaoResponse

def criar_simulacao(sim: SimulacaoCreate) -> SimulacaoResponse:
    cursor.execute("""
        INSERT INTO simulacoes (moeda, valor_brl, valor_convertido, cotacao)
        VALUES (?, ?, ?, ?)""",
        (sim.moeda, sim.valor_brl, sim.valor_convertido, sim.cotacao))
    conn.commit()
    sim_id = cursor.lastrowid
    return SimulacaoResponse(id=sim_id, **sim.dict())

def listar_simulacoes() -> list[SimulacaoResponse]:
    cursor.execute("SELECT * FROM simulacoes")
    return [SimulacaoResponse(id=r[0], moeda=r[1], valor_brl=r[2],
                              valor_convertido=r[3], cotacao=r[4])
            for r in cursor.fetchall()]

def atualizar_simulacao(id: int, sim: SimulacaoUpdate) -> SimulacaoResponse:
    cursor.execute("""
        UPDATE simulacoes
        SET moeda=?, valor_brl=?, valor_convertido=?, cotacao=?
        WHERE id=?""",
        (sim.moeda, sim.valor_brl, sim.valor_convertido, sim.cotacao, id))
    conn.commit()
    return SimulacaoResponse(id=id, **sim.dict())

def deletar_simulacao(id: int):
    cursor.execute("DELETE FROM simulacoes WHERE id=?", (id,))
    conn.commit()

def existe_simulacao(id: int) -> bool:
    cursor.execute("SELECT 1 FROM simulacoes WHERE id=?", (id,))
    return cursor.fetchone() is not None