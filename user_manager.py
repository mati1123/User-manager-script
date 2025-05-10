import subprocess

def skapa_anvandare():
    namn = input("Ange användarnamn: ")
    try:
        subprocess.run(["sudo", "useradd", namn])
        print(f"Användare '{namn}' skapad!")
    except Exception as e:
        print("Fel vid skapande:", e)

def ta_bort_anvandare():
    namn = input("Ange användarnamn att ta bort: ")
    try:
        subprocess.run(["sudo", "userdel", "-r", namn])
        print(f"Användare '{namn}' borttagen!")
    except Exception as e:
        print("Fel vid borttagning:", e)

def lista_anvandare():
    try:
        print("Vanliga användare:")
        subprocess.run(["awk", "-F:", "$3>=1000 {print $1}", "/etc/passwd"])
    except Exception as e:
        print("Fel vid listning:", e)



print("Välkommen till User Manager Script!")



def show_menu():
    print("=== User Manager Script ===")
    print("1. Skapa användare")
    print("2. Ta bort användare")
    print("3. Lista alla användare")
    print("4. Avsluta ")



show_menu()
val = input("Välj alternativ (1-4): ")

if val == "1":
    skapa_anvandare()
elif val == "2":
    ta_bort_anvandare()
elif val == "3":
    lista_anvandare()
elif val == "4":
    print("Avslutar...")
else:
    print("Ogiltigt val.")





