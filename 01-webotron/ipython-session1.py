# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythoAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all()
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='satvautomatingaws-boto3')'
new_bucket = s3.create_bucket(Bucket='satvautomatingaws-boto3')
new_bucket = s3.create_bucket(Bucket='satvautomatingaws-boto3', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('history', '')
