import requests


result = requests.get("https://catfact.ninja/fact")

koci_fakt = result.json()

print("Random cat fact:", koci_fakt['fact'])
