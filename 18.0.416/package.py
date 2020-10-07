
name = "houdini"

version = "18.0.416"
 
description = "SideFX Houdini"

_data = {
    # Allzpark
    "label": "Houdini",
    "icon": "{root}/resources/icon.svg"
}

requires = [
    "!PySide2",
]

tools = [
    "houdinifx",
]


private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root}"


def commands():
    env = globals()["env"]
    system = globals()["system"]

    env.HOUDINI_VERSION = str(env.REZ_HOUDINI_VERSION)

    if system.platform == "windows":
        env.HOUDINI_LOCATION = "C:/Program Files/Side Effects Software/"\
                               "Houdini {env.HOUDINI_VERSION}"

        env.HOUDINI_SCRIPT_PATH.append("{env.HOUDINI_LOCATION}/houdini/scripts")
        env.HOUDINI_OTLSCAN_PATH.append("@/otls")
        env.HOUDINI_MENU_PATH.append("@/")

    elif system.platform == "linux":
        pass

    elif system.platform == "osx":
        pass

    env.PATH.append("{env.HOUDINI_LOCATION}/bin")
    env.PDG_USE_PDGNET = "1"

    # Disable local .env file
    env.HOUDINI_NO_ENV_FILE = "1"
