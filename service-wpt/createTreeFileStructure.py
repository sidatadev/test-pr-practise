import os

def create_directory_structure():
    # Base directories and files
    base_dirs_files = [
        "requirements",
        "src",
        "test_suite",
        ".bandit",
        ".coveragerc",
        ".flake8",
        ".gitignore",
        ".pre-commit-config.yaml",
        ".pylintrc",
        "Dockerfile",
        "gunicorn_config.py",
        "Makefile",
        "manifest.yml",
        "pip.conf",
        "pyproject.toml",
        "README.md",
        "requirements.txt",
        "run.py",
        "tasks.py",
        "version.txt",
        "wsgi.py"
    ]
    
    # Create base directories and files
    for item in base_dirs_files:
        if '.' in item:  # Check if it's a file (by checking presence of an extension)
            with open(item, 'w') as f:
                pass
        else:
            os.makedirs(item, exist_ok=True)
    
    # Additional directories and files inside `test_suite`
    test_suite_dirs_files = [
        "end-to-end",
        "endpoint",
        "sample_data",
        "unit"
    ]
    
    test_suite_files = {
        "end-to-end": ["test_e2e.py"],
        "endpoint": ["testEndpoints.py"],
        "sample_data": ["sample_payloads.py"],
        "unit": ["__init__.py", "conftest.py", "test_run.py", "test_service.py"]
    }
    
    for dir_name, files in test_suite_files.items():
        for file_name in files:
            with open(os.path.join("test_suite", dir_name, file_name), 'w') as f:
                pass

if __name__ == "__main__":
    create_directory_structure()
