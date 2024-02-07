import subprocess
import yaml

with open(f"D:\File\EXE\config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    winrar=config['WinRARpath']

def compress_file_with_password(source, destination, password):
    command = f'"{winrar}" a  -r -afzip -p{password} {destination} .' # note -r note .
    subprocess.run(command, shell=True,cwd=source,check=True)

def extract_file_with_password(archive, destination, password):
    command = f'"{winrar}" x {archive} -p{password} -o+ -y {destination}'
    subprocess.run(command, shell=True, check=True)