import boto3
import os

# Representa el servicio de AWS a usar

s3 = boto3.resource('s3')

# Crear nuevo Bucket

def create_new_bucket(new_bucket_name):
    
    s3.create_bucket(
        ACL='private',
        Bucket=new_bucket_name,
        )
    
    print(f'El bucket {new_bucket_name} se creo exitosamente...')

# Listar Buckets disponibles

def list_buckets():
    
    print('Buckets disponibles: ')

    for bucket in s3.buckets.all():
        print(f"""
        {bucket.name}
        """)

# Crear Carpeta

def create_new_folder(bucket_name, folder_name):
    
    folder_name = folder_name + '/'

    s3.Bucket(bucket_name).put_object(Key=(folder_name))

    print('La carpeta se creo exitosamente...')

# Subir Archivo

def upload_file(bucket_name, relative_route, key):
    
    s3.Bucket(bucket_name).upload_file(relative_route, key)
    
    print('El archivo se subio exitosamente...')

# Subir Multiples archivos de una carpeta

def upload_multiple_file(bucket_name, folder_absolute_route, relative_route, folder_key=''):
    
    for key in os.listdir(folder_absolute_route):
            path = relative_route + key
            key = folder_key + key
            s3.Bucket(bucket_name).upload_file(path, key)

    print('Los archivos se subieron exitosamente...')

# Listar Archivos dentro de un Bucket

def list_bucket_files(bucket_name):

    print('Archivos disponibles: ')
    
    for objects in s3.Bucket(bucket_name).objects.all():
        print(f"""
            {objects.key}
        """)

# Descargar archivos

def download_file(bucket_name, key , absolute_route):

    s3.Bucket(bucket_name).download_file(key, absolute_route)

    print('El archivo se descargo exitosamente...')

# Descargar todos los archivos de un Bucket 

def download_all_files(bucket_name, absolute_route):
    
    for objects in s3.Bucket(bucket_name).objects.all():
        
        path = absolute_route + objects.key
        key = objects.key
        s3.Bucket(bucket_name).download_file(key, path)

    print('Descarga exitosa...')






print('todo ok')