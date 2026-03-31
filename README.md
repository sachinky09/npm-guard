# 🛡️ npm-guard

A lightweight CLI tool for detecting suspicious npm packages using static analysis and YARA rules.

---

## 🚀 Features

- Scan npm packages or local projects
- Detect:
  - postinstall / preinstall scripts
  - eval() usage
  - child_process usage
  - network calls
  - obfuscation patterns
- YARA-based detection
- Simple risk scoring
- Clean CLI output

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd npm-guard

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Usage

```bash
npm-guard scan <package-name>
npm-guard scan ./your-project
```

Example:

```bash
npm-guard scan express
```

---

## 📊 Output Example

```
Package: express

Risk Score: 2 / 10 (LOW)

Findings:
- network call detected

Recommendation:
✅ Seems relatively safe
```

---

## 🧠 How It Works

1. Fetch npm package (if needed)
2. Extract contents
3. Run static analysis
4. Run YARA rules
5. Generate risk score

---

## ⚠️ Limitations

- Static analysis only
- May produce false positives

---

## 💡 One-line Pitch

A Kali-style CLI tool to detect malicious npm dependencies using heuristics and YARA.

---

## 📜 License

MIT
