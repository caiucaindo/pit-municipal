import pytest


@pytest.mark.contract
@pytest.mark.integration
def test_ibge_e_brasilapi_concordam_sobre_municipios_referencia(
    ibge_client, brasilapi_client, municipios_referencia
):
    for referencia in municipios_referencia:
        resposta_ibge = ibge_client.listar_municipios_por_uf(referencia["uf"])
        resposta_brasilapi = brasilapi_client.listar_municipios_por_uf(referencia["uf"])

        assert resposta_ibge.status_code == 200
        assert resposta_brasilapi.status_code == 200

        codigos_ibge = {item["id"] for item in resposta_ibge.json()}
        codigos_brasilapi = {
            int(item["codigo_ibge"]) for item in resposta_brasilapi.json()
        }

        assert referencia["codigo_ibge"] in codigos_ibge
        assert referencia["codigo_ibge"] in codigos_brasilapi


@pytest.mark.contract
def test_ibge_lista_estados_possui_contrato_basico(ibge_client):
    resultado = ibge_client.listar_estados()
    estados = resultado.json()

    assert resultado.status_code == 200
    assert len(estados) >= 27
    assert all({"id", "sigla", "nome", "regiao"}.issubset(estado) for estado in estados)


@pytest.mark.contract
def test_ibge_regiao_sem_municipios_retorna_lista_vazia(ibge_client):
    resultado = ibge_client.listar_municipios_por_regiao(0)

    assert resultado.status_code == 200
    assert resultado.json() == []
