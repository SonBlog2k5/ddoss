import sys
import requests

def check_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    ip_address = data["ip"]
    host_name = data.get("hostname", "N/A")
    isp = data["org"]
    country = data["country"]
    region = data["region"]
    city = data["city"]

    print(f"\n\x1b[38;5;226mIP address: \x1b[38;5;255m{ip_address}")
    print(f"\x1b[38;5;226mHost name: \x1b[38;5;255m{host_name}")
    print(f"\x1b[38;5;226mISP: \x1b[38;5;255m{isp}")
    print(f"\x1b[38;5;226mCountry: \x1b[38;5;255m{country}")
    print(f"\x1b[38;5;226mRegion: \x1b[38;5;255m{region}")
    print(f"\x1b[38;5;226mCity: \x1b[38;5;255m{city}\n")

if __name__ == "__main__":
    ip = sys.argv[1]
    check_ip_info(ip)