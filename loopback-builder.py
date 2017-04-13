
import jsonrpclib
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

ztp = CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_STATE)
ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)

if ztp == 'true':
    user = CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_USERNAME)
    passwd = CVPGlobalVariables.getValue(GlobalVariableNames.ZTP_PASSWORD)
else:
    user = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_USERNAME)
    passwd = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_PASSWORD)


def get_hostname():
    url = "https://%s:%s@%s/command-api" % (user, passwd, ip)
    ss = jsonrpclib.Server(url)
    show_hostname = ss.runCmds(1, ["enable", {"cmd": "show hostname"}])[1]
    hostname = show_hostname['hostname']
    return hostname


def create_routes(hostname):
    number = hostname[-1:]
    if hostname.startswith("leaf"):
        switch_type = "10"
    elif hostname.startswith("spine"):
        switch_type = "20"
    for x in range(100, 200):
        print "int lo%d" % (x)
        print "ip add 10." + switch_type + "." + number + ".%d/32" % (x)


def main():
    hostname = get_hostname()
    create_routes(hostname)


if __name__ == "__main__":
    main()
