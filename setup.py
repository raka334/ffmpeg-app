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
    executables=[Executable("test2.py", base=base)]
)
