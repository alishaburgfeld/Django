from django.db import models


class User(models.Model):
    pass

class Restaurant(models.Model):
    pass


class Order(models.Model):
    # A user has many orders
    # An order belongs to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="orders")
    # An order belongs to a restaurant
    # A restaurant has many orders
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name="orders")


class FoodItem(models.Model):
    pass

class OrderFoodItem(models.Model):
    # An order_food_item belongs to a food_item
    # A food item has many order_food_items (I think they have this the wrong way around??)
    food_item= models.ForeignKey(FoodItem, on_delete=models.CASCADE,related_name="order_food_items")
    # An order_food_item belongs to an order
    # An order has many order_food_items
    order= models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_food_items")


# Associations

# And finally if you have set up your associations correctly a user should have many food items through orders. See the final test.




