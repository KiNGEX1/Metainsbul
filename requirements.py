import os

os.system("apt update && apt upgrade -y")
os.system("pkg install wget curl openssh git -y")
os.system("apt install ncurses-utils")
os.system("pkg install ruby -y")
os.system("cd Metainsbul")
os.system("chmod +x Metainstall.sh")
os.system("clear")
os.system("bash MetaInstall.sh")
