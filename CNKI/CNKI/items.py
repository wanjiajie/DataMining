import scrapy


class CnkiItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    abstract = scrapy.Field()
