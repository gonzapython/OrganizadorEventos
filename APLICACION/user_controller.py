class UserController():
    def __init__(self, user_model):
        self.user_model = user_model

    def login(self, user_model):
        return self.user_model.login()

    def registrarse(self, user_model):
        return self.user_model.registrarse()

