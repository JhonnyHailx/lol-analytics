import os

analysis_dir = "src/analysis"
py_files = [
    f for f in os.listdir(analysis_dir)
    if f.endswith('.py')
    and f not in ('run_all_examples.py', 'debug_scripts_runner.py')
]

print("Executando todos scripts da pasta 'analysis'...\n")
for py_file in py_files:
    script_path = os.path.join(analysis_dir, py_file)
    print(f"--- Rodando {py_file} ---")
    os.system(f"python {script_path}")

print("\nTodos os scripts executados. Os arquivos .csv foram gerados em 'data/reports/'.")
