rule Suspicious_JS
{
    strings:
        $a = "eval("
        $b = "child_process"
        $c = "Buffer.from"

    condition:
        any of them
}
