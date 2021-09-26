import subprocess
import scapy.all as scapy
from random import randint
import argparse
import time
import re
import os

import language_pl
import language_en


class ChangingMode:

    def __init__(self):
        self.interfaces = []
        self.wlan_interface = None
        self.random_address = self.random_mac_address()
        self.language = self.default_language()

    def default_language(self):
        """Gets the system language and sets it. Functions especially needed when running a program with options."""
        if re.findall("pl_PL", os.getenv('LANG')):
            return language_pl.LanguagePL()
        else:
            return language_en.LanguageEN()

    def interface_program(self):
        try:
            subprocess.check_output("/sbin/ifconfig")
        except FileNotFoundError:
            print("ifconfig [-]")
            self.language.interface_program(2)
            try:
                subprocess.run(["sudo", "apt-get", "install", "net-tools"])
                subprocess.run("clear")
                self.language.interface_program(1)
            except subprocess.CalledProcessError:
                subprocess.run("clear")
                self.language.interface_program(3)

    def list_of_interfaces(self):
        for interface in scapy.get_if_list():
            if interface == 'lo':
                pass
            else:
                self.interfaces.append(interface)

    def line_interface(self, interface):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest="interface", help="Wlan interface")
        options = parser.parse_args()

        if options.interface in interface:
            self.wlan_interface = options.interface
        else:
            self.wlan_interface = None

    @staticmethod
    def even_number(first_part_of_mac):
        modified_mac = int(first_part_of_mac)
        modified_mac += 1
        return str(modified_mac)

    def random_mac_address(self):
        mac = ""
        for i in range(1, 13):
            mac += str(randint(0, 9))
            if i == 2:
                if int(mac) % 2 != 0:
                    mac = self.even_number(mac)
            if i == 12:
                break
            if i % 2 == 0:
                mac += ":"
        return mac

    def changing_mode(self, interface, wlan_interface):
        if wlan_interface is None:
            self.language.ch_mode(1)
        else:
            for i in interface:
                subprocess.run(["sudo", "ifconfig", i, "down"])
                self.language.ch_mode(2, i)
                time.sleep(3)
            subprocess.call(["sudo", "ifconfig", wlan_interface, "hw", "ether", self.random_address])
            self.language.ch_mode(3, self.wlan_interface, self.random_address)
            subprocess.call(["sudo", "iwconfig", wlan_interface, "mode", "monitor"])
            self.language.ch_mode(4, self.wlan_interface)
            subprocess.call(["sudo", "airmon-ng", "check", "kill"])
            self.language.ch_mode(5)
            subprocess.call(["sudo", "ifconfig", wlan_interface, "up"])
            self.language.ch_mode(6, self.wlan_interface)

    def run(self):
        self.interface_program()
        self.list_of_interfaces()
        self.line_interface(self.interfaces)
        self.changing_mode(self.interfaces, self.wlan_interface)
