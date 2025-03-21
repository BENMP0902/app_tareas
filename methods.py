# Un archivo que contiene todas las acciones que un usiario puede realizar
from models import Usuario, Task

from extensions import jwt
from flask_jwt_extended import create_access_token

#DATETIME nos permite trabajar con fechas y horas
#Timedelta realiza la conversion de dias, horas, minutos, etc a formato Linux
from datetime import timedelta

#Metodo para que el usuario pueda crear una cuenta
def crear_cuenta(nombre, correo, password):

    usuario_existente = Usuario.query.filter_by(email=correo).first()
    #Revisamos si la quey es diferente a None
    if usuario_existente is not None:
        print('El correo ya existe')
        return{'status': 'error', 'error': 'La cuenta ya esta registrada'}

    #Esto solo se ejecuta si el usuario no existe en la db
    print(f"Intentando crear cuenta con: {nombre}, {correo}, {password}")  # 👈 Agrega esto para depuración
    nuevo_usuario = Usuario(name = nombre, email = correo)

    nuevo_usuario.hashear_password(password_original=password)
 

    #Guardamos el nuevo usuario en la base de datos
    nuevo_usuario.save()

    return {'status': 'ok', 'email': correo}

def iniciar_sesion(correo, password):


    #VAriable que contenga usuarios filtrados por un parametro
    usuarios_existentes = Usuario.query.filter_by(email = correo).first()

    #1. Si el usuario existe puede iniciar sesion

    #2. Si el ussuario no existe no puede iniciar sesion

    #Si el ususario no existe
    if usuarios_existentes is None:
        print('La cuenta no existe')
        return{'status': 'error', 'error': 'La cuenta no existe'}

    #Si la contraseña del formulario esta en la db 
    if usuarios_existentes.verificar_password(password_plano = password):
        
        #Variable de caducidad del token
        caducidad = timedelta(minutes=10)

        print('Inico de sesion exitoso :)')
        token_de_acceso = create_access_token(
            identity=usuarios_existentes.name, 
            expires_delta=caducidad,
            #Se agrega al payload el id del usuario
            additional_claims={'user_id': usuarios_existentes.id})
        
        print(token_de_acceso)
        return {'status': 'ok', 'token': token_de_acceso}

    # Usuario existente y contraseña incorrecta
    else:
        print('Contraseña incorrecta')
        return {'status': 'error', 'error': 'Contraseña incorrecta'}
        
def encontrar_todos_los_usuarios():

    #Variable que contendra la respuesta de la db
    usuarios = Usuario.query.all()

    print(usuarios)

    return usuarios
    #Busqueda de usuario en la db
    
def encontrar_usuario_id(user_id):

    #Variable que contendra la respuesta de la db
    usuario = Usuario.query.filter_by(id=user_id).first()

    if usuario == None:
        return {'status': 'error', 'error': 'El usuario no existe'}
    return usuario

def crear_tarea(user_id, nombre_tarea, descripcion_tarea):
    nueva_tarea = Task(
        user_id=user_id,
        name=nombre_tarea,  # Usamos 'name' en lugar de 'nombre_tarea'
        description=descripcion_tarea  # Usamos 'description' en lugar de 'descripcion_tarea'
    )
    nueva_tarea.save()
    return {'status': 'ok', 'tarea_id': nueva_tarea.id}

def obtener_tareas_usuario(user_id):
    tareas = Task.query.filter_by(user_id=user_id).all()
    return tareas

def actualizar_estado_tarea(tarea_id, nuevo_estado):
    tarea = Task.query.get(tarea_id)
    if tarea:
        tarea.status = nuevo_estado  # Usamos 'status' en lugar de 'estado'
        tarea.save()
        return {'status': 'ok'}
    return {'status': 'error', 'error': 'Tarea no encontrada'}

def eliminar_tarea(tarea_id):
    tarea = Task.query.get(tarea_id)
    if tarea:
        tarea.delete()
        return {'status': 'ok'}
    return {'status': 'error', 'error': 'Tarea no encontrada'}