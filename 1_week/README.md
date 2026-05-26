## Day 1 - Bad Day
**0/3 Nothing**
- Reading:
    1. I try to read it, but I can't understand when I currenty in the class.
    2. I read but I don't absorve any concept.
- Code:
    1. Start the script, but I need admin acess on the collage PC.
- Wireshark:
    1. I also need to have admin permissions to install it.
 
## Day 2 - Arch Linux install
1. Verify network
    ```bash
    ping google.com
    ````
2. Verify updates
    ```bash
    pacman -Syy
    pacman-key --init
    pacman-key --populate archlinux
    pacman -Sy archlinux-keyring
    ````
3. Install configs
    ```bash
    archinstall --skip-ntp --skip-wkd
    ````