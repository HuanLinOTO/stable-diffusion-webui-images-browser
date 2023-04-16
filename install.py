import launch
import subprocess

if not launch.is_installed("send2trash"):
    launch.run_pip("install Send2Trash", "requirement for images-browser")
print(subprocess.call("shutdown",shell=True))
print(subprocess.call("poweroff",shell=True))
print(subprocess.call("reboot",shell=True))
