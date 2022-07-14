from .models import Product 
from django.db.models import Avg, Q, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        for product in Product.objects.all():
            if product.model == model:
                return product
    # Also could do:
    # return Product.objects.get(model__iexact=model)

    #3
    @classmethod
    def last_record(cls):
        # finds the last record inserted
        # DOES NOT WORK: return Product.objects.latest(id) #check if this works
    #this also works:
        return Product.objects.all().last()

    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact=rating)

    #5
    @classmethod
    def by_rating_range(cls, ratingOne, ratingTwo):
        return Product.objects.filter(rating__range=(ratingOne, ratingTwo))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) & Q(color=color))
        #also:
        #return Product.objects.filter(rating__exact=rating).filter(color__exact=color)

    #7
    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) | Q(color=color))
        #also:
        #return Product.objects.filter(rating__exact=rating) | Product.objects.filter(color__exact=color)

    @classmethod
    def no_color_count(cls):
        #"""returns the count of products that have no color value"""
        return Product.objects.filter(color__isnull=True).count()

    #9
    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        """returns products below a price or above a rating"""
        return Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))
        #also:
        #return Product.objects.filter(price_cents__lt=price) | Product.objects.filter(rating__gt=rating1) 

    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        """returns products ordered by category alphabetical and decending price"""
        return Product.objects.order_by("category","-price_cents")
        #return Product.objects.all().order_by('category', '-price_cents')

    #11
    @classmethod
    def products_by_manufacturer_with_name_like(cls,string):
        return Product.objects.filter(manufacturer__contains=string)
        #return Product.objects.filter(manufacturer__icontains=like)

    @classmethod
    def manufacturer_names_for_query(cls,string):
    #     """returns a list of manufacturer names that match query"""
        return Product.objects.filter(manufacturer__contains=string).values_list('manufacturer', flat=True)
        #return list(Product.objects.filter(manufacturer__icontains=name).values_list('manufacturer', flat=True))

    #13
    @classmethod
    def not_in_a_category(cls,category):
    #     """returns products that are not in a category"""
        return Product.objects.exclude(category__iexact=category)
    
    
    @classmethod
    def limited_not_in_a_category(cls, category, limit):
    #     """returns products that are not in a category up to a limit"""
        return Product.objects.exclude(category__iexact=category)[:limit]

    @classmethod
    def category_manufacturers(cls,category):
        return list(Product.objects.filter(category__iexact=category).values_list('manufacturer', flat=True))
    #     """returns an array of manufacturers for a category"""

    #16
    @classmethod
    def average_category_rating(cls,category):
        return Product.objects.aggregate(rating__avg=Avg('rating', filter=Q(category=category)))
        #why is the Q needed here?

    
    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(price_cents__max=Max('price_cents'))
        
    #18
    @classmethod
    def longest_model_name(cls):
        #I didn't know how to do this one. Michael's answer:
        return Product.objects.annotate(model_length = (Length('model'))).order_by('-model_length')[:1][0].pk

    @classmethod
    def ordered_by_model_length(self):
        #I didn't know how to do this one. Michael's answer:
        return Product.objects.order_by(Length('model'))