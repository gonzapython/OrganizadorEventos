class UserView():
    def __init__(self, user_controler):
        self.user_controler = user_controler

    def login(self, user_controler):
        return self.user_controler.login()

    def registrarse(self, user_controler):
        return self.user_controler.registrarse()

