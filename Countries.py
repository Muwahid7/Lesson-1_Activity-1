class india():
    def capital(self):
        print("Delhi is the capital of india")
    def language(self):
        print("Hindi is the National language of india")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("English is the National language of USA")
    def type(self):
        print("USA is a developed country")
obj_ind = india()
obj_USA = USA()
for country in (obj_ind,obj_USA):
    country.capital()
    country.language()
    country.type()