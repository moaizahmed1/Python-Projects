import json
import scrapy
from metro_scraper.items import MetroItem

class MetroSpiderSpider(scrapy.Spider):
    name = "metro_spider"
    allowed_domains = ["metro-online.pk"]
    start_urls =[
            "https://admin.metro-online.pk/api/read/Products?"
            "type=Products_nd_associated_Brands&order=product_scoring__DESC&"
            "filter=||tier1Id&filterValue=||8659&filter=||tier2Id&filterValue=||8659&"
            "filter=||tier3Id&filterValue=||8659&filter=||tier4Id&filterValue=||8659&&"
            "offset=0&limit=100&filter=active&filterValue=true&"
            "filter=storeId&filterValue=10&filter=!url&filterValue=!null&"
            "filter=Op.available_stock&filterValue=Op.gt__0&"
        ]
    

    def parse(self, response):
        if response.status != 200:
            self.logger.error("Failed to fetch data from API")
            return

        # Scrapy automatically parses JSON responses
        data = response.json()
        products = data if isinstance(data, list) else data.get("data", [])

        if not products:
            self.logger.warning("No products found.")
            return
        
        total_saved = 0

        for product in products:
            item = MetroItem()
            item["brand_name"] = product.get("brand_name")
            item["product_name"] = product.get("product_name")
            item["description"] = product.get("description")
            item["regular_price"] = product.get("price")
            item["discounted_price"] = product.get("sale_price")
            item["image_url"] = product.get("url") or product.get("url_r2")
            total_saved += 1
            yield item