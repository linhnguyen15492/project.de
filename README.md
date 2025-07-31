# project notes

- create python enviroment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. From within Windows (PowerShell or Command Prompt):

   ```bash
   wsl hostname -I
   ```

2. From within WSL (Linux terminal):

   ```bash
   ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'
   ```

3. To find the Windows host IP address from within WSL:

   ```bash
   cat /etc/resolv.conf | grep nameserver | cut -d ' ' -f 2
   ```

ipconfig
Wireless LAN adapter Wi-Fi: IPv4 Address. . . . . . . . . . . : 192.168.9.71

[hướng dẫn kết nối mongodb từ wsl2](https://blog.codonomics.com/2020/08/connect-to-mongodb-on-windows-host-from.html)