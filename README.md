# User Manager Script

Detta är ett terminalbaserat Python-script för hantering av användare i ett Linux-system. Programmet erbjuder en meny där man kan skapa, ta bort och lista användare direkt via kommandoraden. 

## Funktioner

- Skapa nya användare med kommandot `useradd`
- Ta bort befintliga användare med `userdel`
- Lista alla vanliga användare (UID ≥ 1000) via `awk`
- Enkel och tydlig menystruktur i terminalen

## Krav

- Python 3
- Linux eller WSL (Windows Subsystem for Linux)
- Behörighet att köra `sudo`-kommandon

## Installation och användning

1. Klona projektet från GitHub:

```bash
git clone https://github.com/mati1123/User-manager-script.git
cd User-manager-script
python3 user_manager.py
```


=== User Manager Script ===
1. Skapa användare
2. Ta bort användare
3. Lista alla användare
4. Avsluta
