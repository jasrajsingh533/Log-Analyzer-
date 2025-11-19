# Log-Analyzer-
import re
ip=r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
time=r"\b\d{2}:\d{2}:\d{2}\b"

print("Paste your logs below. Once you are done please press Enter twice.")

log=""
while True:
    line = input()
    if line == "":
        break
    log += line + "\n"

ips=re.findall(ip,log)
times=re.findall(time,log)

print("\n       Log Analyzer      ")
print("IPs Found:",ips)
print("Times Found:",times)
