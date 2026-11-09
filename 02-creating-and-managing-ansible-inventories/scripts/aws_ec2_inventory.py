#!/usr/bin/env python3

import boto3
import json
import sys

def get_ec2_inventory():
    """
    Generate dynamic inventory from AWS EC2 instances (with mock fallback for training labs)
    """
    inventory = {
        '_meta': {
            'hostvars': {}
        }
    }
    
    # Try fetching live EC2 instances
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] != 'running':
                    continue
                    
                instance_id = instance['InstanceId']
                private_ip = instance.get('PrivateIpAddress', '')
                public_ip = instance.get('PublicIpAddress', '')
                
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                instance_name = tags.get('Name', instance_id)
                
                inventory['_meta']['hostvars'][instance_name] = {
                    'ansible_host': public_ip or private_ip,
                    'ec2_instance_id': instance_id,
                    'ec2_instance_type': instance['InstanceType'],
                    'ec2_private_ip': private_ip,
                    'ec2_public_ip': public_ip,
                    'ec2_state': instance['State']['Name'],
                    'ec2_tags': tags
                }
                
                for key, value in tags.items():
                    group_name = f"{key}_{value}".replace(' ', '_').replace('-', '_').lower()
                    if group_name not in inventory:
                        inventory[group_name] = {'hosts': []}
                    inventory[group_name]['hosts'].append(instance_name)
                
                instance_type_group = f"type_{instance['InstanceType'].replace('.', '_')}"
                if instance_type_group not in inventory:
                    inventory[instance_type_group] = {'hosts': []}
                instance_type_group['hosts'].append(instance_name)
                
        return inventory

    except Exception as e:
        # Fallback to mock inventory for training/testing environments
        mock_inventory = {
            "_meta": {
                "hostvars": {
                    "aws_web_01": {
                        "ansible_host": "127.0.0.1",
                        "ansible_connection": "local",
                        "ec2_instance_id": "i-0123456789abcdef0",
                        "ec2_instance_type": "t2.micro",
                        "ec2_state": "running",
                        "ec2_tags": {"Environment": "production", "Application": "web"}
                    },
                    "aws_db_01": {
                        "ansible_host": "127.0.0.1",
                        "ansible_connection": "local",
                        "ec2_instance_id": "i-0987654321fedcba0",
                        "ec2_instance_type": "t2.small",
                        "ec2_state": "running",
                        "ec2_tags": {"Environment": "production", "Application": "database"}
                    }
                }
            },
            "environment_production": {
                "hosts": ["aws_web_01", "aws_db_01"]
            },
            "application_web": {
                "hosts": ["aws_web_01"]
            },
            "application_database": {
                "hosts": ["aws_db_01"]
            },
            "type_t2_micro": {
                "hosts": ["aws_web_01"]
            },
            "type_t2_small": {
                "hosts": ["aws_db_01"]
            }
        }
        return mock_inventory

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        inventory = get_ec2_inventory()
        print(json.dumps(inventory, indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps({}))
    else:
        print("Usage: aws_ec2_inventory.py --list")
        print("       aws_ec2_inventory.py --host <hostname>")
        sys.exit(1)
