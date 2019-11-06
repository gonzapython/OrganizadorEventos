
import json
import os

from excepciones import (UsuarioNoExiste,
                         ContraseñaIncorrecta)


class User(self):
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def imprimir_amistad():
        print("                                                                                          ")
        print(" ---------------------------------------------------------------------------------------- ")
        print(" ---------------------------------------------------------------------------------------- ")
        print("           *** ¡¡¡¡¡ BIENVENIDO a tu Portal  AMISTAD-DivinoTesoro- !!!!! ***              ")
        print("                                                                                          ")
        print(" 1 => Si YA estás registrado:  Teclea 1 para introducir tu nombre de usuario y contraseña ")
        print("                                                                                          ")
        print(" 2 => Si NO estás registrado:  Teclea 2 para registrarte..... y ser FELIZ                 ")
        print("                                                                                          ")
        print(" 3 => SALIR: Teclea 3 para Salir.  ¡¡Hasta pronto!!                                       ")
        print(" ---------------------------------------------------------------------------------------- ")
        print("                                                                                          ")

    def inicio_amistad(self):
        opcion = int(input( " Teclea 1 , 2  ó  3: > "))
        if opcion == 1 or opcion == 2 or opcion == 3:
            return opcion
        inicio_amistad()

    # -- ésta es común a login y registrarse
    def _comprobar_existe_usuario(self, usuario):
        lista_de_directorios = os.listdir('./USUARIOS')
        for directorio in lista_de_directorios:
            if directorio != usuario.upper():
                raise UsuarioNoExiste


    # -- Parte de LOGIN -----------------------------------------------------

    def _validar_usuario_login(self):

            usuario, contraseña = login()
            if not comprobar_existe_usuario(usuario):
                print(f'** NO existe el usuario {usuario}')
                return
            if not comprobar_contraseña(usuario, contraseña):
                print(f'** Contraseña incorrecta ')
                return

            return usuario

    def _comprobar_contraseña(self, usuario, contraseña):
        datos_usuario = dict()

        with open('./USUARIOS/'+usuario.upper()+'/datos_usu.json', 'r') as json_file:
            datos_usuario = json.load(json_file)

        if datos_usuario["contrasena"] != contraseña:
            raise ContraseñaIncorrecta

    def _mostrar_solicitudes_amistad(self, usuario):
        print("                              ")
        print(" ---------------------------- ")
        print(" ** SOLICITUDES de AMISTAD ** ")

        lista_de_ficheros = os.listdir('./USUARIOS/'+usuario.upper())

        cont = 0
        for ficheros in lista_de_ficheros:
            if not(ficheros.find("tos_usu") > 0):
                cont += 1
                print("  --->>>>", ficheros[:-5])

        if cont == 0:
            print(" No tienes solicitudes de amistad actualmente ")
            print("                                              ")

    def _mostrar_opciones_disponibles(self):
        print("                                                     ")
        print(" --------------------------------------------------- ")
        print("    *** MENÚ PRINCIPAL - Opciones Disponibles ***    ")
        print("                                                     ")
        print(" 1 => Listar usuarios y solicitar amistad (opcional) ")
        print("                                                     ")
        print(" 2 => VOLVER                                         ")
        print("                                                     ")
        print(" 3 => SALIR                                          ")
        print("                                                     ")
        print(" --------------------------------------------------- ")

        opcion = int(input( " Introduce tu opción: > "))
        return opcion

    def _listar_usuarios(self):
        #-- listar usuarios
        lista_de_ficheros = list()
        lista_de_ficheros = os.listdir('./USUARIOS')
        if len(lista_de_ficheros) !=0:
            print(" Usuarios actuales de AMISTAD: ")
            for index, fichero in enumerate(lista_de_ficheros):
                print(f'{index} .-> {fichero}')
        else:
            print(" No hay usuarios de AMISTAD hasta el momento ")
            return 0

        #-- solicitar_amistad
        print(" ¿A quién quieres enviar una solicitud de Amistad? ")
        opcion = input( " Introduce el número o 'N' si no quieres amistad de momento: > ")
        if opcion.upper() == 'N':
            return 0

        amigo = lista_de_ficheros[int(opcion)]
        return amigo

    def _tratar_opciones(self, opcion, usuario):
        if opcion == 1:
            print("  opcion  1  ")
            amigo = listar_usuarios()
            if amigo != 0:
                enviar_solicitud_amistad(usuario, amigo)

            opcion = mostrar_opciones_disponibles()
            opcion = tratar_opciones(opcion, usuario)

        elif opcion == 2:
            return opcion
        elif opcion == 3:
            return opcion

    def _enviar_solicitud_amistad(self, usuario, amigo):
        datos_amigo = {'nombre': usuario}

        directorio_amigo = amigo.upper()
        fichero_usuario = usuario.upper()+'.JSON'
        with open('./USUARIOS/'+directorio_amigo+'/'+fichero_usuario, '+w') as json_file:
            json.dump(datos_amigo, json_file)

        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
        print(" >>>>>> Soliciotud enviada... ")
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>> ")


    # -- LOGIN --------------------------------------
    def login(self):
        print(" Escribe tu usuario y tu contraseña ")
        usuario = input(" Usuario: ")
        contraseña = input(" Contraseña: ")
        usuario = self._validar_usuario_login()
        if opcion == 3:
            return
        if usuario == 0:
            return
        #
        self._mostrar_solicitudes_amistad(usuario)
        opcion = self._mostrar_opciones_disponibles()
        opcion = self._tratar_opciones(opcion, usuario):
        if opcion == 2:
            #main()  -- no sé
            pass
        elif opcion == 3:
            return
    # --------------------------------------------------

    #return usuario, contraseña



    # -- Parte de REGISTRARSE -----------------------------------------------

    def _grabar_usuario(self, usuario, contraseña):
        #-- Crear su carpeta
        os.mkdir('./USUARIOS/'+usuario.upper())

        #-- Crear diccionario con sus datos
        datos_usuario = {'nombre': usuario,
                        'contrasena': contraseña,}

        #-- Crear fichero con sus datos
        with open('./USUARIOS/'+usuario.upper()+'/datos_usu.json', '+w') as json_file:
            json.dump(datos_usuario, json_file)



    # -- REGISTRARSE --------------------------------------
    def registrarse(self):
        print(" Escribe tu usuario y tu contraseña (mínimo de 8 caracteres)")
        usuario = input(" Usuario: ")

        contraseña_primera_vez = input(" Primera vez: Contraseña (mínimo 8 caracteres): ")
        contraseña_segunda_vez = input(" Segunda vez: Contraseña (mínimo 8 caracteres): ")

        if len(contraseña_primera_vez) <8 or len(contraseña_segunda_vez) < 8:
            print(" Ha de ser de 8 caracteres como mínimo")
            registrarse()
        if contraseña_primera_vez != contraseña_segunda_vez:
            print(" No coinciden las contraseñas. Inténtalo de nuevo ")
            registrarse()

        if self._comprobar_existe_usuario(usuario):
            print(f'YA existe el usuario {usuario}')
            return

        if self._grabar_usuario(usuario, contraseña):
            print("                                                            ")
            print(" ***               YA estás registrado                  *** ")
            print("                                                            ")
            print(" Puedes entrar en AMISTAD escribiendo tu usuario/contraseña ")
            print("                                                            ")
            print(f'         ** ¡¡Hasta pronto!! {usuario} **                  ')
            print("                                                            ")
            return


        #return usuario, contraseña_primera_vez


