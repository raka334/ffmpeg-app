import sys
from cx_Freeze import setup, Executable

# Define the base for the executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for GUI applications

# Setup configuration
setup(
    name="MyApplication",
    version="0.1",
    description="Description of my application",
    executables=[Executable("test2.py", base=base)],
    options={
        "build_exe": {
            "include_files": [],  # Add any additional files you want to include
        },
        "bdist_msi": {
            "add_to_path": True,  # Optionally add to PATH
            "upgrade_code": "45e1542d-60c2-41ca-9835-64ba13f02af6",  # Replace with your unique GUID
        },
    },
)
