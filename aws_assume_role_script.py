import os
import json
import subprocess
import boto3


os.system("set AWS_ACCESS_KEY_ID=")
os.system("set AWS_SECRET_ACCESS_KEY=")
os.system("set AWS_SESSION_TOKEN=")


ACCESS_KEY_ID = "......." ## enter access id of main account
SECRET_ACCESS_KEY = "....." ## enter secrect access key of main account
AWS_DEFAULT_REGION = "....." ## enter AWS Region
MFA_ARN= "........"  ## enter mfa arn found in IAM section of aws console
ROLE_ARN = "......." ## enter 


#subprocess.Popen(["aws configure set aws_access_key_id {ACCESS_KEY_ID}; aws configure set aws_secret_access_key #{SECRET_ACCESS_KEY}; aws configure set default.region {AWS_DEFAULT_REGION}"],  shell=True)

print(ACCESS_KEY_ID)
print(SECRET_ACCESS_KEY)
print(AWS_DEFAULT_REGION)

#subprocess.Popen("aws configure set aws_access_key_id ACCESS_KEY_ID ", shell=True)
#subprocess.Popen("aws configure set aws_secret_access_key SECRET_ACCESS_KEY ", shell=True)
#subprocess.Popen("aws configure set default.region AWS_DEFAULT_REGION ", shell=True)

client = boto3.client('sts', 'us-west-1')
role_session_name = "AssumeRoleSession"
mfa_token = input("enter mfa token: ")


response = client.assume_role(RoleArn=ROLE_ARN,
            RoleSessionName=role_session_name,
            DurationSeconds=43200,    # change value if required
            SerialNumber=MFA_ARN,
            TokenCode=mfa_token)

tmp_credentials = {
    'sessionId': response['Credentials']['AccessKeyId'],
    'sessionKey': response['Credentials']['SecretAccessKey'],
    'sessionToken':response['Credentials']['SessionToken']
}
print(json.dumps(tmp_credentials))

