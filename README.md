# PIT Municipal

## Plataforma de Inteligencia Territorial Municipal

Projeto voltado a disciplica de Testes de Software, integrado com APIs publicas usando Pytest.
A proposta é validar integracões com serviços publicos que fornecem dados de municipios brasileiros, UFs e códigos IBGE.

## APIs utilizadas

- IBGE Localidades: `https://servicodados.ibge.gov.br/api/v1/localidades`
- BrasilAPI: `https://brasilapi.com.br/api`

## Tecnologias

- Python
- Pytest
- Requests
- pytest-html

## Estrutura do projeto

```text
projeto/
|-- api/
|   |-- http_client.py
|   |-- ibge_client.py
|   |-- brasilapi_client.py
|   `-- settings.py
|-- tests/
|   |-- conftest.py
|   |-- test_ibge_municipios.py
|   |-- test_brasilapi_municipios.py
|   |-- test_contratos_e_consistencia.py
|   `-- test_erros.py
|-- reports/
|-- requirements.txt
|-- pytest.ini
|-- README.md
```

## Como executar

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

Execute os testes:

```powershell
python -m pytest
```

Gere o relatorio HTML:

```powershell
python -m pytest --html=reports/relatorio.html --self-contained-html
```

Exemplo de chamada isolada no terminal:

```powershell
python -c "from api.ibge_client import IbgeClient; r = IbgeClient().buscar_municipio_por_codigo(3550308); print(r.status_code); print(r.json())"
```

## Exemplos de testes implementados

- Status code das APIs IBGE e BrasilAPI.
- Tempo de resposta minimo esperado.
- Existencia de municipios especificos por UF.
- Validacao de codigo IBGE.
- Validacao de estrutura JSON.
- Tratamento de UF invalida.
- Lista vazia para consulta sem resultado.
- Consistencia entre dados do IBGE e da BrasilAPI.

## Resultados

O relatorio HTML gerado em `reports/relatorio.html` contem:

- total de testes executados;
- testes aprovados;
- eventuais falhas;
- tempo total de execução;
- detalhes por caso de teste.
