#### run_doctests.py
# Script para executar todos os doctests dos módulos do projeto

import sys
import os

# Adiciona a raiz do projeto ao sys.path para permitir importação dos módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import doctest

def run_all_doctests():
    """
    ### Executa os doctests de todos os módulos
    # Para cada módulo, importa e executa os testes via doctest.testmod.
    # Exibe um resumo com o total de testes executados e falhas encontradas.
    # Encerra o script com código de erro caso existam falhas (útil para integração contínua).
    """
    modules = [
        'src.data.csv_importador',           # Módulo de importação de CSV
        'src.analysis.monetizacao',          # Módulo de análise de monetização
        'src.analysis.ano_lancamento',       # Módulo de análise de lançamento por ano
        'src.analysis.plataforma_os'         # Módulo de análise de plataforma de SO
    ]
    total_failures = 0
    total_tests = 0
    for mod_name in modules:
        # Importa dinamicamente cada módulo
        mod = __import__(mod_name, fromlist=[''])
        print(f"\nRodando doctest em: {mod_name}")
        # Executa os doctests do módulo
        result = doctest.testmod(mod, verbose=True)
        total_failures += result.failed
        total_tests += result.attempted
    # Exibe um resumo final dos resultados
    print(f"\nResumo dos doctests: {total_tests} testes, {total_failures} falhas.")
    # Encerra com erro caso haja alguma falha
    if total_failures > 0:
        sys.exit(1)

# Executa o runner se for chamado diretamente como script
if __name__ == "__main__":
    run_all_doctests()
