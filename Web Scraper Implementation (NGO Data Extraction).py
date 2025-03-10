#I. Web Scraper Implementation

#Target Analysis & Ethical Compliance

#Target: https://ngodarpan.gov.in (sample implementation)

#Check robots.txt: https://ngodarpan.gov.in/robots.txt

# 5-second delay between requests

#Implement rotating user agents

# Install required libraries
!pip install requests beautifulsoup4 pandas openpyxl
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_ngo_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    ngo_list = []
    
    # Example selector - adjust based on target website structure
    for ngo in soup.select('.ngo-listing-item'):
        try:
            data = {
                'Name': ngo.select_one('.title').text.strip(),
                'Address': ngo.select_one('.address').text.strip(),
                'Services': ', '.join([s.text.strip() for s in ngo.select('.services li')]),
                'Contact Person': ngo.select_one('.contact-person').text.strip(),
                'Phone': ngo.select_one('.phone').text.strip()
            }
            ngo_list.append(data)
        except AttributeError as e:
            print(f"Error parsing entry: {e}")
    
    return ngo_list

def main():
    base_url = "https://ngodarpan.gov.in"
    all_data = []
    
    for page in range(1, 10):  # Adjust page range as needed
        url = f"{base_url}/index.php/home/sectorwise_ngo_new/{page}"
        print(f"Scraping page {page}")
        all_data.extend(scrape_ngo_data(url))
        time.sleep(2)  # Respectful delay
        
    # Export to Excel
    df = pd.DataFrame(all_data)
    df.to_excel("ngo_data.xlsx", index=False)
    print("Data exported to ngo_data.xlsx")

if __name__ == "__main__":
    main()


   # def test_scraper():
    #test_url = "https://ngodarpan.gov.in/sample-page"
   # result = scrape_page(test_url)
   # assert 'Name' in result, "Missing Name field"
   # assert len(result['Phone']) == 10, "Invalid phone format"
   # assert isinstance(result['Services'], list), "Services should be list"


#Key features:
#•	Respectful scraping with delays and headers
#•	Error handling for missing elements
#•	Structured data export to Excel
#•	CSS selector-based parsing

#. Ethical Considerations
#1.	Check robots.txt before scraping
#2.	Only scrape public data
#3.	Add proxy rotation if needed
#4.	Limit request rate

#.	Advanced Features
#1.	Proxy rotation middleware
#2.	CAPTCHA solving integration
#3.	Headless browser fallback (using Selenium)
#4.	Data validation pipeline
#5.	Automatic website structure detection

#------------------------------implementation---------------------------
 Implementation Roadmap
#1.	Web Scraper Development
#•	Phase 1: Base Scraper (2 days)
#•	Phase 2: Distributed Scraping (1 day)
#•	Phase 3: Data Validation Pipeline (1 day)


