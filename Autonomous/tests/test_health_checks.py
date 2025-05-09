import subprocess
import os

MODULES = [
    "discovery",
    "self_evolution",
    "scaling",
    "monitoring",
    "automation",
    "integration"
]

def test_health_checks():
    for module in MODULES:
        script = os.path.join(module, "health_check.py")
        result = subprocess.run(["python3", script], capture_output=True, text=True)
        assert result.returncode == 0, f"{module} health check failed: {result.stderr}"
        assert "OK" in result.stdout, f"{module} health check output unexpected: {result.stdout}"
