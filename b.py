import threading
import socks
import ssl
import time
import sys
target_host = "www.google.com"
target_port = 443
proxy_type_list = {
    "http": socks.HTTP,
    "socks4": socks.SOCKS4,
    "socks5": socks.SOCKS5
}
proxy_type = 'http'
pysocks_proxy_type = proxy_type_list[proxy_type]
input_file = 'proxy.txt'
output_file = 'proxy.txt'
timeout = 3
total_socks = [proxy.strip() for proxy in open(input_file)]
live_socks = []
live_socks_counter = 0
def connect_socks(socks_address):
    try:
        global live_socks_counter
        dead_socks_counter = 0
        headers = "GET / HTTP/1.3\r\nHost: " + target_host + "\r\n\r\n"
        socks_address_split = socks_address.split(":")
        socks_host = socks_address_split[0]
        socks_port = int(socks_address_split[1])
        conn= None
        try:
            socks.setdefaultproxy(pysocks_proxy_type, socks_host, socks_port)
        except:
            total_socks.remove(socks_address)
            return
        while True:
            if dead_socks_counter == 1:
                total_socks.remove(socks_address)
                break
            try:
                conn = socks.socksocket()
                conn.settimeout(timeout)
                conn.connect((target_host, target_port))
                if target_port == 443:
                    ssl_context = ssl.create_default_context()
                    conn = ssl_context.wrap_socket(conn, server_hostname=target_host)
                conn.send(headers.encode())
                conn.close()
                live_socks.append(socks_address)
                live_socks_counter += 1
                print('Total SOCKS5 working: ' + str(live_socks_counter), end='\r')
                break
            except:
                conn.close()
                dead_socks_counter += 1
    except:
        shfdsdfhsf=263462346234

thread_list = []
import time
for socks_address in total_socks:
    thread = threading.Thread(target=connect_socks, args=(socks_address, ))
    thread.start()
    thread_list.append(thread)
    sys.stdout.flush()
for thread in thread_list:
    thread.join()
    sys.stdout.flush()
print('Total SOCKS working: ' + str(live_socks_counter))
file = open(output_file, "w")
for socks_address in live_socks:
    file.write(socks_address + "\n")
file.close()
