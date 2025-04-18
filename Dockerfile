# Użyj oficjalnego obrazu Pythona jako bazy
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj wszystkie pliki z projektu do katalogu w kontenerze
COPY . .

# Zainstaluj potrzebne biblioteki
RUN pip install flask

# Udostępnij port
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]
