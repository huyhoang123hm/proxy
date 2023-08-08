package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
	"sync"
)

func readCookieFile(filePath string) ([]string, error) {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(string(data), "\n")
	return lines, nil
}

func haha(proxyInfo, cookieValue string, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i < 100; i++ {
		proxyHostPort := strings.Split(proxyInfo, ":")
		if len(proxyHostPort) != 2 {
			fmt.Println("Invalid proxy format:", proxyInfo)
			continue
		}
		targetURL := "https://hitsagainstaraid.click"

		// Create a new HTTP client with a custom Transport that uses the proxy
		proxyURL := fmt.Sprintf("http://%s:%s", proxyHostPort[0], proxyHostPort[1])
		proxy, err := url.Parse(proxyURL)
		if err != nil {
			fmt.Println("Invalid proxy URL:", err)
			continue
		}
		client := &http.Client{
			Transport: &http.Transport{
				Proxy: http.ProxyURL(proxy),
			},
		}

		// Prepare the request with headers
		req, err := http.NewRequest("GET", targetURL, nil)
		if err != nil {
			fmt.Println("Request error:", err)
			continue
		}
		req.Header.Set("Cookie", cookieValue)
		req.Header.Set("Authority", "hitsagainstaraid.click")
		req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
		req.Header.Set("Accept-Language", "en-US,en;q=0.9")
		req.Header.Set("Cache-Control", "max-age=0")
		req.Header.Set("If-Modified-Since", "Sun, 03 Apr 2022 10:07:45 GMT")
		req.Header.Set("Sec-Ch-Ua", "")
		req.Header.Set("Sec-Ch-Ua-Mobile", "?0")
		req.Header.Set("Sec-Ch-Ua-Platform", `""`)
		req.Header.Set("Sec-Fetch-Dest", "document")
		req.Header.Set("Sec-Fetch-Mode", "navigate")
		req.Header.Set("Sec-Fetch-Site", "none")
		req.Header.Set("Sec-Fetch-User", "?1")
		req.Header.Set("Upgrade-Insecure-Requests", "1")
		req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

		// Perform the request and read the response
		resp, err := client.Do(req)
		if err != nil {
			fmt.Println("Request error:", err)
			continue
		}
		resp.Body.Close()
	}
}

func main() {
	cookieFilePath := "cookie.txt" // Replace with the actual path to your cookie.txt file
	lines, err := readCookieFile(cookieFilePath)
	if err != nil {
		fmt.Println("Error reading cookie file:", err)
		return
	}

	var wg sync.WaitGroup
	for i := 0; i < 4; i++ {
		for _, line := range lines {
			line = strings.TrimSpace(line)
			if line == "" {
				continue
			}
			proxyInfoCookieValue := strings.Split(line, "|")
			proxyInfo := proxyInfoCookieValue[0]
			if len(proxyInfoCookieValue) < 2 {
				fmt.Println("Invalid line format:", line)
				continue
			}
			cookieValue := proxyInfoCookieValue[1]
			wg.Add(1)
			go haha(proxyInfo, cookieValue, &wg)
		}
	}
	wg.Wait()
}
