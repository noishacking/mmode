import subprocess

class LanguageEN:

    def interface_program(self, start):
        if start == 1:
            subprocess.run("clear")
            print("\nifconfig installed successfully [+] \n")
        if start == 2:
            subprocess.run("clear")
            print("ifconfig [-]")
            print("\nInstalling the net-tools!\n")
        if start == 3:
            subprocess.run("clear")
            print("\n\nUnfortunately, the net-tools package cannot be installed.\n\n")

    def ch_mode(self, number, interface="wlan0", r_address = 0):
        if number == 1:
            print("There is no such network interface")
        if number == 2:
            print(f"[+] Disabling the network interface {interface}")
        if number == 3:
            print(f"[+] Changing the Mac address of the wireless interface  {interface} for {r_address}")
        if number == 4:
            print(f"[+] Changing the interface module {interface} for monitor")
        if number == 5:
            print(f"[+] Network traffic off")
        if number == 6:
            print(f"[+] Enabling the wireless interface {interface}")