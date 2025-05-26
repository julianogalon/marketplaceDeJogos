import sys
import os

# Adiciona a raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import doctest

def run_all_doctests():
    modules = [
        'src.data.csv_importador',
        'src.analysis.monetizacao',
        'src.analysis.ano_lancamento',
        'src.analysis.plataforma_os',
        'src.analysis.estatistica_linhas'
    ]
    total_failures = 0
    total_tests = 0
    for mod_name in modules:
        mod = __import__(mod_name, fromlist=[''])
        print(f"\nRodando doctest em: {mod_name}")
        result = doctest.testmod(mod, verbose=True)
        total_failures += result.failed
        total_tests += result.attempted
    print(f"\nResumo dos doctests: {total_tests} testes, {total_failures} falhas.")
    if total_failures > 0:
        sys.exit(1)

if __name__ == "__main__":
    run_all_doctests()
