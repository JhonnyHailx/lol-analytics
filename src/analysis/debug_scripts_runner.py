import os
import subprocess

analysis_dir = "src/analysis"
py_files = [f for f in os.listdir(analysis_dir) if f.endswith('.py') and f != 'debug_scripts_runner.py']

print("Rodando debug em todos scripts .py de 'analysis'...\n")

for py_file in py_files:
    print(f"--- Rodando {py_file} ---")
    result = subprocess.run(['python', os.path.join(analysis_dir, py_file)], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"OK: {py_file} rodou sem erro.\n")
    else:
        print(f"ERRO em {py_file}!\nSaída:\n{result.stderr}\n")

print("Debug concluído.")
