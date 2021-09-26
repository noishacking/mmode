import subprocess

class LanguagePL:

    def interface_program(self, start):
        if start == 1:
            subprocess.run("clear")
            print("\nifconfig zainstalowano pomyślnie [+] \n")
        if start == 2:
            subprocess.run("clear")
            print("ifconfig [-]")
            print("\nInstalacja pakietu net-tools!\n")
        if start == 3:
            subprocess.run("clear")
            print("\n\nNiestety nie można zainstalować pakietu net-tools.\n\n")

    def ch_mode(self, number, interface="wlan0", r_address = 0):
        if number == 1:
            print("Nie ma takiego intefejsu sieciowego")
        if number == 2:
            print(f"[+] Wyłącznie interfejsu sieciowego {interface}")
        if number == 3:
            print(f"[+] Zmiana adresu Mac interfejsu bezprzewodowego {interface} na {r_address}")
        if number == 4:
            print(f"[+] Zmiana modu interfejsu {interface} na monitor")
        if number == 5:
            print(f"[+] Wyłączenie ruchu sieciowego")
        if number == 6:
            print(f"[+] Włączenie interfejsu bezprzewodowego {interface}")
