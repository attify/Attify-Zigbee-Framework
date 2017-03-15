!/bin/bash

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
NORMAL=$(tput sgr0)

printf "${RED}"
echo
echo "      ___  _   _   _  __            "
echo "     / _ \| | | | (_)/ _|           "
echo "    / /_\ \ |_| |_ _| |_ _   _      "
echo "    |  _  | __| __| |  _| | | |     "
echo "    | | | | |_| |_| | | | |_| |     "
echo "    \_| |_/\__|\__|_|_|  \__, |     "
echo "                          __/ |     "
echo "                         |___/      "
echo
echo "[*] Attify Zigbee Framework v1.0 Installer"
printf "${NORMAL}"

sleep 1

printf "${GREEN}[*] Installing dependencies ${NORMAL}\n\n"
sudo apt-get install python-gtk2 python-cairo python-usb python-crypto python-serial python-dev libgcrypt-dev

printf "${GREEN}[*] Installing Killerbee ${NORMAL}\n\n"
cd killerbee
sudo python setup.py install

printf "${GREEN}[*] All done! ${NORMAL} "

echo "[*] Bye now!"

printf "${RED}"
echo " _______________"
echo "( Happy hacking )"
echo " ---------------"
echo "        o   ^__^"
echo "         o  (oo)\_______"
echo "            (__)\       )\/\"
echo "                ||----w |"
echo "                ||     ||"
printf "${NORMAL}\n"
