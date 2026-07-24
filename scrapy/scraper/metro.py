import csv
import os
import requests


class MetroScraper:

  def __init__(self, filename="metro_products.csv"):
    self.filename = filename
    self.headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    self.fieldnames = [
        "brand_name",
        "product_name",
        "description",
        "regular_price",
        "discounted_price",
        "image_url",
    ]
    self.base_url = (
              "https://admin.metro-online.pk/api/read/Products?&type=Products_nd_associated_Brands&order=product_scoring__DESC&filter=||tier1Id&filterValue=||8659&filter=||tier2Id&filterValue=||8659&filter=||tier3Id&filterValue=||8659&filter=||tier4Id&filterValue=||8659&&offset=0&limit=100&filter=active&filterValue=true&filter=storeId&filterValue=10&filter=!url&filterValue=!null&filter=Op.available_stock&filterValue=Op.gt__0&")

  def fetch_all_products(self):
   
    response = requests.get(self.base_url, headers=self.headers)

    if response.status_code != 200:
      print(f"Failed to fetch data")
      return []

    data = response.json()
    return data if isinstance(data, list) else data.get("data", [])

  def run(self):
    
    file_exists = os.path.exists(self.filename) and os.path.getsize(self.filename) > 0

    with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.DictWriter(file, fieldnames=self.fieldnames)

      if not file_exists:
        writer.writeheader()

      print("Fetching all products from Metro API...")
      products = self.fetch_all_products()

      if not products:
        print("No products found.")
        return

      total_saved = 0
      for product in products:
        writer.writerow({
            "brand_name": product.get("brand_name"),
            "product_name": product.get("product_name"),
            "description": product.get("description"),
            "regular_price": product.get("price"),
            "discounted_price": product.get("sale_price"),
            "image_url": product.get("url") or product.get("url_r2"),
        })
        total_saved += 1

    print(f"Successfully saved {total_saved} products to {self.filename}")



scraper = MetroScraper()
scraper.run()

