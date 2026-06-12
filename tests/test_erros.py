import pytest


@pytest.mark.errors
def test_ibge_codigo_municipio_inexistente_nao_quebra_contrato(ibge_client):
    resultado = ibge_client.buscar_municipio_por_codigo(9999999)

    assert resultado.status_code in (200, 400, 404)
    if resultado.status_code == 200:
        assert resultado.json() == []


@pytest.mark.errors
def test_brasilapi_endpoint_municipios_com_uf_invalida_retorna_json(brasilapi_client):
    resultado = brasilapi_client.listar_municipios_por_uf("XX")

    assert resultado.status_code in (400, 404)
    assert resultado.response.headers["content-type"].lower().startswith("application/json")
