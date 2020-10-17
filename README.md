# Flipkart Review API

Python based web scraper using scrapy to scrape Flipkart "Product" or "All Reviews" pages and returns all the reviews on the page, and the associated meta data about the product and the reviewer.

It can be used as a command line tool just like any scrapy project or used as a RESTful API.


### Table of Contents
___

- [Flipkart Review API](#flipkart-review-api)
    - [Table of Contents](#table-of-contents)
    - [Installation Instructions](#installation-instructions)
    - [Usage as a command line review scraper](#usage-as-a-command-line-review-scraper)
    - [Usage as an API](#usage-as-an-api)
      - [Example Response:](#example-response)
    - [Full API Implementation](#full-api-implementation)



### Installation Instructions
_____

> git clone https://github.com/kushal-goenka/flipkart-review-api.git
> 
> cd flipkart-review-api/
> 
> pip3 install -r requirements.txt



### Usage as a command line review scraper
___


> scrapy crawl review -o [FileName] -a page=[PageNumber] -a url=[FlipkartURL]

The above command takes 3 arguments:

1. The name of the json file where the data is saved, in the above case its r.json.
2. Page Number, the page number where the reviews are according to Flipkart
3. URl: This URL can be either the "All Reviews" page on Flipkart, or the original Product Page with the price information/description etc.


An example with output.json as the output filename and scraping reviews from the first review page for a specific URL would be:

> scrapy crawl review -o output.json -a page=1 -a url="https://www.flipkart.com/realme-5i-forest-green-64-gb/p/itmdac0da867a9fa?pid=MOBFNG3GNW3BU2XE&lid=LSTMOBFNG3GNW3BU2XERAL9TG&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Realme&fm=productRecommendation%2Fsimilar&iid=ceed1ea3-d651-4cd7-81fc-90c8cf2879ba.MOBFNG3GNW3BU2XE.SEARCH&ppt=browse&ppn=browse&ssid=mtqj6s4xb2sii2o01602530157645"



### Usage as an API
___

To run it on your local machine, in the root directory, run the following


> gunicorn app:app

You will see the webserver start up, to try out the API:

> http://127.0.0.1:8000/v1.0/reviews?&page={}&url={}

The Parameter is the Page Number and the URL for the Flipkart Product. Below is an example:

> http://127.0.0.1:8000/v1.0/reviews?&page=1&url=https://www.flipkart.com/realme-5i-forest-green-64-gb/p/itmdac0da867a9fa?pid=MOBFNG3GNW3BU2XE&lid=LSTMOBFNG3GNW3BU2XERAL9TG&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Realme&fm=productRecommendation%2Fsimilar&iid=ceed1ea3-d651-4cd7-81fc-90c8cf2879ba.MOBFNG3GNW3BU2XE.SEARCH&ppt=browse&ppn=browse&ssid=mtqj6s4xb2sii2o01602530157645"


#### Example Response:

```json

[
    
    {"product_price": "\u20b99999", 
    "requested_url": "URL"},
    
    {"review_title": "Product Title", 
    "avg_rating": "4.4", 
    "total_ratings": "3,64,537 Ratings &", 
    "total_reviews": "24,907 Reviews", 
    "total_pages": "Page 1 of 2,491", 
    "5": "2,50,327", 
    "4": "67,635", 
    "3": "22,835", 
    "2": "7,656", 
    "1": "16,084"},

    {"review_score": "5", 
    "review_title": "Brilliant", 
    "review_content": "The UI is super smooth and performs really well. The quad cams are amazing. 5000 mah battery is like a cherry on top. Perfect phone for its price!", 
    "reviewer_name": "Reviewer Name", 
    "reviewer_location": "Reviewer Location", 
    "reviewer_date": "Review Date", 
    "permalink": "/reviews/permalink", 
    "upvote": "6836", 
    "downvote": "1292"}

]


```

### Full API Implementation
___


The API Can be found on RapidAPI:


[RapidAPI Link](https://rapidapi.com/reviewdata-reviewdata-default/api/flipkart-reviews)


If you want to use the API, replace the http://127.0.0.1:8000 to:

> https://reviewdataapi.herokuapp.com/v1.0/reviews?&page={}&url={}
> http://reviewdata.org/


Since its hosted above, the below will also work:

> curl "http://reviewdata.org/v1.0/reviews?&page=1&url=https://www.flipkart.com/realme-5i-forest-green-64-gb/p/itmdac0da867a9fa?pid=MOBFNG3GNW3BU2XE&lid=LSTMOBFNG3GNW3BU2XERAL9TG&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Realme&fm=productRecommendation%2Fsimilar&iid=ceed1ea3-d651-4cd7-81fc-90c8cf2879ba.MOBFNG3GNW3BU2XE.SEARCH&ppt=browse&ppn=browse&ssid=mtqj6s4xb2sii2o01602530157645"

