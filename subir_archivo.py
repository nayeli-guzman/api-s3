import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['body']['bucket_name']
    archivo_base64 = event['body']['archivo_base64']  # El archivo en formato base64
    archivo_nombre = event['body']['archivo_nombre']  # El nombre del archivo
    directorio = event['body']['directorio']  # El "directorio" donde guardar el archivo
    
    try:
        # Decodificar el archivo desde base64
        archivo_decodificado = base64.b64decode(archivo_base64)
        
        # Subir el archivo al "directorio" (prefijo) en S3
        s3.put_object(Bucket=bucket_name, Key=f"{directorio}/{archivo_nombre}", Body=archivo_decodificado)
        
        return {
            'statusCode': 200,
            'body': f"Archivo '{archivo_nombre}' subido exitosamente al directorio '{directorio}' en el bucket '{bucket_name}'"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error al subir el archivo: {str(e)}"
        }

