import argparse
import sys
import os

# Adiciona o diretório atual ao sys.path para garantir que as importações funcionem
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(
        description="MIMO-Flow: Framework de Orquestração de Agentes com Long-Chain Reasoning"
    )
    parser.add_argument("task", type=str, help="Descrição da tarefa para o sistema processar")
    
    args = parser.parse_args()
    
    orchestrator = Orchestrator()
    orchestrator.run_flow(args.task)

if __name__ == "__main__":
    main()
