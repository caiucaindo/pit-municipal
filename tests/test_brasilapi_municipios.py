import pytest


@pytest.mark.integration
@pytest.mark.performance
def test_brasilapi_lista_ufs_com_status_200_e_tempo_adequado(
    brasilapi_client, max_response_time
):
    resultado = brasilapi_client.listar_ufs()
    ufs = resultado.json()

    assert resultado.status_code == 200
    assert resultado.elapsed_seconds < max_response_time
    assert isinstance(ufs, list)
    assert any(uf["sigla"] == "SP" for uf in ufs)


@pytest.mark.contract
def test_brasilapi_contrato_json_de_uf(brasilapi_client):
    resultado = brasilapi_client.listar_ufs()
    uf = resultado.json()[0]

    assert resultado.status_code == 200
    assert set(["id", "sigla", "nome", "regiao"]).issubset(uf)
    assert isinstance(uf["id"], int)
    assert isinstance(uf["sigla"], str)
    assert isinstance(uf["nome"], str)
    assert isinstance(uf["regiao"], dict)


@pytest.mark.integration
@pytest.mark.parametrize("municipio", [
    {"uf": "SP", "nome": "S\u00e3o Paulo", "codigo_ibge": 3550308},
    {"uf": "RJ", "nome": "Rio de Janeiro", "codigo_ibge": 3304557},
])
def test_brasilapi_lista_municipios_por_uf(brasilapi_client, municipio):
    resultado = brasilapi_client.listar_municipios_por_uf(municipio["uf"])
    municipios = resultado.json()

    assert resultado.status_code == 200
    assert isinstance(municipios, list)
    assert any(
        int(item["codigo_ibge"]) == municipio["codigo_ibge"]
        and item["nome"].casefold() == municipio["nome"].casefold()
        for item in municipios
    )


@pytest.mark.contract
def test_brasilapi_contrato_json_de_municipio(brasilapi_client):
    resultado = brasilapi_client.listar_municipios_por_uf("SP")
    municipio = resultado.json()[0]

    assert resultado.status_code == 200
    assert set(["nome", "codigo_ibge"]).issubset(municipio)
    assert isinstance(municipio["nome"], str)
    assert isinstance(municipio["codigo_ibge"], str)
    assert municipio["codigo_ibge"].isdigit()


@pytest.mark.errors
def test_brasilapi_estado_invalido_retorna_erro_controlado(brasilapi_client):
    resultado = brasilapi_client.listar_municipios_por_uf("XX")

    assert resultado.status_code in (400, 404)
    assert resultado.response.headers["content-type"].lower().startswith("application/json")
