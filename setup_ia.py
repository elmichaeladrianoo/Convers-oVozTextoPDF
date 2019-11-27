import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win64":
    base = "Win64GUI"

executables = [
        Executable("PrBR-Audio.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "IntelApp",
    version = "1.0",
    description = "Projeto Inteligencia Artificial",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
