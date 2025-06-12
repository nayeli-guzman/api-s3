import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['body']['bucket_name']
    directorio = event['body']['directorio']  # El nombre del "directorio" a crear
    
    try:
        # S3 no tiene directorios reales, pero podemos simularlos subiendo un objeto vacío con un prefijo
        s3.put_object(Bucket=bucket_name, Key=f"{directorio}/")
        
        return {
            'statusCode': 200,
            'body': f"Directorio '{directorio}' creado en el bucket '{bucket_name}'"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error al crear el directorio: {str(e)}"
        }

