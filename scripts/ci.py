import subprocess

def run_ci():
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    subprocess.run(["black", "src/", "tests/"], check=True)
    subprocess.run(["pytest", "tests/"], check=True)

if __name__ == "__main__":
    run_ci()