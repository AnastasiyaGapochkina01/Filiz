#!/usr/bin/env python3
"""
Script for AWS EC2: list, stop and start instances
"""
import argparse
import boto3
import sys


parser = argparse.ArgumentParser(description="AWS EC2 actions")
parser.add_argument("--action", type=str, help="start or stop instance by name")
parser.add_argument("--list", action='store_true', help="List all instances")
parser.add_argument("--host", type=str, help="Target instance name")
parser.add_argument("--get-ip", action='store_true', help="Get public IP address of the host")

args = parser.parse_args()

ec2 = boto3.client("ec2")


if args.list:
    try:
        response = ec2.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                name_tag = next((tag["Value"] for tag in instance.get("Tags", []) if tag["Key"] == "Name"), "N/A")
                state = instance["State"]["Name"]
                print(f"NAME: {name_tag} STATE - {state}")
    except Exception as e:
        print(f"Error listing instances: {e}")
        sys.exit(1)


if args.host:
    try:
        response = ec2.describe_instances(
            Filters=[
                {"Name": "tag:Name", "Values": [args.host]}
            ]
        )

        instances = [
            i for r in response["Reservations"] for i in r["Instances"]
        ]

        if not instances:
            print(f"Instance '{args.host}' not found")
            sys.exit(1)

        instance = instances[0]
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]

        if args.get_ip:
            public_ip = instance.get("PublicIpAddress")
            if public_ip:
                print(public_ip)
            else:
                print(f"Instance '{args.host}' has no public IP")
            sys.exit(0)

        if args.action == "start":
            if state == "running":
                print(f"Instance '{args.host}' is already running")
            else:
                ec2.start_instances(InstanceIds=[instance_id])
                print(f"Instance '{args.host}' starting...")

        elif args.action == "stop":
            if state == "stopped":
                print(f"Instance '{args.host}' is already stopped")
            else:
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"Instance '{args.host}' stopping...")
        else:
            print(f"Unknown action: {args.action}")

    except Exception as e:
        print(f"Error with instance '{args.host}': {e}")
        sys.exit(1)
