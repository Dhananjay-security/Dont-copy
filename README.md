## Approach:

    Identify the website structure and understand the data to be scraped
    Inspect the website and find out the tags and attributes containing the required data
    Use Scrapy, a web crawling framework in Python to scrape the data from the website
    Parse the HTML content using XPath selectors and extract the required data
    Store the data in a CSV file using the CSV writer module in Python

## Challenges:

    Dynamic content: One of the main challenges in web scraping is to handle dynamic content. In some websites, the data is 
    loaded dynamically, which means the content of the website changes after the page has been loaded. This makes it difficult
    to extract the required data. However, in this case, we were able to locate the JSON data in a script tag and extract it 
    using Scrapy.

    Website restrictions: Some websites may have restrictions on web scraping. They may block IP addresses or use CAPTCHAs to 
    prevent automated scraping. In this case, we did not face any such restrictions.

    Incorrect data extraction: Another challenge is to correctly extract the required data from the HTML content. Sometimes, 
    the data may be nested inside multiple tags or may be present in different locations on the webpage. This can make it 
    difficult to locate and extract the data accurately. However, we were able to locate the required data using XPath selectors 
    in this case.

## How we overcame them:

    Dynamic content: I used Scrapy, a web crawling framework that can handle dynamic content by simulating user interactions 
    and waiting for the content to load before extracting the data.

    Website restrictions: In this case, I did not face any restrictions, so I did not have to overcome this challenge.

    Incorrect data extraction: I carefully inspected the HTML content and used XPath selectors to accurately locate and extract
    the required data. I also tested our code on multiple pages to ensure that it was extracting the data correctly.
