apt update && apt upgrade -y

pkg install python -y

pip install requests

cd Metainsbul

mv msh /data/data/com.termux/files/home

chmod +x /data/data/com.termux/files/home/msh

unzip msh.zip

rm -rf msh.zip

chmod +x msh

cd /data/data/com.termux/files/home

cd $HOME

cd

mv Metainsbul /data/data/com.termux

echo "Type ./msh to start"
