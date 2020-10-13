# review-api
Review API for E-commerce Websites

Starting with Flipkart.

## How to start the webScraper functionality?

pip3 install scrapy
cd to root directory of the project/git repo
run a scrapy command like the following:

> scrapy crawl review -o r.json -a page=1 -a url="https://www.flipkart.com/wagwan-letter-s-alphabet-best-gift-boy-friend-special-birthday-girlfriend619-ceramic-coffee-mug/p/itm6e2472e7dd97e?pid=MUGFNYP8VHAJXE6F&lid=LSTMUGFNYP8VHAJXE6FQU1Q8H&marketplace=FLIPKART&spotlightTagId=BestsellerId_upp%2Fi7t%2Fmsi&srno=b_1_3&otracker=nmenu_sub_Home%20%26%20Furniture_0_Coffee%20Mugs&fm=organic&iid=de07e23f-7433-427e-b32f-d3c1b8dcd05c.MUGFNYP8VHAJXE6F.SEARCH&ppt=browse&ppn=browse&ssid=0jro2c445s0000001602533269501"

The above command takes 3 arguments:

1. The name of the json file where the data is saved, in the above case its r.json.
2. Page Number, the page number where the reviews are according to Flipkart
3. URl: This URL can be either the "All Reviews" page on Flipkart, or the original Product Page with the price information/description etc.


## Example Response:

'''javascript

{
    "product_price":"\u20b9178"
},
{
    "review_title":"Wagwan Letter S Alphabet Best Gift for Boy Friend Special Birthday Gift For Girlfriend619 Ceramic Coffee Mug Reviews",
    "avg_rating":"4.3",
    "total_ratings":"460 Ratings &",
    "total_reviews":"46 Reviews",
    "total_pages":"Page 1 of 5",
    "5":"305",
    "4":"78",
    "3":"35",
    "2":"16",
    "1":"26"
},
{
    "review_score":"5",
    "review_title":"Perfect product!",
    "review_content":"nice design and this is for my love Jannat...I am given her.",
    "reviewer_name":"Arshad  Amin",
    "reviewer_location":", Darbhanga District",
    "reviewer_date":"7 months ago",
    "permalink":"/reviews/396199ea-4f02-43d7-a164-8f0859d7028c",
    "upvote":"1",
    "downvote":"0"
}

'''

# Other Examples:

scrapy crawl review -o r.json -a page=3 -a url="https://www.flipkart.com/1-art-creations-vastu-seven-running-horses-uv-textured-framed-digital-reprint-14-inch-x-20-painting/p/itmf79hzphvfk7rr?pid=PTGF79FGDBBSFGRF&lid=LSTPTGF79FGDBBSFGRFMMPDJ8&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Home%20%26%20Furniture_0_Paintings&fm=productRecommendation%2Fsimilar&iid=en_JSrk%2BgBzV5pkXtkRlX5Otbjz0W0NqqjYrEGD9qrTv6bjmVMPcXoaGYz42arSUdD%2FpseQC5Yp8LtehAKGUd9%2B2Q%3D%3D&ppt=browse&ppn=browse&ssid=tay3wnoek00000001602515035289"


scrapy crawl review -o r.json -a page=3 -a url="https://www.flipkart.com/milton-thermosteel-duo-dlx-1000-ml-bottle/product-reviews/itmd5866a8a44f9a?pid=BOTFDBRKNU29RAZJ&lid=LSTBOTFDBRKNU29RAZJ5CTH7D&marketplace=FLIPKART"

scrapy crawl review -o r.json -a page=1 -a url="https://www.flipkart.com/wagwan-letter-s-alphabet-best-gift-boy-friend-special-birthday-girlfriend619-ceramic-coffee-mug/p/itm6e2472e7dd97e?pid=MUGFNYP8VHAJXE6F&lid=LSTMUGFNYP8VHAJXE6FQU1Q8H&marketplace=FLIPKART&spotlightTagId=BestsellerId_upp%2Fi7t%2Fmsi&srno=b_1_3&otracker=nmenu_sub_Home%20%26%20Furniture_0_Coffee%20Mugs&fm=organic&iid=de07e23f-7433-427e-b32f-d3c1b8dcd05c.MUGFNYP8VHAJXE6F.SEARCH&ppt=browse&ppn=browse&ssid=0jro2c445s0000001602533269501"





run the following:

scrapy crawl review -o r.json -a page=1 -a url="https://www.flipkart.com/realme-5i-forest-green-64-gb/p/itmdac0da867a9fa?pid=MOBFNG3GNW3BU2XE&lid=LSTMOBFNG3GNW3BU2XERAL9TG&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Realme&fm=productRecommendation%2Fsimilar&iid=ceed1ea3-d651-4cd7-81fc-90c8cf2879ba.MOBFNG3GNW3BU2XE.SEARCH&ppt=browse&ppn=browse&ssid=mtqj6s4xb2sii2o01602530157645"