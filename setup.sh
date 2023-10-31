apt update && apt upgrade -y

pkg install python -y

pip install requests

cd Metainsbul

mv MetaSh /data/data/com.termux/files/home

chmod +x /data/data/com.termux/files/home/MetaSh

python Meta.py
