import subprocess

def install_packages_from_requirements(requirements_file):
    with open(requirements_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # Install the package using conda
            subprocess.run(['conda', 'install', '-y', line], check=True)

install_packages_from_requirements('requirements.txt')

