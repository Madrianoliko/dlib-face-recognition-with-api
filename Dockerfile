# Użyj obrazu buildpack-deps jako bazowego obrazu
FROM buildpack-deps

# Aktualizuj i instaluj pakiety
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu /app w kontenerze
COPY requirements.txt .

# Stwórz i aktywuj środowisko wirtualne
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Zainstaluj zależności aplikacji
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt
RUN /venv/bin/pip install opencv-python-headless

# Skopiuj zawartość aktualnego katalogu do katalogu /app w kontenerze
COPY . .

# Uruchom aplikację
CMD ["/venv/bin/python", "main.py"]
