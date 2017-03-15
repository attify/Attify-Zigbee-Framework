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

printf "\n\n${GREEN}[*] Installing dependencies ${NORMAL}\n\n"
sudo apt-get install python-gtk2 python-cairo python-usb python-crypto python-serial python-dev libgcrypt-dev

printf "\n\n${GREEN}[*] Getting PyQt ${NORMAL} \n\n "
sudo apt-get install python-qt4

printf "\n\n${GREEN}[*] Installing Killerbee ${NORMAL}\n\n"
cd killerbee
sudo python setup.py install

printf "\n\n${GREEN}[*] All done! ${NORMAL} \n\n"


printf "${GREEN}"
printf " _______________              \n"
printf "( Happy hacking )   	      \n"
printf " ---------------    	      \n"
printf "        o   ^__^     	      \n"
printf "         o  (oo)\______       \n"
printf "            (__)\       )\/\  \n"
printf "                ||----w |     \n"
printf "                ||     ||     \n"
printf "${NORMAL}\n"
