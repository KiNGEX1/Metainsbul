import requests

def ip_locator(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print("IP Address:", data["query"])
        print("Country:", data["country"])
        print("Region:", data["regionName"])
        print("City:", data["city"])
        print("Latitude:", data["lat"])
        print("Longitude:", data["lon"])
        print("ISP:", data["isp"])
        
        # Create a Google Maps link
        google_maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
        print("Google Maps URL:", google_maps_url)
    else:
        print("Failed to locate the IP address.")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    ip_locator(ip_address)
    
