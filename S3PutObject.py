#Talk python to me

import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='s3-put-object-demo'

	transactionToUpload = {}
	transactionToUpload['EmpId'] = '12345'
	transactionToUpload['fname'] = 'Sanjeev'
	transactionToUpload['lname'] = 'Choudhary'
	transactionToUpload['DOJ'] = "10th-June-2019"
	transactionToUpload['Department'] = 'Digital'

	fileName = 'EmpInfo' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')
