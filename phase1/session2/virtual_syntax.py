"""
Session: One
Date: 21st April 2026 10:30am-12:30pm
focus: Setup (virtual environment, git)
Facilitator: Olatunbosun
"""

# virtual Environment
"""
python -m venv 'choice name for the venv' - If you are creating it right in the 
                                            directory where you are
python -m venv /path/path/choice-name-for-the-venv - if your are pointing it to a directory

Activation of Virtual Environment

Step 1: .venvname/Scripts/Activate.ps1 - Go through if your system permit 
        but sometime you have user policy error.
        If the code run without error skip step 2
Step 2: User Policy Error correction:
Set-ExecutionPolicy -Scope process -ExecutionPolicy Bypass

Step 3: Reinitiate step 1 again
"""
# Installing your first package
"""
verify installed packages - pip freeze
pip install panda,
pip install numpy

verify installed packages again
"""

print(help(str))
