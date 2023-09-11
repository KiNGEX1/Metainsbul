import os

os.system("clear")
print("Start Ngrok.")
print("1. Ngrok http")
print("2. Ngrok tcp")
ngrok_choice = input("Enter your choice: ").strip()


ngrok_path = "/data/data/com.termux/files/home/ngrok"

if ngrok_choice == '1':
    port = input("Enter your port: ").strip()
    os.system(f"{ngrok_path} http {port}")
elif ngrok_choice == '2':
    port = input("Enter your port: ").strip()
    os.system(f"{ngrok_path} tcp {port}")
else:
    print("Invalid choice. Please select 1 or 2.")
    
