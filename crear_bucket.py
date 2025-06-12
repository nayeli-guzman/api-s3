import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['body']['bucket_name']  # El nombre del bucket recibido en el cuerpo de la solicitud

    try:
        # Crear un nuevo bucket
        s3.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': f"Bucket '{bucket_name}' creado exitosamente"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error al crear el bucket: {str(e)}"
        }

