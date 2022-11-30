class Flipkart:
    def __init__(self,app_id,app_secret) -> None:
        self.app_id = app_id
        self.app_secret= app_secret
    def headers(self):
        return "headers"
    
    def get_orders(self):
        print("Flipkart orders")

    def cancell_order(self,order_id):
        print(f"{order_id} cancelled")
    
    def confirm_order(self,order_id):
        print(f"{order_id} Picked")

class Amazon:
    def __init__(self,username,password,auth) -> None:
        pass
    def get_orders(self):
        print("Amazon orders")
    
    def cancell_order(self,order_id):
        print(f"{order_id} cancelled")
    
    def confirm_order(self,order_id):
        print(f"{order_id} Picked")


class Client:
    def auth(self,site,**kwargs):
        if site == "flipkart":
            self.flipkart = Flipkart(kwargs["app_id"],kwargs["app_secret"])
        elif site == "amazon":
            self.amazon = Amazon(kwargs['username'],kwargs["password"],kwargs["auth_secret"])

    def get_orders(self):
        for site in {"flipkart","amazon","myntra","someother"}.intersection(set(dir(self))):
            getattr(self,site).get_orders()

    def cancel_order(self):
        getname(self)



c1 = Client()
c1.auth("flipkart",app_id="some_id",app_secret="some_secret")
print("CLIENT-1")
c1.get_orders()


c2 = Client()
c2.auth("amazon",username="username",password="password",auth_secret="secret")
c2.auth("flipkart",app_id="some_id",app_secret="some_secret")
print("CLIENT-2")
c2.get_orders()
