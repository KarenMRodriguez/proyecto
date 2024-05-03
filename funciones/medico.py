import os
import json
import funciones.globales as gf
import modules.corefileMD as cf
import ui.UiMedico as umc

def NewMedic ():

   title =  """
   *************************
   ** REGISTRO DE MEDICOS **
   *************************
   """
   gf.borrar_pantalla()
   print(title)
   identificacion = input("ingrese el numero de identificacion : ")
   nombreApellido = input("ingrese el nombres y apellidos :" )
   correo = input("ingrese su correo electronico :" )
   Nrconsultorio = input("ingrese el numero del consultorio:")
   horarioAtencion = input("ingrese la hora:")
   especialidad = input ('ingresa la especialidad:')

   medico = {
      'identificacion': identificacion,
      'nombre:Apellido': nombreApellido,
      'correoElectronico' : correo,
      'consultorio' : Nrconsultorio,
      'horarioAtencion': horarioAtencion,
      'especialidad': especialidad
   }
   
   cf.AddData('data',identificacion,medico)
   gf.centroMedicoAL.get('data').update({identificacion:medico})
   if(bool(input("desdea ingresar otro medico S(si)) o Enter(no)"))):
      NewMedic()
   else:
    umc.MenuMedico(0)

def searchData():
   criterio = input('ingrese la ID del medico:')
   dataMedico=gf.centroMedicoAL.get('dataMedico')
   return dataMedico


def Modifydata():
   dataMedico = searchData() 

   identificacion,nombreApellido,correo,Nrconsultorio = dataMedico.values()
   for key in dataMedico.keys():
      if(key != 'identificacion'and key != 'medico'):
         if (bool(input('Desea modificar el {key}  S(si) o enter (no)'))):
            searchData[key] = input (f'ingrese el numero valor para {key}')
   gf.centroMedicoAL.get('dataMedico').update({identificacion:dataMedico})
   umc.MenuMedico









