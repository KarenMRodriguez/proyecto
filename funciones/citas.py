import  os
import json
import funciones.globales as gf
import modules.corefilesCT as cf
import ui.Uicitas as uict


def  newcita():
  title =  """
    **********************
    ** AGENDAR DE CITAS **
    **********************
    """
  gf.borrar_pantalla()
  print(title)
  identificacion = input ('ingrese numero de identificacion :')
  nombresApellidos = input ('ingrese los nombres y apellidos :')
  especialista = input ('ingree el especialista:')
  correo = input ('ingres el correo electronico :')
  fecha = input('ingrese el DD/MM/AAAA:')

  cita = {
    'identificacion': identificacion,
    'nombre_apellido' : nombresApellidos,
    'especalista' : especialista,
    'correo': correo,
    'fecha': fecha,
    'cita': cita
  }

  cf.AddData('data',identificacion,cita)

  gf.centroMedico.get('data').update({identificacion:cita})
  if(bool(input("desdea agendar ua cita S(si)) o Enter(no)"))):
    newcita()
  else:
    uict.menucitas(0)
    
def  searchData():
  criterio = input('ingrese la identificacion del paciente:')
  data=gf.centroMedicoAL.get('data').get(criterio)
  return data

def Modifydata():
  datacita = searchData() 
  identificacion,nombresApellidos,correo,especialista,correo,fecha = datacita.values()
  for key in datacita.keys():
          if(key != 'identificacion'and key != 'cita'):
              if (bool(input('Desea modificar el {key}  S(si) o enter (no)'))):
                  datacita[key] = input (f'ingrese el numero valor para (key)')
                  gf.centroMedicoAL.get('data').update({identificacion:datacita})
  uict.menucitas


