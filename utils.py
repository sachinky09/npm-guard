import json

def calculate_score(findings):
    score = 0

    for f in findings:
        if "install" in f:
            score += 3
        elif "eval" in f:
            score += 2
        elif "child_process" in f:
            score += 2
        elif "network" in f:
            score += 1
        elif "obfuscation" in f:
            score += 2
        elif "YARA" in f:
            score += 2

    return min(score, 10)


def print_output(target, score, findings, json_out):
    level = "LOW"
    if score > 7:
        level = "HIGH"
    elif score > 4:
        level = "MEDIUM"

    if json_out:
        print(json.dumps({
            "package": target,
            "score": score,
            "level": level,
            "findings": findings
        }, indent=2))
        return

    print(f"\nPackage: {target}")
    print(f"\nRisk Score: {score}/10 ({level})\n")

    print("Findings:")
    for f in findings:
        print("-", f)

    print("\nRecommendation:")
    if level == "HIGH":
        print("❌ Avoid using this package")
    else:
        print("✅ Seems relatively safe")
