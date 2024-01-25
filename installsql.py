import os

os.system("figlet SQLMAP")
print("INSTALLING")

os.system("pkg install git -y")
os.system("apt update")
os.system("apt upgrade -y)
print("")
print("INSTALLING SQLMAP")
os.system("git clone https://github.com/sqlmapproject/sqlmap")
os.system("cd sqlmap")
os.system("python sqlmap.py -hh")
