import boto3
import os

# Servicio de AWS a usar

s3 = boto3.resource('s3')

# Listar Buckets disponibles

def list_buckets():
    
    print('Buckets disponibles: ')

    for bucket in s3.buckets.all():
        print(f"""
        {bucket.name}
        """)

# Listar archivos disponibles

def list_bucket_files(bucket_name):

    print('Key disponibles: ')
    
    for objects in s3.Bucket(bucket_name).objects.all():
        print(f"""
            {objects.key}
        """)

# Acciones disponibles

print("""

Ingrese 1 para crear un bucket

Ingrese 2 para crear una carpeta

Ingrese 3 para subir un archivo

Ingrese 4 para subir multiples arhivos

Ingrese 5 para descargar un archivo

Ingrese 6 para descargar todos los archivos de un bucket

""")

required_action = input('')

if required_action == '1':

    # Crear nuevo Bucket

    new_bucket_name = input('Ingrese nombre del nuevo bucket: ')
    
    s3.create_bucket(
        ACL='private',
        Bucket=new_bucket_name,
        )
    
    print(f'El bucket {new_bucket_name} se creo exitosamente...')

elif required_action == '2':

    list_buckets()

    # Crear carpeta

    bucket_name = input('Ingrese nombre del bucket: ')
    folder_name = input('Ingrese nombre de la nueva carpeta: ')

    folder_name = folder_name + '/'

    s3.Bucket(bucket_name).put_object(Key=(folder_name))

    print('La carpeta se creo exitosamente...')

elif required_action == '3':

    list_buckets()

    # Subir archivo

    bucket_name = input('Ingrese nombre del bucket: ')
    relative_route = input('Ingrese ruta relativa del archivo: ')
    key = input('Ingrese nombre y tipo de archivo: ')

    s3.Bucket(bucket_name).upload_file(relative_route, key)
    
    print('El archivo se subio exitosamente...')

elif required_action == '4':

    list_buckets()

    bucket_name = input('Ingrese nombre del bucket: ')
    
    list_bucket_files(bucket_name)

    # Subir multiples archivos de una carpeta

    folder_absolute_route = input('Ingrese ruta absoluta de la carpeta: ')
    relative_route = input('Ingrese ruta relativa de la carpeta: ')
    folder_key = input('Ingrese key si desea subir los archivos a una carpeta del bucket: ')


    for key in os.listdir(folder_absolute_route):
            path = relative_route + key
            key = folder_key + key
            s3.Bucket(bucket_name).upload_file(path, key)

    print('Los archivos se subieron exitosamente...')

elif required_action == '5':

    list_buckets()

    bucket_name = input('Ingrese nombre del bucket: ')
    
    list_bucket_files(bucket_name)

    # Descargar archivo

    key = input('Ingrese key del archivo: ')
    absolute_route = input('Ingrese ruta absoluta de la carpeta donde desea guardar el archivo: ')

    s3.Bucket(bucket_name).download_file(key, absolute_route)

    print('El archivo se descargo exitosamente...')

elif required_action == '6':

    list_buckets()

    # Descargar todos los archivos de un bucket

    bucket_name = input('Ingrese nombre del bucket: ')
    absolute_route = input('Ingrese ruta absoluta de la carpeta donde desea guardar los archivos: ')

    for objects in s3.Bucket(bucket_name).objects.all():
                
                path = absolute_route + objects.key
                key = objects.key
                s3.Bucket(bucket_name).download_file(key, path)

    print('Descarga exitosa...')

else:

    print('Por favor, indique una acción')

