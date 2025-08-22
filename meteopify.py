import requests
import sys
# LANGUAGE ITALIAN ONLY FOR NOW
print("Inserisci la tua API-KEY di OpenWeatherMap (non verrà salvata)")
API_KEY = input("> ").strip()

if not API_KEY:
    print("Manca la chiave API. Uscita in corso...")
    sys.exit(1)

API_BASE = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_UNITS = "metric"
DEFAULT_LANG = "it"

while True:
    city = input("Inserisci la città: ").strip()
    if not city:
        print("Nessuna città inserita.")
        continue

    city = city.replace(", ", ",")
    if "," not in city:
        city = f"{city},IT"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": DEFAULT_UNITS,
        "lang": DEFAULT_LANG
    }

    response = requests.get(API_BASE, params=params, timeout=10)
    if response.status_code == 200:
        payload = response.json()
        # stampa minima (adatta se vuoi)
        name    = payload.get("name", "")
        country = (payload.get("sys") or {}).get("country", "")
        temp    = (payload.get("main") or {}).get("temp", 0.0)
        hum     = (payload.get("main") or {}).get("humidity", 0)
        desc    = (payload.get("weather") or [{}])[0].get("description", "").capitalize()

        print(f"\nMeteo per {name} ({country})")
        print(f"  Temperatura: {temp}°C")
        print(f"  Umidità:     {hum}%")
        print(f"  Condizioni:  {desc}\n")
    else:
        print(f"Errore: {response.status_code} - {response.text[:200]}")

    again = input("Vuoi il meteo per un'altra località? [s/N]: ").strip().lower()
    if again not in ("s", "si", "y", "yes"):
        break
