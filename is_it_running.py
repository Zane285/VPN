from logging import exception
import psutil, tqdm, os
from time import sleep
while True:
    if "openvpn.exe" in (p.name() for p in psutil.process_iter()):
        if "FortniteClient-Win64-Shipping.exe" in (p.name() for p in psutil.process_iter()):
            print(f"Detected Fortnite and OpenVPN\nKilling OpenVPN")
            try:
                os.system("taskkill.exe /F /IM openvpn.exe")
            except Exception as e:
                print(e)

    elif "FortniteClient-Win64-Shipping.exe" not in (p.name() for p in psutil.process_iter()):
        if "openvpn.exe" not in (p.name() for p in psutil.process_iter()):
            try:
                print("initializing vpn")
                cmd = 'start /b cmd /c "C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --connect cVPN-us-newyork01-tcp443.ovpn'
                os.system(cmd)
            except Exception as e:
                print(e)
