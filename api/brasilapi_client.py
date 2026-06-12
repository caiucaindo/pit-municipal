"""Cliente para endpoints publicos do IBGE expostos pela BrasilAPI."""

from api.http_client import BaseApiClient
from api.settings import BRASILAPI_BASE_URL, REQUEST_TIMEOUT_SECONDS


class BrasilApiClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(BRASILAPI_BASE_URL, timeout=REQUEST_TIMEOUT_SECONDS)

    def listar_ufs(self):
        return self.get("/ibge/uf/v1")

    def listar_municipios_por_uf(self, uf: str):
        return self.get(f"/ibge/municipios/v1/{uf.upper()}")

