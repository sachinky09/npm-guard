import os
import json
import re

def analyze(path):
    findings = []

    pkg = os.path.join(path, "package.json")

    if os.path.exists(pkg):
        try:
            data = json.load(open(pkg))
            scripts = data.get("scripts", {})

            if "postinstall" in scripts:
                findings.append("postinstall script detected")

            if "preinstall" in scripts:
                findings.append("preinstall script detected")
        except:
            pass

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".js"):
                full = os.path.join(root, file)

                try:
                    content = open(full, errors="ignore").read()

                    if "eval(" in content:
                        findings.append("eval usage detected")

                    if "child_process" in content:
                        findings.append("child_process usage detected")

                    if re.search(r"https?://", content):
                        findings.append("network call detected")

                    if "Buffer.from" in content:
                        findings.append("possible obfuscation detected")

                except:
                    continue

    return findings
