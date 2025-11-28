import subprocess
from colorama import Fore, Back, Style
import os
os.system('clear')
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
WiFis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]
for WiFi in WiFis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', WiFi, 'key=clear']).decode('cp866').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]
    try:
        print(Fore.GREEN + f'[NAME: {WiFi}], [PASS: {results[0]}]')
    except IndexError:
        print(Fore.RED + f'[NAME]: {WiFi}, [PASS: None]')
print(Fore.LIGHTGREEN_EX + f'all password geted')
