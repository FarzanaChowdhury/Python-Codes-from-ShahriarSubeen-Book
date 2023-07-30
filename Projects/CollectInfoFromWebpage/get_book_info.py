# To test if our regex works

import re

st = """
<div class="book-list-wrapper "> 
<a href="/book/224822/python-diye-programming-shekha-4th-part" 
title="পাইথন দিয়ে প্রোগ্রামিং শেখা - ৪র্থ খণ্ড তামিম শাহরিয়ার সুবিন" 
onclick="gtag('event','product_view_details');
ga('send', 'event', 'Product', 'Click', 'Product-View_details_button-Click');"
 target="_blank"> <div class="book-img"> 
 <img src="https://ds.rokomari.store/rokomari110/ProductNew20190903/130X186/Python_Diye_Programming_Shekha_4th_Part-Tamim_Shahriar_Subeen-b1b52-224822.jpg" alt="Python Diye Programming Shekha - 4th Part image"> 
 <div class="cart-btn-area"> 
 <button class="btn cart-btn js--add-to-cart" product-id="224822" 
 onclick="ecomEventEmit('add_to_cart', 'RokProduct', '224822', '2725', '301');
 ga('send', 'event', 'ProductList', 'Click', 'ProductList-Click_on_ProductList_AddToCart_Button-Click');"> 
 Add to Cart </button> </div> </div> <div class="book-text-area"> <h4 class="book-title">পাইথন দিয়ে প্রোগ্রামিং শেখা - ৪র্থ খণ্ড</h4> <p class="book-author">তামিম শাহরিয়ার সুবিন</p> <div class="rating-section text-center"> <i class="ion-ios-star"></i> <i class="ion-ios-star"></i> <i class="ion-ios-star"></i> <i class="ion-ios-star"></i> <i class="ion-ios-star-half"></i> <span class="text-secondary">(23)</span> </div> <p class="book-status text-capitalize">Product in stock</p> <p class="book-price"> <strike class="original-price pl-2">TK. 350</strike> TK. 301 </p> </div> </a> <div class="home-details-btn-wrapper"> <a class="btn home-details-btn btn-block" href="/book/224822/python-diye-programming-shekha-4th-part" onclick="gtag('event','product_view_details');ga('send', 'event', 'Product', 'Click', 'Product-View_details_button-Click');"> View Details </a> </div> </div>
"""

# book_info = r'<div class="book-list-wrapper ">\s*<a href="(.*?)"\s*title="(.*?)"[^>]*>'
# image = r'<div class="book-img">\s*<img src="(.*?)"\s*alt'

book_info = r'<div class="book-list-wrapper ">\s*<a href="(.*?)"\s*title="(.*?)"[^>]*>.*?<div class="book-img">\s*<img src="(.*?)"\s*alt'

result = re.findall(book_info,st, re.DOTALL)

if result:

    print(result)
else:
    print("No match")


# # Find all matches in the string
# book_matches = re.findall(book_info, st, re.DOTALL)

# # Check if any matches were found
# if book_matches:
#     # Extract book_link, title, and image from the first match
#     book_link, title = book_matches[0]

# image_matches = re.findall(image,st)
# if image_matches:
#     image_link=image_matches
#     # Print the extracted information
#     print("book_link =", book_link)
#     print("title =", title)
#     print("image =", image_link)
# else:
#     print("No matches found in the given string.")