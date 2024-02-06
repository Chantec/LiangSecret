import argparse
import os
import myrar
import subprocess
from pathlib import Path
import datetime
import shutil


# lsec init name pwd
# lsec open name pwd 
# lsec close name
# lsec ls
# lsec op 

rarpath="D:\\File\\mysecretrar\\"
outpath="C:\\Users\\liang\\Desktop\\"

def init_space(name,pwd='123'):
    directory=os.path.join(outpath,name)# 

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Folder '{directory}' created successfully.")
        
        # 获取当前日期和时间
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join(directory,'time.txt'), 'w', encoding='utf-8') as file:
            file.write(formatted_time+'\n')
            file.write(pwd)

        
    else:
        print(f"NOT!!!Folder '{directory}' already exists.")
    
    myrar.compress_file_with_password(directory,rarpath+f"{name}.rar",pwd)
    shutil.rmtree(directory)


# init_space('testliang1','hello')
# init -- ok

# todo
# open
# close

# open
def open_space(name,pwd='123'):
    file_path=os.path.join(rarpath,name+".rar")
    print(file_path)
    myrar.extract_file_with_password(file_path,os.path.join(outpath,name+'\\'),pwd)#note \\

# open_space('testliang1','hello')
# open ok




# close 
def close_space(name):
    # 将name文件夹 压缩回去
    directory=os.path.join(outpath,name)
    print(directory)

    # 打开文件
    with open(os.path.join(directory,'time.txt'), 'r', encoding='utf-8') as file:
        # 使用列表推导式读取所有行
        lines = [line.strip() for line in file]
        
        # 获取第二行（注意索引从0开始）
        pwd = lines[1]

    myrar.compress_file_with_password(directory,rarpath+f"{name}.rar",pwd)
    shutil.rmtree(directory)


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

# 解析命令行参数
args = parser.parse_args()

if args.command == "init":
    print(f"Initializing Lsec instance '{args.name}' with password '{args.pwd}'.")
    init_space(args.name,args.pwd)
elif args.command == "open":
    print(f"Opening Lsec instance '{args.name}' with password '{args.pwd}'.")
    open_space(args.name,args.pwd)
elif args.command == "close":
    close_space(args.name)
    print("Closing Lsec instance.")
else:
    parser.print_help()