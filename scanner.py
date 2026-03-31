from fetcher import fetch_target
from analyzer import analyze
from yara_runner import run_yara
from utils import calculate_score, print_output

def run_scan(target, json_out=False, use_yara=True):
    path = fetch_target(target)

    findings = []

    findings += analyze(path)

    if use_yara:
        findings += run_yara(path)

    findings = list(set(findings))

    score = calculate_score(findings)

    print_output(target, score, findings, json_out)
