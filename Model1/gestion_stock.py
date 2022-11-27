#!/usr/bin/python
#-*- coding: utf-8 -*-

class gestion_stock():
    def __init__(self,idMedicamento,ubicacion,cantidad):
        #medicamento.__init__(self,idMedicamento,nombre,cantidad)
        self.idMedicamento = None
        self.ubicacion = None
        self.cantidad = None

    def agregar(self, ):
        pass

    def eliminar(self, ):
        pass

    def __toString__(self):
        return "idMedicamento:{}  ubicacion:{} ".format(self.idMedicamento,self.ubicacion)
