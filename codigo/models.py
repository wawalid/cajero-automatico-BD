from datetime import datetime


class Usuario():
    # id_usuario = 0
    def __init__(self, dni, contraseña, fecha_alta, fecha_inactivacion):
        # self.id_usuario = Usuario.id_usuario
        # self.id_usuario += 1
        self.dni = dni
        self.contraseña = contraseña
        # self.fecha_alta = fecha_alta
        # self.fecha_inactivacion = fecha_inactivacion


class Sesiones():
    # id_sesion = 0
    def __init__(self, id_usuario, fecha_inicio_sesion, fecha_fin_sesion):
        # self.id_sesion = Sesiones.id_sesion
        # self.id_sesion += 1
        self.id_usuario = id_usuario
        # self.fecha_inicio_sesion = fecha_inicio_sesion
        # self.fecha_fin_sesion = fecha_fin_sesion

class Transaccion():
    # id_transaccion = 0
    def __init__(self, id_usuario, importe, fecha_transaccion):
        # self.id_transaccion = Transaccion.id_transaccion
        # self.id_transaccion += 1
        self.id_usuario = id_usuario
        self.importe = importe
        # self.fecha_transaccion = fecha_transaccion




