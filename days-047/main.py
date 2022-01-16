import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

My_Email = "mr.iyitutuncu@gmail.com"
My_Password = os.environ.get("MY_PASSWORD")


Buy_Price = 5000
url = "https://www.amazon.com/MSI-GS76-Stealth-Gaming-Laptop/dp/B095BSDM5V"
# url = "https://www.amazon.com/ASUS-i9-10980HK-ScreenPad-Celestial-UX582LR-XS94T/dp/B08ZJQ6NDG/ref=ex_alt_wg_d"\
#       "?_encoding=UTF8&pd_rd_i=B08ZJQ6NDG&psc=1&pd_rd_w=UlLWl&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r" \
#       "=Z11XHCZVAX6ZSDM0VS5A&pd_rd_r=22856d81-25a6-406b-bc8f-32464f2b1676&pd_rd_wg=mgpvl"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="price_inside_buybox").getText()
title = soup.find(id="productTitle").getText().strip()
# print(title)
# print(price)
price_without_currency = price.split("$")[1]
# print(price_without_currency)
# print(price_without_currency.split(",")[0] + price_without_currency.split(",")[1])
price_as_float = float(price_without_currency.split(",")[0] + price_without_currency.split(",")[1])
# print(price_as_float)

if price_as_float < Buy_Price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(My_Email, My_Password)
        connection.sendmail(
            from_addr=My_Email,
            to_addrs=My_Email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
