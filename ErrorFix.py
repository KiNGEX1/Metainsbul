import os

print("Fixing Ip tracker")
os.system("apt update && apt upgrade -y")
os.system("pip install requests")
print("Fixed")
print("__________________")
print("Fixing Metaspolit")
os.system("termux-setup-storage")
os.system("pkg install ruby -y")
os.system("pkg install wget curl openssh git -y")
os.system("apt install ncurses-utils")
os.system("pkg up")
print("Fixed Metaspolit")
print("__________________")
print("Fixing Ngrok")
print("1. Arch64")
print("2. Arch32")
architecture_choice = input("Enter your choice: ").strip()

if architecture_choice == '1':
    os.system("pkg install wget -y")
  print("Ngrok Fixed")
print("Turn On your Hotspot Before using the Ngrok")
elif architecture_choice == '2':
    os.system("pkg install wget -y")
print("Ngrok Fixed")
print("Turn On your Hotspot Before using the Ngrok")
  
