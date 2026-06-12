import pytest


@pytest.mark.integration
@pytest.mark.performance
@pytest.mark.parametrize("uf", ["SP", "RJ", "MG"])
def test_ibge_consulta_municipios_por_uf_retorna_200_e_responde_rapido(
    ibge_client, max_response_time, uf
):
    resultado = ibge_client.listar_municipios_por_uf(uf)

    assert resultado.status_code == 200
    assert resultado.elapsed_seconds < max_response_time
    assert isinstance(resultado.json(), list)
    assert len(resultado.json()) > 0


@pytest.mark.integration
@pytest.mark.parametrize("municipio", [
    {"uf": "SP", "nome": "S\u00e3o Paulo", "codigo_ibge": 3550308},
    {"uf": "RJ", "nome": "Rio de Janeiro", "codigo_ibge": 3304557},
    {"uf": "MG", "nome": "Belo Horizonte", "codigo_ibge": 3106200},
])
def test_ibge_lista_municipios_especificos_por_uf(ibge_client, municipio):
    resultado = ibge_client.listar_municipios_por_uf(municipio["uf"])
    municipios = resultado.json()

    assert resultado.status_code == 200
    assert any(
        item["id"] == municipio["codigo_ibge"] and item["nome"] == municipio["nome"]
        for item in municipios
    )


@pytest.mark.contract
def test_ibge_contrato_json_de_municipio(ibge_client):
    resultado = ibge_client.listar_municipios_por_uf("SP")
    municipio = resultado.json()[0]

    assert resultado.status_code == 200
    assert set(["id", "nome", "microrregiao", "regiao-imediata"]).issubset(municipio)
    assert isinstance(municipio["id"], int)
    assert isinstance(municipio["nome"], str)
    assert isinstance(municipio["microrregiao"], dict)
    assert isinstance(municipio["regiao-imediata"], dict)


@pytest.mark.integration
def test_ibge_valida_codigo_ibge_de_municipio(ibge_client):
    resultado = ibge_client.buscar_municipio_por_codigo(3550308)
    municipio = resultado.json()

    assert resultado.status_code == 200
    assert municipio["id"] == 3550308
    assert municipio["nome"] == "S\u00e3o Paulo"


@pytest.mark.errors
def test_ibge_estado_invalido_retorna_lista_vazia_ou_erro_controlado(ibge_client):
    resultado = ibge_client.listar_municipios_por_uf("XX")

    assert resultado.status_code in (200, 400, 404)
    if resultado.status_code == 200:
        assert resultado.json() == []

