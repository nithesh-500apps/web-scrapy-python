import scrapy


class TimesjobSpider(scrapy.Spider):
    name = "timesjob"
    allowed_domains = ["www.timesjobs.com"]
    start_urls = ["https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="]

    def parse(self, response):
        # print(response.text)
        job_links_data=response.xpath("//ul[@class='new-joblist']/li/header/h2/a").xpath('@href').getall()
        print(job_links_data)


        for job in job_links_data:
            yield scrapy.Request(url=job, callback=self.parse_job)
            # break

    def parse_job(self, response):
        # print(response.text)
        job_dict = {}
        title = response.xpath("//div[@class='jd-header wht-shd-bx']/h1/text()").get()
        title = response.xpath("(//ul[@class='top-jd-dtl clearfix']//li)[1]").get()
        title = response.xpath("(//ul[@class='top-jd-dtl clearfix']//li)[2]").get()
        title = response.xpath("(//ul[@class='top-jd-dtl clearfix']//li)[3]").get()
        job_dict['title'] = title.replace('"', "").strip()
        job_dict['job_url'] = response.request.url
        yield job_dict