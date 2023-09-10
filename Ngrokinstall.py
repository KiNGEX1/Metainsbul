import os

print("What's the architecture of your device?")
print("1. Arch64")
print("2. Arch32")
print("3. Already Installed (Start)")
architecture_choice = input("Enter your choice: ").strip()

if architecture_choice == '1':
    os.system("pkg install wget -y")
    os.system("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz")
    os.system("tar -xvzf ngrok-v3-stable-linux-arm64.tgz")
    os.system("rm -rf ngrok-v3-stable-linux-arm64.tgz")
    os.system("chmod +x ngrok")
    ngrok_token = input("Enter your ngrok authentication token: ").strip()
    os.system(f"./ngrok authtoken {ngrok_token}")
    os.system("./ngrok config upgrade")
elif architecture_choice == '2':
    os.system("pkg install wget -y")
    os.system("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz")
    os.system("tar -xvzf ngrok-v3-stable-linux-386.tgz")
    os.system("rm -rf ngrok-v3-stable-linux-386.tgz")
    os.system("chmod +x ngrok")
    ngrok_token = input("Enter your ngrok authentication token: ").strip()
    os.system(f"./ngrok authtoken {ngrok_token}")
    os.system("./ngrok config upgrade")
elif architecture_choice == '3':
    os.system("python NgrokStart.py")
