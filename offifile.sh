clear

pkg install curl

pkg install ruby -y

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \

chmod 755 msfinstall && \

./msfinstall

echo "Type msfconsole to start metasploit"
