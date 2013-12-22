from distutils.core import setup
import py2exe
import sys

sys.argv.append("py2exe")

py2exe_options = {
    "includes" : ["sip"],
    "dll_excludes" : ["MSVCP90.dll"],
    "compressed" : 1,
    "optimize" : 2,
    "ascii" : 0,
}
setup(
    name = 'CTMB Config Manager',
    version = "1.0",
    windows = [
        {
            "script": "main.py",
            "icon_resources": [(1, "images/logo.ico")],
            "dest_base": "configmanager",
        }
    ],
    zipfile = None,
    data_files = [
        ("images", ["images/logo.png"]),
        ("langs", ["langs/qt_zh_CN.qm", "langs/zh_CN.qm"])
    ],
    options = {"py2exe" : py2exe_options}
)