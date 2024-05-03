import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiPaciente as uipc

def NewPaciente ():

      title =  """
      **************************
      ** REGISTRO DE PACIENTE **
      **************************
      """
      gf.borrar_pantalla()
      print(title)
      identificacion = input("ingrese el numero de identificacion : ")
      nombresApellidos = input("ingrese los nombres y apellidos :" )
      NrCelular = input('ingrese su numero de celular:')
      telefono = input("ingrese su numero de telefono :")
      edad = input('ingrese su edad :')
      genero = input('ingrese su genero M/F:')

   
      paciente = {
         'identificacion': identificacion,
         'nombresApellidos': nombresApellidos,
         'NrCelular' : NrCelular,
         'telefono' : telefono,
         'edad' : edad,
         'genero' : genero,
      }
   
      cf.AddData('data',identificacion,paciente)
      gf.centroMedicoAL.get('data').update({identificacion:paciente})
      if(bool(input('Desea Registrar Otro Paciente  S(si) o enter (no)'))):
       NewPaciente()
      else:
       uipc.MenuPaciente

def   searchData():
      criterio = input('ingrese el numero de identificacion del paciente:')
      data=gf.centroMedicoAL.get(data).get(criterio)
      return data

def   ModifyData():
      datapaciente = searchData()
      identificacion,nombre_apellido,nuumero_celular,telefono,edad,genero = datapaciente.values()
      for key in datapaciente.keys():
          if(key != 'identificacion'and key != 'paciente'):
              if (bool(input('Desea modificar el {key}  S(si) o enter (no)'))):
                  datapaciente[key] = input (f'ingrese el numero valor para (key)')
      gf.centroMedicoAL.get('data').update({identificacion:datapaciente})
      cf.UpsateFile(gf.centroMedicoAL)
      uipc.MenuPaciente
          




      
        

   