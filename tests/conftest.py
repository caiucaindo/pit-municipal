import pytest

from api.brasilapi_client import BrasilApiClient
from api.ibge_client import IbgeClient
from api.settings import MAX_RESPONSE_TIME_SECONDS


@pytest.fixture(scope="session")
def ibge_client():
    return IbgeClient()


@pytest.fixture(scope="session")
def brasilapi_client():
    return BrasilApiClient()


@pytest.fixture(scope="session")
def max_response_time():
    return MAX_RESPONSE_TIME_SECONDS


@pytest.fixture(scope="session")
def municipios_referencia():
    return [
        {"uf": "SP", "nome": "S\u00e3o Paulo", "codigo_ibge": 3550308},
        {"uf": "RJ", "nome": "Rio de Janeiro", "codigo_ibge": 3304557},
        {"uf": "MG", "nome": "Belo Horizonte", "codigo_ibge": 3106200},
    ]

