import subprocess

def run_yara(path):
    findings = []

    try:
        result = subprocess.check_output(
            f"yara -r rules/suspicious.yar {path}",
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode()

        if result.strip():
            findings.append("YARA rule matched")

    except:
        pass

    return findings
