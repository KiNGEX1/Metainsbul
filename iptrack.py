import requests

def ip_locator(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print("██╗██████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗")
        print("██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
        print("██║██████╔╝  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░")
        print("██║██╔═══╝░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░")
        print("██║██║░░░░░  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗")
        print("╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
        print("\n[Location Information]\n")
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ZIP Code: {data['zip']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"ISP: {data['isp']}\n")
        
        # Create a Google Maps link
        google_maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
        print(f"[Google Maps URL]\n{google_maps_url}")
    else:
        print("Failed to locate the IP address.")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    ip_locator(ip_address)
   
