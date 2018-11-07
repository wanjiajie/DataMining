from scrapy.exceptions import DropItem


class CnkiPipeline(object):
    filter_str = "/Article/"

    def process_item(self, item, spider):
        if self.filter_str in item['href']:
            print(item['title'], item['href'])
            with open('./tmp.csv', 'a') as f:
                f.write(item['title']+','+item['href']+'\n')
            return item
        else:
            raise DropItem("this's not a normal paper")
