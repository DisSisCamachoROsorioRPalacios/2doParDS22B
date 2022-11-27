#!/usr/bin/python
#-*- coding: utf-8 -*-

from gestion_stock import gestion_stock

class medicamento(gestion_stock):
    def __init__(self,idMedicamento,ubicacion,nombre,cantidad):
        gestion_stock.__init__(self,idMedicamento,ubicacion,cantidad)
        self.idMedicamento = None
        self.nombre = None
        self.cantidad = None

    def curar(self, ):
        print("El paciente tomo elmedicamento correctamente")

    def caducar(self, ):
        print("El medicamento ha caducado ")
    
    def __toString__(self):
        return gestion_stock.__toString__(self)+"idMedicamento:{} Nombre : {} ubicacion:{} cantidad:{}".format(self.idMedicamento,self.nombre,self.ubicacion,self.cantidad)

medica= medicamento(1,"zumpango","paracetamol",12)
print(medica.__toString__())
