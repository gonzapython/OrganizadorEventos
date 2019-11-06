from user_controller    import UserController
from user_view          import UserView
from user_model         import User


user_model      = User()
user_controller = UserController(user_model)
user_view       = UserView(user_controler)


def main():
    imprimir_amistad()

    opcion = inicio_amistad()

    if  opcion == '1':
        userview.login()
    elif opcion == '2':
        userview.registrarse()


# ------

main()
