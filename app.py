import logging
import time

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def hello():
    logging.info("Função hello() chamada")
    return "Hello, World!"

def slow_function():
    logging.info("Função slow_function() chamada")
    time.sleep(2)
    return "Processamento concluído"

if __name__ == "__main__":
    print(hello())
    print(slow_function())
