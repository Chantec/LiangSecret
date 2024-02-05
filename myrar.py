import subprocess


def compress_file_with_password(source, destination, password):
    command = f'"C:\\Program Files\\WinRAR\\WinRAR.exe" a -afzip -p{password} {destination} {source}'
    subprocess.run(command, shell=True, check=True)


# compress_file_with_password("D:\\mysecret", "C:\\Users\\liang\\secret.rar", 'mima')


def extract_file_with_password(archive, destination, password):
    command = f'"C:\\Program Files\\WinRAR\\WinRAR.exe" x {archive} -p{password} -o+ -y {destination}'
    subprocess.run(command, shell=True, check=True)

# extract_file_with_password(r"C:\\Users\\liang\\secret.rar", r'D:\\Web',"mima")


