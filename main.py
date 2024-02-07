import argparse
import os
import myrar
import subprocess
from pathlib import Path
import datetime
import shutil
import yaml


# lsec init name pwd
# lsec open name pwd 
# lsec close name
# lsec ls


with open(f"D:\File\EXE\config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    rarpath=config["rarpath"]
    outpath=config["outpath"]

def init_space(name,pwd='123'):
    directory=os.path.join(outpath,name)# 

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Space {name} 创建成功")
        
        # 获取当前日期和时间
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join(directory,'time.txt'), 'w', encoding='utf-8') as file:
            file.write(formatted_time+'\n')
            file.write(pwd)
        
        myrar.compress_file_with_password(directory,rarpath+f"{name}.rar",pwd)
        shutil.rmtree(directory)
        
    else:
        print(f"NOT!!!Folder '{directory}'已经存在 创建失败")

# open
def open_space(name,pwd='123'):
    file_path=os.path.join(rarpath,name+".rar")
    myrar.extract_file_with_password(file_path,os.path.join(outpath,name+'\\'),pwd)#note \\

# close 
def close_space(name):
    # 将name文件夹 压缩回去
    directory=os.path.join(outpath,name)

    # 打开文件
    with open(os.path.join(directory,'time.txt'), 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]        
        pwd = lines[1]

    myrar.compress_file_with_password(directory,rarpath+f"{name}.rar",pwd)
    shutil.rmtree(directory)

# ls
def ls_space():

    # 获取当前目录下的所有文件


    # 遍历文件列表，输出文件名
    for file in os.listdir(rarpath):
        print(file.split('.')[0])


#init_space('testliang1','hello')
#open_space('testliang1','hello')
#close_space('testliang1')



parser = argparse.ArgumentParser(description="Lsec command-line interface")

subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

# 初始化子命令
init_parser = subparsers.add_parser("init", help="Initialize a new Lsec instance")
init_parser.add_argument("name", type=str, help="Name of the Lsec instance")
init_parser.add_argument("pwd", type=str, help="Password for the Lsec instance")

# 打开子命令
open_parser = subparsers.add_parser("open", help="Open an existing Lsec instance")
open_parser.add_argument("name", type=str, help="Name of the Lsec instance")
open_parser.add_argument("pwd", type=str, help="Password for the Lsec instance")

# 关闭子命令
close_parser = subparsers.add_parser("close", help="Close the Lsec instance")
close_parser.add_argument("name", type=str, help="Name of the Lsec instance")

# ls
init_parser = subparsers.add_parser("ls", help="List all the space")

# 解析命令行参数
args = parser.parse_args()

if args.command == "init":
    print(f"初始化Space '{args.name}' with password '{args.pwd}'.")
    init_space(args.name,args.pwd)
elif args.command == "open":
    print(f"打开Space '{args.name}' with password '{args.pwd}'.")
    open_space(args.name,args.pwd)
elif args.command == "close":
    close_space(args.name)
    print(f"关闭Space '{args.name}'")
elif args.command == 'ls':
    print(f"list:")
    ls_space()
else:
    parser.print_help()