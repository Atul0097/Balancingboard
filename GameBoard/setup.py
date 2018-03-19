import cx_Freeze

executables = [cx_Freeze.Executable("pygameVideo15.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Asteroid.png"],
                            "include_files":["background.png"],
                            "include_files":["explosion.png"],
                            "include_files":["laser.png"],
                            "include_files":["ship.png"]
                           }},
    executables = executables

    )