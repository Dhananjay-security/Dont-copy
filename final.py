import scrapy
import json
import csv

class AdidasSpider(scrapy.Spider):
    name = "Adidas"

    def start_requests(self):
        url = 'https://www.adidas.co.in/storefront/IN478187-delhi-shop-101-nelson-mandela-marg-dlf-emporio-mall-vasant-kuni-adidas-originals-store-delhi-dlf-promenade'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        script_data = response.xpath("//script[@type='application/ld+json']/text()")
        if script_data:
            json_data = json.loads(script_data.get())
            store_name = json_data['name']
            street_address = json_data['address']['streetAddress']
            city = json_data['address']['addressLocality']
            state = json_data['address']['addressRegion']
            postal_code = json_data['address']['postalCode']
            country = json_data['address']['addressCountry']
            phone_number = json_data['telephone']
            latitude = json_data['geo']['latitude']
            longitude = json_data['geo']['longitude']
            opening_hours = json_data['openingHoursSpecification'][0]['opens'] + " - " + json_data['openingHoursSpecification'][0]['closes']

            #It will create the file in the same directory or you can put the path of your own file for the same
            with open('adidas.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Store Name', 'Street Address', 'City', 'State', 'Postal Code', 'Country', 'Phone Number', 'Latitude', 'Longitude', 'Opening Hours'])
                writer.writerow([store_name, street_address, city, state, postal_code, country, phone_number, latitude, longitude, opening_hours])
