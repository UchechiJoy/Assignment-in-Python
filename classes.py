class User():

    first_name=""
    last_name=""
    email_address=""
    phone_number=""
    alergies=""
    food_diet=""
    user_type=""

    def get_full_name(self):

        return f"{self.first_name}{self.last_name}"
    
class MenuItem():
    name=""
    description=""
    service_size=""
    allergens=""

class Price():
    totalPrice=""


class Order():
  orderId = ""
  orderedMeal = ""
  quantity = ""
  short_description = ""
  isPacked = False
  isTake_away=""
  additional_needs = ""
  price = Price.totalPrice

class KitchenStaff:
    pass

user=User()