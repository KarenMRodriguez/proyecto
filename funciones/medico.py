import os
import json
import funciones.globales as gf
import modules.corefileMD as cf
import ui.UiMedico as umc

def NewMedic ():

   title =  """
   *********
   * REGISTRO DE MEDICOS *
   *********
   """
   gf.borrar_pantalla()
   print(title)
   identificacion = input("ingrese el numero de identificacion : ")
   nombreApellido = input("ingrese los nombres y apellidos :" )
   correo = input("ingrese su correo electronico :" )
   Nrconsultorio = input("ingrese el numero del consultorio:")
   horarioAtencion = input("ingrese la hora:")
   especialidad = input ('ingresa la especialidad:')

   medico = {
      'identificacion': identificacion,
      'nombreApellido': nombreApellido,
      'correoElectronico' : correo, 
      'consultorio' : Nrconsultorio,
      'horarioAtencion': horarioAtencion,
      'especialidad': especialidad
   }
   
   cf.AddData('data',identificacion,medico)
   gf.centroMedicoAL.get('data').update({identificacion:medico})
   if (bool(input("desdea ingresar otro medico S(si) o Enter(no)"))):
      NewMedic()
   else:
    umc.MenuMedico(0)

def searchData(identificaion):
   dataMedico=gf.centroMedicoAL.get('data').get(identificaion)
   return dataMedico

def editMedic():
   identificacion = input("Ingrese la identificación del médico que desea editar: ")
   dataMedico = searchData(identificacion)

   if dataMedico:
      print("Datos actuales del médico:")
      print(dataMedico)

        # Solicitar al usuario los campos que desea modificar
      fields_to_edit = ['nombreApellido', 'correoElectronico', 'consultorio', 'horarioAtencion', 'especialidad']
      for field in fields_to_edit:
         if bool(input(f"Desea modificar {field}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {field}: ")
               dataMedico[field] = new_value

        # Actualizar los datos del médico
      gf.centroMedicoAL.get('data').update({identificacion: dataMedico})
      cf.UpsateFile(gf.centroMedicoAL)
      print("Datos del médico actualizados correctamente.")
   else:
        print("No se encontró ningún médico con la identificación proporcionada.")





