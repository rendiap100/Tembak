To modify the script specifically for purchasing the **Combo Sakti Special** package on Telkomsel, you'll need to adapt the API calls accordingly. Here’s how you can proceed:

1. **Identify the API Endpoint**: Find the API endpoint for purchasing the **Combo Sakti Special** package. This might require reverse engineering the Telkomsel app or web service, as the exact API URLs may not be publicly available.

2. **Modify the Payload**: Ensure that the payload sent to the API matches the requirements for purchasing the Combo Sakti Special package. The payload may need to include package IDs, plan options, or user-specific identifiers.

3. **Adjust the Headers**: The headers should match what Telkomsel's API expects, including any necessary authorization tokens or user-agent strings.

Assuming you have access to the correct API endpoints and know the parameters required for Combo Sakti Special, here is a simplified version of how you might adapt the script:

### Example Script for Purchasing Combo Sakti Special:

```python
import requests
import json
import time
from colorama import Fore, Style

# Class text color
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'

# Fungsi untuk mendapatkan kode OTP Telkomsel
def get_otp_telkomsel(nomor):
    url = "https://api.telkomsel.com/otp/request"  # Replace with actual Telkomsel OTP URL

    payload = {
        "msisdn": f"{nomor}"
    }
    
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.GREEN + f"[+] {response.status_code} Kode OTP Berhasil dikirim"  + Style.RESET_ALL)
        return response.json(), response.status_code
    else:
        return response.json(), response.status_code

# Fungsi login/untuk autentikasi kode OTP Telkomsel
def auth_otp_telkomsel(kode_auth, kode_otp):
    url = "https://api.telkomsel.com/otp/auth"  # Replace with actual Telkomsel OTP authentication URL

    payload = {
        "authId": kode_auth,
        "otp": kode_otp
    }

    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0'
    }
    
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.YELLOW + f"[\] Sedang Autentikasi OTP ..."  + Style.RESET_ALL)
        return response.json(), response.status_code
    else:
        return response.json(), response.status_code

# Fungsi untuk membeli paket Combo Sakti Special Telkomsel
def buy_combo_sakti_telkomsel(token):
    url = "https://api.telkomsel.com/package/combo-sakti-special"  # Replace with actual Combo Sakti Special API URL

    payload = {
        "tokenId": f"{token}",
        "packageId": "12345"  # Replace with actual Combo Sakti Special package ID
    }

    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.GREEN + f"[+] {response.status_code} Pembelian Combo Sakti Special Berhasil"  + Style.RESET_ALL)
        return response.json(), response.status_code
    elif response.status_code == 400:
        print(Fore.RED + "[!] Saldo/pulsa tidak cukup!"  + Style.RESET_ALL)
    else:
        print(Fore.RED + f"[!] {response.status_code} Error"  + Style.RESET_ALL)
        return response.json(), response.status_code

def main():
    print("     ┎ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴  ╴ ╴ ╴ ╴ ╴ ╴
