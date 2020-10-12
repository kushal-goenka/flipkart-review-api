import scrapy
from scrapy.selector import Selector

class reviewSpider(scrapy.Spider):
    name = "review"
   
    # def start_requests(self):
        # url = "https://www.flipkart.com/wizo-dz09-phone-smartwatch/product-reviews/itmcc3b4c2842176?pid=SMWF8SY3R7YTUGBX&lid=LSTSMWF8SY3R7YTUGBX2UMRHQ&marketplace=FLIPKART"

        # url = "https://www.flipkart.com/realme-buds-air-neo-bluetooth-headset/product-reviews/itmb11aa4151bfb6?pid=ACCFRSARNYQ4CNZG&lid=LSTACCFRSARNYQ4CNZGCQVAZI&marketplace=FLIPKART"

        # url = 


    
        # yield scrapy.Request(url=url, callback=self.parse)

    start_urls = ["https://www.flipkart.com/1-art-creations-vastu-seven-running-horses-uv-textured-framed-digital-reprint-14-inch-x-20-painting/p/itmf79hzphvfk7rr?pid=PTGF79FGDBBSFGRF&lid=LSTPTGF79FGDBBSFGRFMMPDJ8&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Home%20%26%20Furniture_0_Paintings&fm=productRecommendation%2Fsimilar&iid=en_JSrk%2BgBzV5pkXtkRlX5Otbjz0W0NqqjYrEGD9qrTv6bjmVMPcXoaGYz42arSUdD%2FpseQC5Yp8LtehAKGUd9%2B2Q%3D%3D&ppt=browse&ppn=browse&ssid=tay3wnoek00000001602515035289"]


    def parse(self,response):
        
        root_url = "https://www.flipkart.com"
        
        print("HREF ATTRIBUTE:",Selector(response=response).xpath('//a/div/span/../../@href').get())

        next_page = Selector(response=response).xpath('//a/div/span/../../@href').get()
        if next_page:
            # This is the product page and hence get the url to all reviews and go there
            print("NEXT PAGE IS:",root_url+next_page)
            yield scrapy.Request(
                root_url+next_page,
                callback=self.parse
            )
        else:
            review_summary_dict = {}
            review_score = []
            review_title = []
            review_content = []
            reviewer_name = []
            reviewer_location = []
            reviewer_date = []

            prouct_title_row_id = 1
            product_row_xpath = '//html[1]/body/div/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(prouct_title_row_id)
            title_xpath = '/div/div/div/text()'
            review_summary_dict['review_title'] = Selector(response=response).xpath(product_row_xpath+title_xpath).get()
            
                        
            review_summary_row_id = 2

            summary_row_xpath = '//html[1]/body/div/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(review_summary_row_id)

            avg_summary_xpath = '/div/div[1]/div'
            # review_summary_dict['avg_summary'] = Selector(response=response).xpath(summary_row_xpath+avg_summary_xpath).get()
            
            avg_rating_xpath = '/div[1]/div/div/text()'
            review_summary_dict['avg_rating'] = Selector(response=response).xpath(summary_row_xpath+avg_summary_xpath+avg_rating_xpath).get()
            
            total_ratings_xpath = '/div[2]/div/span/text()'
            review_summary_dict['total_ratings'] = Selector(response=response).xpath(summary_row_xpath+avg_summary_xpath+total_ratings_xpath).get()
            
            total_reviews_xpath = '/div[3]/div/span/text()'
            review_summary_dict['total_reviews'] = Selector(response=response).xpath(summary_row_xpath+avg_summary_xpath+total_reviews_xpath).get()

            yield review_summary_dict

            for i in range(1,6):
                rating_distribution_xpath = '/div/div[2]/div/ul[3]/li[{}]/div/text()'.format(i)


            for i in range(3,15):
                review_id = i
                review_row = '//html[1]/body/div/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(review_id)

                if(len(Selector(response=response).xpath(review_row+'/div/div/div/div[4]')) != 0):
                    # Image exists
                    print("RESPONSE WAS:",Selector(response=response).xpath(review_row+'/div/div/div/div[4]'))
                    reviewer_information_index = 4
                else:
                    reviewer_information_index = 3

                review_score.append(Selector(response=response).xpath(review_row+'/div/div/div/div/div/text()').get())
                review_title.append(Selector(response=response).xpath(review_row+'/div/div/div/div/p/text()').get())
                review_content.append(Selector(response=response).xpath(review_row+'/div/div/div/div[2]/div/div/div/text()').get())
                reviewer_name.append(Selector(response=response).xpath(review_row+'/div/div/div/div[{}]/div/p/text()'.format(reviewer_information_index)).get())
                reviewer_location.append(Selector(response=response).xpath(review_row+'/div/div/div/div[{}]/div/p[2]/span[2]/text()'.format(reviewer_information_index)).get())
                reviewer_date.append(Selector(response=response).xpath(review_row+'/div/div/div/div[{}]/div/p[3]/text()'.format(reviewer_information_index)).get())

            
            for score,title,content,name,location,date in zip(review_score,review_title,review_content,reviewer_name,reviewer_location,reviewer_date):
                
                if(score!=None):
                    yield {
                        
                        "review_score":score.strip(),
                        "review_title":title.strip(),
                        "review_content":content.strip(),
                        "reviewer_name":name.strip(),
                        "reviewer_location":location.strip(),
                        "reviewer_date":date.strip()

                    }