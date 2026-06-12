"""Cliente HTTP pequeno para padronizar chamadas com Requests."""

from dataclasses import dataclass
from time import perf_counter
from typing import Any

import requests


@dataclass(frozen=True)
class ApiResult:
    """Resposta HTTP acompanhada do tempo medido pelo teste."""

    response: requests.Response
    elapsed_seconds: float

    @property
    def status_code(self) -> int:
        return self.response.status_code

    def json(self) -> Any:
        return self.response.json()


class BaseApiClient:
    """Wrapper simples sobre requests.Session para chamadas GET."""

    def __init__(self, base_url: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "pytest-integracao-municipios/1.0",
            }
        )

    def get(self, path: str, params: dict[str, Any] | None = None) -> ApiResult:
        url = f"{self.base_url}/{path.lstrip('/')}"
        started_at = perf_counter()
        response = self.session.get(url, params=params, timeout=self.timeout)
        elapsed_seconds = perf_counter() - started_at
        return ApiResult(response=response, elapsed_seconds=elapsed_seconds)

