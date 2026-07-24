import scrapy

class MetroItem(scrapy.Item):
    brand_name = scrapy.Field()
    product_name = scrapy.Field()
    description = scrapy.Field()
    regular_price = scrapy.Field()
    discounted_price = scrapy.Field()
    image_url = scrapy.Field()