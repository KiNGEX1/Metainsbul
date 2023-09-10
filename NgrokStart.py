import os

print("Start Ngrok.")
print("1. Start Ngrok")
print("2. Reverse Tcp")
ngrok_choice = input("Enter your choice: ").strip()

if ngrok_choice == '1':
    port = input("Enter your port: ").strip()
    os.system(f"./ngrok http {port}")
elif ngrok_choice == '2':
    port = input("Enter your port: ").strip()
    os.system(f"./ngrok tcp {port}")
else:
    print("Invalid choice. Please select 1 or 2.")
  
