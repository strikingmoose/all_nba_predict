from constants import Constants
import boto3

# AWS should connect to default account because I've already configured AWS credentials via AWS CLI

# Create an ec2 resource
ec2 = boto3.resource('ec2')

# Set up
###############################################
# Create a VPC
# masterVpc = ec2.create_vpc(
#     DryRun = False,
#     CidrBlock ='10.0.0.0/16',
#     InstanceTenancy = 'default',
#     AmazonProvidedIpv6CidrBlock = False
# )
#
# masterVpc.create_tags(
#     DryRun = False,
#     Tags = [
#         {
#             'Key': 'Name',
#             'Value': 'master'
#         },
#     ]
# )

# # Create ec2 instance eligible for free tier
# ec2.create_instances(
#     # DryRun = True,
#     ImageId = Constants.amiDict['Amazon Linux AMI 2016.09.1 (HVM), SSD Volume Type'],
#     InstanceType = Constants.ec2FreeTierInstance,
#     MinCount = 1,
#     MaxCount = 1
# )
#
# # Get a list of all ec2 instances which are running
# instances = ec2.instances.filter(
#     Filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
# )
#
# ec2Ids = [instance.id for instance in instances]
#
# # Terminate all instances which are running
# ec2.instances.filter(InstanceIds = ec2Ids).terminate()

# Clean Up
###############################################
# Delete all VPCs except for our default
for vpc in ec2.vpcs.filter(
    Filters = [{
        'Name': 'tag:Name',
        'Values': ['master']
    }]
):
    vpc.delete()