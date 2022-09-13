## Authenticate-access-to-AWS-resources-using-MFA-token-through-the-command-prompt

### Step 1:

Here attached a python file named as aws_assume_role_script, you inculde ACCESS_KEY_ID, SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, ROLE_ARN and MFA_ARN in this file.

MFA arn avaialble in AWS--> IAM--> Users--> Security Credentials--> Assigned MFA device--> MFA arn

### Step 2:

#### Open a Command prompt

Run python file aws_assume_role_script

````
python aws_assume_role_script.py
````
Enter MFA token: 

You receive an output with temporary credentials and an expiration time (by default, 12 hours) similar to the following:

{
        "SessionId": "session-Id",
        "SessionKey": "session-key",
        "SessionToken": "session-token",
    }

### Step 3:

#### open another command prompt for configure aws credentials

````
aws configure --profile "profile_name"
````

aws_access_key_id:

aws_secret_access_key:

Default Region Name:

Default output format:

### Step 4:

Edit AWS credentials file availabe in the path `C:\Users\username\.aws`

AWS Session Token include in credentials file

AWS_SESSION_TOKEN= "session token paste here"

### Step 5:

Finally, Check the access to AWS resources through the command prompt.

````
aws s3 ls --profile "profile_name"
````

END

