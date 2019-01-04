# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class learnning(scrapy.Spider):
    name = "englishLearning"
    allowed_domains = ["bbs.otianya"]
    # http://bbs.otianya.cn/post-english-175299-1.shtml
    urlPrev = "http://bbs.otianya.cn/post-english-175299-"
    start_urls = [
    ]
    for item in range(1,32):
        start_urls.append(urlPrev+str(item)+".shtml")
    print("url = "+str(start_urls))
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename,"a") as f:
            for item in response.xpath('//div[@class="bbs-content"]/text()').extract():
                # f.write(bytes(item, encoding = "utf8"))
                f.write(item)