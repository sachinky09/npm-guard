import os
import subprocess
import tempfile

def fetch_target(target):
    if os.path.exists(target):
        return target

    print("[+] Fetching package...")

    temp = tempfile.mkdtemp()

    subprocess.run(
        f"npm pack {target}",
        shell=True,
        cwd=temp,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    for f in os.listdir(temp):
        if f.endswith(".tgz"):
            subprocess.run(f"tar -xzf {f}", shell=True, cwd=temp)
            return os.path.join(temp, "package")

    raise Exception("Failed to fetch package")
