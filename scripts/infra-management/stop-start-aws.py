import argparse
import boto3

def manage_instances(action, instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    if action == 'start':
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}")
    elif action == 'stop':
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}")
    elif action == 'info':
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        print("Instance info:")
        print(f"ID: {instance['InstanceId']}\nType: {instance['InstanceType']}\nState: {instance['State']['Name']}")
    else:
        print("Unknown action")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'stop', 'info'], help='Action to do')
    parser.add_argument('instance_id', help='ID ec2 instance')
    parser.add_argument('region', default='us-east-1', help='Region to action')
    args = parser.parse_args()
    manage_instances(args.action, args.instance_id, args.region)
