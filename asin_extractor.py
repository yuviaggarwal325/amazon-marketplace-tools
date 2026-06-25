import re

url = "https://www.amazon.in/dp/B0ABC12345"

match = re.search(r"/dp/([A-Z0-9]{10})", url)

if match:
    print("ASIN:", match.group(1))
