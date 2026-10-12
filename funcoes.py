import logging
from datetime import datetime
import json
import csv
from config import *

date_hour = datetime.now().strftime("%Y%m%d_%H%M%S")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(root_path / "logs" / f"{date_hour} Teste Técnico.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def log(log_text, level=logging.INFO):
    logging.log(level, log_text)

def read_json(json_path):
    data = ""
    try:
        with open(json_path, 'r', encoding='utf-8') as arquivo:
            data = json.load(arquivo)
        log("Aquivo "+str(json_path)+" lido com sucesso.",logging.INFO)
        log("Total de registros lidos: "+str(len(data)))
        return data

    except Exception as e:
        log("Falha ao ler arquivo Json. "+str(e),logging.ERROR)
        raise

def filter_data(registros):
    #status igual a APROVADO;
    #CPF não nulo e não vazio.
    validated_records = []
    try:
        for reg in registros:
            if reg["status"] == "APROVADO":
                if reg["cpf"].replace(" ","") != "" and reg.get("cpf") is not None and reg["id"] != "" and reg["nome"] != "":
                    validated_records.append(reg)
                else:
                    log("O Registro "+str(reg) +" apresenta inconsistência nos dados. ",logging.WARNING)
            else:
                log("O Registro "+str(reg)+" apresenta status diferente de Aprovado. ",logging.WARNING)
        log("Registros filtrados e tratados com sucesso.",logging.INFO)
        return validated_records
    except Exception as e:
        log("Erro ao tratar registros. "+str(e),logging.ERROR)
        raise

def data_to_csv(data):
    try:
        nome_arquivo = "aprovados.csv"
        
        # Definir os nomes das colunas (chaves)
        colunas = ["id", "nome", "cpf"]

        with open(out_csv, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas,delimiter=',',extrasaction='ignore')

            escritor.writeheader()
            escritor.writerows(data)


        log("Arquivo CSV salvo com sucesso. ",logging.INFO)
        log("Total de registros exportados: "+str(len(data)))
    except Exception as e:
        log("Falha ao gravar arquivo CSV. "+str(e),logging.ERROR)
        raise
