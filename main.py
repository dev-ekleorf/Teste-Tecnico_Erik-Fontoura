from funcoes import *
from config import *

def main():
    state = "INIT"

    while state != "END":

        if state == "INIT":
            try:
              logging.info("Inicializando automação")
              state = "PROCESS"
            except Exception as e:
               log("Erro durante Inicialização. "+str(e))
               state = "END"

        elif state == "PROCESS":
          try:
            log("Inicializando Processamento. ",logging.INFO)
            data = read_json(in_json_path)
            data = filter_data(data)
            data_to_csv(data)

            state = "END_PROCESS"
          except Exception as e:
             log("Erro durante processamento. "+str(e))
             state = "END"

        elif state == "END_PROCESS":
          log("Automação finalizada",logging.INFO)
          state = "END"

main()