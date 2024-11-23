import subprocess

def run_coverage():
    subprocess.run(["coverage", "run", "-m", "pytest"], check=True)
    subprocess.run(["coverage", "report"], check=True)
    subprocess.run(["coverage", "xml"], check=True)

if __name__ == "__main__":
    run_coverage()
