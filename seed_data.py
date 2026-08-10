import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), 'mealbite'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mealbite.settings')
django.setup()

from delivery.models import Restaurant, Item


def seed():
    print("Clearing existing items and restaurants...")
    Item.objects.all().delete()
    Restaurant.objects.all().delete()

    print("Creating 20 restaurants with 5 items each (100 items total)...")

    # 1. Burger Lounge & Bistro
    r1 = Restaurant.objects.create(
        name="Burger Lounge & Bistro",
        picture="https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
        cuisine="Burgers • Fast Food • American",
        rating=4.8
    )
    Item.objects.create(restaurant=r1, name="Big Mac Double Cheeseburger", description="Double beef patty with melted cheddar, special house sauce, pickles & fresh lettuce.", price=249.0, vegeterian=False, picture="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r1, name="Crispy Cajun Seasoned Fries", description="Deep-fried golden potato strips tossed in fiery Cajun spice blend.", price=119.0, vegeterian=True, picture="https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r1, name="Spicy Buffalo Chicken Wings", description="10-piece crispy fried wings glazed with spicy cayenne pepper sauce & ranch.", price=229.0, vegeterian=False, picture="https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r1, name="Grilled Veggie & Avocado Burger", description="Artisanal veggie patty topped with fresh avocado slices and herb mayo.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r1, name="Creamy Vanilla Bean Milkshake", description="Thick handcrafted vanilla bean shake topped with whipped cream and cherry.", price=149.0, vegeterian=True, picture="https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=600&q=80")

    # 2. Bella Italia Trattoria
    r2 = Restaurant.objects.create(
        name="Bella Italia Trattoria",
        picture="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
        cuisine="Pizza • Italian • Pasta",
        rating=4.9
    )
    Item.objects.create(restaurant=r2, name="Margherita Neapolitan Pizza", description="Hand-tossed crust, San Marzano tomato sauce, fresh mozzarella & basil leaves.", price=349.0, vegeterian=True, picture="https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r2, name="Creamy Chicken Penne Alfredo", description="Penne pasta tossed in rich parmesan cream sauce with grilled chicken.", price=389.0, vegeterian=False, picture="https://images.unsplash.com/photo-1621996346565-e3d5d6281270?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r2, name="Garlic Butter Bruschetta", description="Toasted sourdough topped with diced vine tomatoes, garlic, extra virgin olive oil.", price=179.0, vegeterian=True, picture="https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r2, name="Classic Spaghetti Bolognese", description="Traditional Italian slow-cooked beef ragù served over al dente spaghetti.", price=419.0, vegeterian=False, picture="https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r2, name="Classic Espresso Tiramisu", description="Savoiardi ladyfingers soaked in espresso coffee layered with mascarpone cream.", price=229.0, vegeterian=True, picture="https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=600&q=80")

    # 3. Shordaab BBQ & Grill
    r3 = Restaurant.objects.create(
        name="Shordaab BBQ & Grill",
        picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        cuisine="Steak • BBQ • Ribs",
        rating=4.7
    )
    Item.objects.create(restaurant=r3, name="Smoked Ribeye Steak 300g", description="Prime cut ribeye steak smoked over hickory wood and seared with garlic herb butter.", price=699.0, vegeterian=False, picture="https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r3, name="Smoky Glazed Pork Ribs", description="Slow-cooked tender pork ribs glazed with sweet honey bourbon barbecue sauce.", price=649.0, vegeterian=False, picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r3, name="Creamy Garlic Mashed Potatoes", description="Fluffy mashed russet potatoes whipped with heavy cream, garlic, and chives.", price=159.0, vegeterian=True, picture="https://images.unsplash.com/photo-1514944298341-9880e65a852e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r3, name="Honey Glazed BBQ Drumsticks", description="Char-grilled chicken drumsticks basted in tangy barbecue honey sauce.", price=299.0, vegeterian=False, picture="https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r3, name="Char-Grilled Sweet Corn", description="Whole sweet corn cob grilled over charcoal and brushed with spiced chili butter.", price=129.0, vegeterian=True, picture="https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=600&q=80")

    # 4. Royal Spice Indian Kitchen
    r4 = Restaurant.objects.create(
        name="Royal Spice Indian Kitchen",
        picture="https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80",
        cuisine="Indian • Mughlai • Curry",
        rating=4.9
    )
    Item.objects.create(restaurant=r4, name="Classic Butter Chicken", description="Tender chicken pieces simmered in rich creamy tomato and cashew nut gravy.", price=329.0, vegeterian=False, picture="https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r4, name="Paneer Butter Masala", description="Fresh cottage cheese cubes cooked in spiced aromatic butter gravy.", price=299.0, vegeterian=True, picture="https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r4, name="Garlic Butter Naan", description="Traditional tandoor-baked flatbread brushed with garlic butter and cilantro.", price=49.0, vegeterian=True, picture="https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r4, name="Hyderabadi Dum Chicken Biryani", description="Fragrant basmati rice layered with marinated chicken, saffron & aromatic spices.", price=359.0, vegeterian=False, picture="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r4, name="Gulab Jamun with Ice Cream", description="Warm milk dumplings soaked in cardamom rose syrup served with vanilla ice cream.", price=129.0, vegeterian=True, picture="https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80")

    # 5. Sea Breeze Seafood Bistro
    r5 = Restaurant.objects.create(
        name="Sea Breeze Seafood Bistro",
        picture="https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80",
        cuisine="Sea Food • Prawns • Gourmet",
        rating=4.6
    )
    Item.objects.create(restaurant=r5, name="Garlic Butter Atlantic Lobster", description="Fresh whole lobster tail roasted with garlic herb sauce, lemon & melted butter.", price=799.0, vegeterian=False, picture="https://images.unsplash.com/photo-1559742811-822863646df8?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r5, name="Crispy Golden Calamari Rings", description="Lightly breaded squid rings fried to golden perfection with spicy aioli dip.", price=349.0, vegeterian=False, picture="https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r5, name="Pan-Seared Salmon Fillet", description="Fresh Atlantic salmon fillet pan-seared with lemon dill butter & asparagus.", price=599.0, vegeterian=False, picture="https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r5, name="New England Clam Chowder", description="Rich creamy clam chowder soup with diced potatoes, celery and fresh herbs.", price=249.0, vegeterian=False, picture="https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r5, name="Fresh Garden Caesar Salad", description="Crisp romaine lettuce, garlic croutons, shaved parmesan with Caesar dressing.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80")

    # 6. Dragon Wok Asian Kitchen
    r6 = Restaurant.objects.create(
        name="Dragon Wok Asian Kitchen",
        picture="https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=800&q=80",
        cuisine="Asian • Chinese • Dim Sum",
        rating=4.8
    )
    Item.objects.create(restaurant=r6, name="Steamed Chicken Dim Sum Basket", description="6-piece handmade steamed chicken dumplings served with chili soy dipping sauce.", price=279.0, vegeterian=False, picture="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r6, name="Veg Schezwan Hakka Noodles", description="Wok-tossed noodles with colorful crisp vegetables in spicy Schezwan sauce.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r6, name="Kung Pao Chicken", description="Stir-fried tender chicken, roasted peanuts, chili peppers and spring onions.", price=349.0, vegeterian=False, picture="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r6, name="Steamed Edamame with Sea Salt", description="Fresh young soybean pods steamed and lightly seasoned with Maldon sea salt flakes.", price=189.0, vegeterian=True, picture="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r6, name="Crispy Vegetable Spring Rolls", description="Crispy golden pastry rolls filled with shredded cabbage, carrots & glass noodles.", price=169.0, vegeterian=True, picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80")

    # 7. El Taco Mexican Cantina
    r7 = Restaurant.objects.create(
        name="El Taco Mexican Cantina",
        picture="https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80",
        cuisine="Mexican • Tacos • Burritos",
        rating=4.7
    )
    Item.objects.create(restaurant=r7, name="Loaded Beef Tacos Supreme", description="3 crispy corn tortillas filled with seasoned ground beef, cheddar, salsa & sour cream.", price=299.0, vegeterian=False, picture="https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r7, name="Cheesy Veggie Quesadilla", description="Grilled flour tortilla stuffed with melted Monterey Jack, peppers, corn & black beans.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1618040996337-56904b7850b9?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r7, name="Nachos Grande with Guacamole", description="Crispy tortilla chips smothered in warm queso cheese, jalapenos & fresh guacamole.", price=229.0, vegeterian=True, picture="https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r7, name="Grilled Chicken Burrito Bowl", description="Cilantro lime rice, grilled chicken, black beans, pico de gallo & chipotle crema.", price=329.0, vegeterian=False, picture="https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r7, name="Cinnamon Churros with Chocolate", description="Crispy fried pastry dusted with cinnamon sugar, served with warm dark chocolate dip.", price=159.0, vegeterian=True, picture="https://images.unsplash.com/photo-1624371414361-e670ef4889d6?auto=format&fit=crop&w=600&q=80")

    # 8. Sweet Treats Pastry & Cafe
    r8 = Restaurant.objects.create(
        name="Sweet Treats Pastry & Cafe",
        picture="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80",
        cuisine="Desserts • Pastries • Cakes",
        rating=4.9
    )
    Item.objects.create(restaurant=r8, name="Choco Lava Molten Cake", description="Warm gooey chocolate cake with a rich molten lava core & vanilla bean ice cream.", price=169.0, vegeterian=True, picture="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r8, name="Red Velvet Cream Cheese Cupcake", description="Moist red velvet sponge topped with silky cream cheese frosting.", price=119.0, vegeterian=True, picture="https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r8, name="Belgian Chocolate Waffle", description="Crispy golden Belgian waffle drizzled with melted dark chocolate & maple syrup.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1562376552-0d160a2f238d?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r8, name="Fresh Mixed Berry Cheesecake", description="New York style baked cheesecake topped with fresh strawberry and blueberry compote.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r8, name="Iced Caramel Macchiato", description="Rich espresso combined with milk and vanilla syrup, topped with caramel drizzle.", price=179.0, vegeterian=True, picture="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=600&q=80")

    # 9. Green Oasis Vegan Cafe
    r9 = Restaurant.objects.create(
        name="Green Oasis Vegan Cafe",
        picture="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
        cuisine="Healthy • Vegan • Organic",
        rating=4.8
    )
    Item.objects.create(restaurant=r9, name="Avocado Toast with Microgreens", description="Toasted sourdough, mashed Hass avocado, cherry tomatoes, chia seeds & lemon zest.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1588137378633-dea1336ce1e2?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r9, name="Quinoa & Roasted Veggie Buddha Bowl", description="Fluffy quinoa, roasted sweet potatoes, chickpea, kale, and tahini dressing.", price=279.0, vegeterian=True, picture="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r9, name="Plant-Based Beyond Burger", description="Juicy plant-based burger patty with vegan cheese, caramelized onion & vegan mayo.", price=329.0, vegeterian=True, picture="https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r9, name="Fresh Green Detox Smoothie", description="Blend of fresh spinach, green apple, cucumber, ginger, coconut water & mint.", price=159.0, vegeterian=True, picture="https://images.unsplash.com/photo-1610970881699-44a5587cabec?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r9, name="Crispy Falafel Wrap with Hummus", description="Warm pita wrapped around crispy chickpea falafel, tahini, cucumber & pickled radish.", price=239.0, vegeterian=True, picture="https://images.unsplash.com/photo-1561651823-34feb02250e4?auto=format&fit=crop&w=600&q=80")

    # 10. Tokyo Ramen & Sushi Bar
    r10 = Restaurant.objects.create(
        name="Tokyo Ramen & Sushi Bar",
        picture="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80",
        cuisine="Japanese • Sushi • Ramen",
        rating=4.9
    )
    Item.objects.create(restaurant=r10, name="Salmon & Tuna Sushi Platter", description="8-piece fresh nigiri and maki roll combination with pickled ginger & wasabi.", price=549.0, vegeterian=False, picture="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r10, name="Spicy Pork Tonkotsu Ramen", description="Rich pork bone broth, tender chashu pork belly, soft-boiled egg & bamboo shoots.", price=429.0, vegeterian=False, picture="https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r10, name="Crispy Vegetable Tempura Basket", description="Assorted seasonal vegetables fried in light crispy Japanese tempura batter.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1615361200141-f45040f367be?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r10, name="Chicken Teriyaki Donburi Bowl", description="Grilled chicken thigh glazed in sweet teriyaki sauce over steamed Japanese rice.", price=379.0, vegeterian=False, picture="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r10, name="Matcha Green Tea Ice Cream", description="Authentic Japanese green tea ice cream scoop garnished with sweet red bean paste.", price=149.0, vegeterian=True, picture="https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?auto=format&fit=crop&w=600&q=80")

    # 11. Saffron Grill Persian House
    r11 = Restaurant.objects.create(
        name="Saffron Grill Persian House",
        picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        cuisine="Persian • Kebabs • Middle Eastern",
        rating=4.8
    )
    Item.objects.create(restaurant=r11, name="Lamb Kofta Kebab", description="Minced lamb skewers seasoned with sumac and herbs, served with saffron rice.", price=399.0, vegeterian=False, picture="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r11, name="Saffron Chicken Chelow Kebab", description="Tender chicken breast marinated in saffron, lemon & yogurt, grilled to order.", price=429.0, vegeterian=False, picture="https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r11, name="Persian Hummus & Warm Pita", description="Creamy chickpea dip blended with tahini, olive oil, served with warm pita bread.", price=189.0, vegeterian=True, picture="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r11, name="Grilled Veggie & Paneer Skewers", description="Charcoal grilled cottage cheese, bell peppers & onions with Persian spice rub.", price=279.0, vegeterian=True, picture="https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r11, name="Persian Pistachio Baklava", description="Crispy phyllo pastry layers stuffed with crushed pistachios & honey syrup.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1519676867240-f03562e64548?auto=format&fit=crop&w=600&q=80")

    # 12. Le Petit Paris Bakery & Bistro
    r12 = Restaurant.objects.create(
        name="Le Petit Paris Bakery & Bistro",
        picture="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80",
        cuisine="French • Bakery • Bistro",
        rating=4.9
    )
    Item.objects.create(restaurant=r12, name="Butter Croissant with Berry Jam", description="Flaky French butter croissant freshly baked, served with artisanal raspberry jam.", price=129.0, vegeterian=True, picture="https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r12, name="French Onion Soup with Gruyère", description="Caramelized onion broth topped with toasted baguette slice and melted Gruyère cheese.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r12, name="Quiche Lorraine with Bacon", description="Savory custard pie filled with crispy smoked bacon, swiss cheese, and nutmeg.", price=299.0, vegeterian=False, picture="https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r12, name="Poulet au Vin (Chicken in Wine)", description="Braised chicken thighs cooked in rich Burgundy wine sauce with mushrooms.", price=459.0, vegeterian=False, picture="https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r12, name="Assorted Parisian Macarons Box", description="Box of 5 delicate French macarons (Pistachio, Raspberry, Chocolate, Vanilla, Lemon).", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1569864358642-9d1684040f43?auto=format&fit=crop&w=600&q=80")

    # 13. Bangkok Street Thai Kitchen
    r13 = Restaurant.objects.create(
        name="Bangkok Street Thai Kitchen",
        picture="https://images.unsplash.com/photo-1559314809-0d155014e29e?auto=format&fit=crop&w=800&q=80",
        cuisine="Thai • Street Food • Noodles",
        rating=4.7
    )
    Item.objects.create(restaurant=r13, name="Classic Shrimp Pad Thai", description="Stir-fried rice noodles with succulent prawns, crushed peanuts, bean sprouts & tamarind sauce.", price=349.0, vegeterian=False, picture="https://images.unsplash.com/photo-1559314809-0d155014e29e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r13, name="Thai Green Curry with Rice", description="Aromatic coconut milk green curry with bamboo shoots, Thai eggplant & basil.", price=329.0, vegeterian=True, picture="https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r13, name="Tom Yum Spicy Seafood Soup", description="Hot & sour lemongrass broth filled with prawns, squid, mushrooms & kaffir lime leaves.", price=289.0, vegeterian=False, picture="https://images.unsplash.com/photo-1548946526-f69e2424cf45?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r13, name="Crispy Money Bag Dumplings", description="Golden crispy fried pastry purses filled with minced vegetables and sweet plum sauce.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r13, name="Mango Sticky Rice Dessert", description="Sweet sticky rice drenched in warm coconut milk served with ripe sweet mango slices.", price=189.0, vegeterian=True, picture="https://images.unsplash.com/photo-1621263764928-df1444c5e859?auto=format&fit=crop&w=600&q=80")

    # 14. Bavarian Beer Garden & Grill
    r14 = Restaurant.objects.create(
        name="Bavarian Beer Garden & Grill",
        picture="https://images.unsplash.com/photo-1538580668433-88229b47e58a?auto=format&fit=crop&w=800&q=80",
        cuisine="German • Sausages • Grill",
        rating=4.6
    )
    Item.objects.create(restaurant=r14, name="Traditional Grilled Bratwurst", description="Grilled German pork sausage served with sauerkraut, sweet mustard and pretzel.", price=389.0, vegeterian=False, picture="https://images.unsplash.com/photo-1528825871115-3581a5387919?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r14, name="Soft Bavarian Pretzel with Dip", description="Freshly baked giant salted pretzel served with warm beer cheese dip.", price=159.0, vegeterian=True, picture="https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r14, name="Crispy Chicken Schnitzel", description="Pan-fried breaded chicken breast fillet served with lemon wedge & French fries.", price=399.0, vegeterian=False, picture="https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r14, name="Classic German Potato Salad", description="Warm potato salad tossed with whole grain mustard, herbs, and vinaigrette.", price=149.0, vegeterian=True, picture="https://images.unsplash.com/photo-1514944298341-9880e65a852e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r14, name="Warm Apple Strudel Dessert", description="Traditional spiced apple pastry roll dusted with powdered sugar & vanilla custard.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=600&q=80")

    # 15. Cappadocia Mediterranean Cafe
    r15 = Restaurant.objects.create(
        name="Cappadocia Mediterranean Cafe",
        picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        cuisine="Mediterranean • Mezze • Falafel",
        rating=4.8
    )
    Item.objects.create(restaurant=r15, name="Falafel & Halloumi Mezze Platter", description="Crispy chickpea falafels, grilled halloumi cheese, hummus, tzatziki & pita.", price=349.0, vegeterian=True, picture="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r15, name="Chicken Shawarma Wrap Supreme", description="Marinated chicken shawarma, garlic toum, pickles wrapped in toasted lavash bread.", price=279.0, vegeterian=False, picture="https://images.unsplash.com/photo-1561651823-34feb02250e4?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r15, name="Greek Salad with Feta & Olives", description="Cucumber, ripe tomatoes, Kalamata olives, red onions & feta cheese dressed in oregano oil.", price=229.0, vegeterian=True, picture="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r15, name="Slow-Roasted Lamb Doner", description="Spiced shaved lamb doner served with turmeric pilaf rice & garlic yogurt sauce.", price=389.0, vegeterian=False, picture="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r15, name="Kunafa with Sweet Cheese", description="Crispy shredded pastry filled with melted cheese, soaked in orange blossom syrup.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1519676867240-f03562e64548?auto=format&fit=crop&w=600&q=80")

    # 16. Havana Club Cuban Cantina
    r16 = Restaurant.objects.create(
        name="Havana Club Cuban Cantina",
        picture="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
        cuisine="Cuban • Caribbean • Sandwiches",
        rating=4.7
    )
    Item.objects.create(restaurant=r16, name="Classic Cubano Sandwich", description="Pressed Cuban bread loaded with roast pork, ham, Swiss cheese, pickles & mustard.", price=329.0, vegeterian=False, picture="https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r16, name="Arroz con Pollo (Cuban Rice)", description="Traditional Cuban savory rice cooked with tender chicken, red peppers & green peas.", price=359.0, vegeterian=False, picture="https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r16, name="Crispy Sweet Plantain Chips", description="Thinly sliced green plantains fried crisp, served with creamy mojo garlic sauce.", price=149.0, vegeterian=True, picture="https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r16, name="Cuban Black Bean & Corn Stew", description="Hearty slow-cooked black bean stew served with white rice & sweet plantains.", price=219.0, vegeterian=True, picture="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r16, name="Tropical Coconut Flan", description="Silky smooth caramel custards infused with sweet coconut cream.", price=169.0, vegeterian=True, picture="https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=600&q=80")

    # 17. Seoul House Korean BBQ
    r17 = Restaurant.objects.create(
        name="Seoul House Korean BBQ",
        picture="https://images.unsplash.com/photo-1498654896293-37aacf113fd9?auto=format&fit=crop&w=800&q=80",
        cuisine="Korean • BBQ • Fried Chicken",
        rating=4.9
    )
    Item.objects.create(restaurant=r17, name="Beef Bulgogi Rice Bowl", description="Marinated sweet soy sliced beef with sautéed onions, sesame seeds over rice.", price=419.0, vegeterian=False, picture="https://images.unsplash.com/photo-1553163147-622ab57be1c7?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r17, name="Crispy Korean Fried Chicken", description="Double-fried chicken wings tossed in spicy sweet Yangnyeom chili glaze.", price=329.0, vegeterian=False, picture="https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r17, name="Kimchi Fried Rice with Egg", description="Spicy fried rice cooked with fermented kimchi, topped with a fried sunny egg.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r17, name="Vegetable Japchae Glass Noodles", description="Sweet potato glass noodles stir-fried with sesame oil, spinach, mushrooms & carrots.", price=269.0, vegeterian=True, picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r17, name="Hotteok Sweet Cinnamon Pancake", description="Korean street pancake stuffed with melted brown sugar, cinnamon & chopped walnuts.", price=139.0, vegeterian=True, picture="https://images.unsplash.com/photo-1562376552-0d160a2f238d?auto=format&fit=crop&w=600&q=80")

    # 18. Steakhouse 101 Prime Cut
    r18 = Restaurant.objects.create(
        name="Steakhouse 101 Prime Cut",
        picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        cuisine="Steakhouse • Gourmet • Fine Dining",
        rating=4.8
    )
    Item.objects.create(restaurant=r18, name="Filet Mignon Steak 250g", description="Center-cut tenderloin steak grilled over mesquite wood served with peppercorn sauce.", price=799.0, vegeterian=False, picture="https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r18, name="Loaded Baked Potato", description="Fluffy baked Idaho potato stuffed with butter, sour cream, cheddar & crispy bacon.", price=189.0, vegeterian=False, picture="https://images.unsplash.com/photo-1514944298341-9880e65a852e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r18, name="Creamed Spinach with Parmesan", description="Fresh spinach folded into rich garlic parmesan cream sauce.", price=169.0, vegeterian=True, picture="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r18, name="Crispy Onion Rings Basket", description="Thick-cut beer battered onion rings fried crisp, served with smoky BBQ dip.", price=149.0, vegeterian=True, picture="https://images.unsplash.com/photo-1639024471283-03518883512d?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r18, name="New York Strip Steak 300g", description="USDA Prime NY strip steak seared in cast iron with rosemary and garlic.", price=749.0, vegeterian=False, picture="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80")

    # 19. La Pizzeria Woodfired Oven
    r19 = Restaurant.objects.create(
        name="La Pizzeria Woodfired Oven",
        picture="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
        cuisine="Pizza • Artisanal • Italian",
        rating=4.9
    )
    Item.objects.create(restaurant=r19, name="Four Cheese Quattro Formaggi", description="Woodfired pizza topped with mozzarella, gorgonzola, parmesan & fontina cheese.", price=399.0, vegeterian=True, picture="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r19, name="Spicy Pepperoni & Hot Honey", description="Crispy artisan crust loaded with spicy pepperoni slice and drizzled with hot honey.", price=429.0, vegeterian=False, picture="https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r19, name="Truffle Garlic Breadsticks", description="Freshly baked dough strips brushed with garlic butter and drizzled with black truffle oil.", price=189.0, vegeterian=True, picture="https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r19, name="Caprese Salad with Mozzarella", description="Thick slices of fresh mozzarella, vine tomatoes, fresh basil and balsamic reduction.", price=239.0, vegeterian=True, picture="https://images.unsplash.com/photo-1592417817098-8f3d6ef23a81?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r19, name="Sicilian Cannoli with Ricotta", description="Crispy pastry shell stuffed with sweet ricotta cream, chocolate chips & pistachio.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=600&q=80")

    # 20. Smoothie & Juice Bar Express
    r20 = Restaurant.objects.create(
        name="Smoothie & Juice Bar Express",
        picture="https://images.unsplash.com/photo-1610970881699-44a5587cabec?auto=format&fit=crop&w=800&q=80",
        cuisine="Juices • Acai Bowls • Smoothies",
        rating=4.8
    )
    Item.objects.create(restaurant=r20, name="Dragonfruit Acai Smoothie Bowl", description="Blended organic acai and dragonfruit topped with banana, granola, chia & berries.", price=249.0, vegeterian=True, picture="https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r20, name="Passionfruit Mango Breeze Smoothie", description="Refreshing blend of fresh mango pulp, passionfruit, Greek yogurt & honey.", price=169.0, vegeterian=True, picture="https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r20, name="Protein Power Peanut Butter Shake", description="Banana, organic peanut butter, almond milk, and plant protein powder shake.", price=199.0, vegeterian=True, picture="https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r20, name="Fresh Watermelon & Mint Chiller", description="100% fresh pressed cold watermelon juice with crushed ice and fresh mint.", price=139.0, vegeterian=True, picture="https://images.unsplash.com/photo-1589733955941-5eeaf75434d8?auto=format&fit=crop&w=600&q=80")
    Item.objects.create(restaurant=r20, name="Whole Wheat Veggie Club Sandwich", description="Triple decker toasted sandwich filled with avocado, cucumber, tomato & hummus.", price=189.0, vegeterian=True, picture="https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=600&q=80")

    print("Successfully seeded 20 restaurants and 100 menu items!")


if __name__ == "__main__":
    seed()


