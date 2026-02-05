#Multiple Inheritance
class Camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality

    def display_camera_details(self):
        print(f"Camera Quality:{self.camera_quality}")

class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality

    def display_music_details(self):
        print(f"Sound Quality:{self.sound_quality}")

class SmartPhone(Camera,MusicPlayer):
    def __init__(self,brand,camera_quality,sound_quality):
        self.brand=brand
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)

    def display_smartphone_details(self):
        print("Brand:", self.brand)

phone = SmartPhone("Samsung", "64 MP", "Dolby Atmos")
phone.display_camera_details()
phone.display_music_details()
phone.display_smartphone_details()



#Multilevel Inheritance
class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price
    
    def display_product(self):
        print(f"Product_name:{self.product_name},Price:{self.price}")

class ElectronicProduct(Product):
    def __init__(self,product_name,price,brand,warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty

    def display_electronic_product(self):
        print(f"Brand:{self.brand},Price:{self.price}")

class MobilePhone(ElectronicProduct):
    def __init__(self,product_name,price,brand,warranty,ram,storage):
        super().__init__(product_name,price,brand,warranty)
        self.ram=ram
        self.storage=storage

    def display_mobile_details(self):
        print(f"RAM:{self.ram},Storage:{self.storage}")

Mobile=MobilePhone("IPhone",50000,"Apple","1 year","8GB","256 GB")
Mobile.display_product()
Mobile.display_electronic_product()
Mobile.display_mobile_details()



