import subprocess
def RunMain(command):
    # subprocess.run(command,shell=True)
    res = subprocess.getoutput(command)
    return res


wifis_info = RunMain("netsh wlan show profiles").split(sep="\n")
wifi_list = [wifi.split(":")[1].strip() for wifi in wifis_info if "All User Profile" in wifi]
wi_fi = []
for x in wifi_list:
    keys = RunMain(f'netsh wlan show profiles name="{x}" key=clear').split(sep="\n")
    key = [key.split(sep=":")[1].strip() for key in keys if "Key Content" in key]
    # line > just for remove the bracket list in my case
    password = ', '.join(map(str, key))
    wi_fi.append({x : password})
wi_fi