import requests

def obter_dados_meteorologicos():

    # ENDEREÇO DE API METEREOLÓGICA LOCAL
    endereco = "http://127.0.0.1:8000/v1/forecast"

    # PARAMETROS DE CONSULTA
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    # RESPOSTA DA API METEREOLÓGICA LOCAL
    resposta = requests.get(

    endereco,
    params=parametros,
    timeout=15
    )

    # RESPOSTA DE ERRO CASO A API LOCAL NÃO ESTEJA FUNCIONANDO
    resposta.raise_for_status()

    # DADOS DA API LOCAL
    dados = resposta.json()

    # CONDIÇÕES METEREOLÓGICAS ATUAIS
    condicoes = dados["current"]

    temperature = condicoes["temperature_2m"]
    umidade = condicoes["relative_humidity_2m"]
    sensacao_termica = condicoes["apparent_temperature"]

    return {
        "Temperatura": temperature,
        "Umidade": umidade,
        "Sensação Térmica": sensacao_termica
    }


if __name__ == "__main__":
    dados = obter_dados_meteorologicos()


    print("=== CONDIÇÕES DO CLIMA ATUAL ===")

    print(f"Temperatura: {dados['Temperatura']}°C")
    print(f"Umidade: {dados['Umidade']}%")
    print(f"Sensação Térmica: {dados['Sensação Térmica']}°C")