"""Cliente para a API publica de localidades do IBGE."""

from api.http_client import BaseApiClient
from api.settings import IBGE_BASE_URL, REQUEST_TIMEOUT_SECONDS


class IbgeClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(IBGE_BASE_URL, timeout=REQUEST_TIMEOUT_SECONDS)

    def listar_estados(self):
        return self.get("/estados", params={"orderBy": "nome"})

    def listar_municipios_por_uf(self, uf: str):
        return self.get(f"/estados/{uf}/municipios", params={"orderBy": "nome"})

    def buscar_municipio_por_codigo(self, codigo_ibge: int):
        return self.get(f"/municipios/{codigo_ibge}")

    def listar_municipios_por_regiao(self, regiao: int):
        return self.get(f"/regioes/{regiao}/municipios", params={"orderBy": "nome"})

