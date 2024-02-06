import subprocess


def compress_file_with_password(source, destination, password):
    command = f'"C:\\Program Files\\WinRAR\\WinRAR.exe" a  -r -afzip -p{password} {destination} .' # note -r note .
    subprocess.run(command, shell=True,cwd=source,check=True)


compress_file_with_password("D:\\mysecret", "C:\\Users\\liang\\secret.rar", 'mima')
# compress_file_with_password("D:\\File\\mysecretspace\\testliang", "C:\\Users\\liang\\secret.rar", 'mima')



def extract_file_with_password(archive, destination, password):
    command = f'"C:\\Program Files\\WinRAR\\WinRAR.exe" x {archive} -p{password} -o+ -y {destination}'
    subprocess.run(command, shell=True, check=True)

# extract_file_with_password(r"C:\\Users\\liang\\secret.rar", r'D:\\Web',"mima")


