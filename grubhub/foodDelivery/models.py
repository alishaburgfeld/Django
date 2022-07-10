from django.db import models


class Users(models.Model):
    pass

class Orders(models.Model):
    # A user has many orders
    # An order belongs to a user
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="users")

class Restaurants(models.Model):
    order= models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="orders")

class FoodItems(models.Model):
    pass

class OrderFoodItems(models.Model):
    pass


# Associations


# A restaurant has many orders
# An order belongs to a restaurant
# An order has many order_food_items
# An order_food_item belongs to an order
# A food item has many order_food_items
# An order_food_item belongs to a food_item
# And finally if you have set up your associations correctly a user should have many food items through orders. See the final test.


# class User(models.Model):
#     pass

# class Shop(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    
# #product 
# class Product(models.Model):
#     shop= models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    

# class Review(models.Model):
#     product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
#     user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewed_products")
    





