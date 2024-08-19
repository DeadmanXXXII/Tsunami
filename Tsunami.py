import requests
import random
import time

# Define a list of random User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]

def generate_random_url(base_url):
    # Generate a random 12-digit number
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    # Replace the last 12 characters of the base URL
    return base_url[:-12] + random_digits

def perform_requests(base_url, num_requests=100):
    for i in range(num_requests):
        random_url = generate_random_url(base_url)
        headers = {
            "User-Agent": random.choice(user_agents)
        }
        try:
            response = requests.get(random_url, headers=headers)
            print(f"Request {i+1}: {random_url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request {i+1} failed: {e}")

if __name__ == "__main__":
    base_urls = [
        "https://www.ebay.com/itm/305669110440",
        "https://www.ebay.com/itm/305669110441",
        "https://www.ebay.com/itm/305669110430"
    ]
    
    for base_url in base_urls:
        print(f"Testing with base URL: {base_url}")
        perform_requests(base_url, num_requests=1000)
        print("\n")

