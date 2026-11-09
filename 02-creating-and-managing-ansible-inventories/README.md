# Lab 2: Creating and Managing Ansible Inventories

## Overview

This laboratory explores the design, configuration, and validation of static, dynamic, and hybrid inventory structures in Ansible. It covers advanced INI and YAML inventory formats, custom dynamic AWS EC2 Python scripting with mock fallback mechanisms, built-in cloud inventory plugins, automated validation playbooks, debugging scripts, and large-scale performance benchmarking.

## Environment Specifications

* **Operating System:** CentOS Stream 9

* **Automation Engine:** Ansible Core 2.14.18

* **Runtime Language:** Python 3.9 with `boto3` and `botocore` libraries

* **Cloud Integration:** `amazon.aws:12.1.0` collection

## Lab Architecture & Tasks

### Task 1: Static Inventories (INI & YAML)

* Created standard INI inventories (`basic_inventory.ini`) and production-grade hierarchical INI files (`production_inventory.ini`) featuring grouped infrastructure (webservers, databases, loadbalancers, monitoring).

* Configured equivalent multi-tier hierarchical structures in YAML format (`inventory.yml`).

### Task 2: Dynamic & Hybrid Inventories

* **Custom Python Script (`aws_ec2_inventory.py`):** Developed a dynamic inventory script adhering to Ansible's `--list` and `--host` protocol, enhanced with robust mock data fallback logic to ensure seamless offline training and testing.

* **Built-in Cloud Plugin (`aws_ec2.aws_ec2.yml`):** Configured the native `amazon.aws.aws_ec2` inventory plugin utilizing region filtering, keyed tag groups, and host variable composition.

* **Hybrid Layout (`inventories/production/static_hosts.ini`):** Structured directory-based hybrid sources merging local on-premises nodes with cloud metadata.

### Task 3: Testing, Validation & Performance

* Executed ad-hoc connectivity commands (`ansible all -m ping`) and system fact-gathering routines (`setup`).

* **Validation Playbook (`validate_inventory.yml`):** Programmed automated assertions verifying host variables, group memberships, and SSH/local transport reachability.

* **Debugging Automation (`debug_inventory.sh`):** Built a shell-based audit tool to inspect inventory graphs, host variables, and connectivity.

* **Performance Benchmarking (`generate_large_inventory.py`):** Generated large-scale inventories (500+ nodes) and benchmarked parsing efficiency across formats using the `time` utility.

## Visual Documentation & Execution Screenshots

### 1. Production Inventory YAML & Graph Structure


*Execution of `ansible-inventory -i production_inventory.ini --list --yaml` and `--graph` displaying clean hierarchical parent-child group mappings.*

### 2. Custom Dynamic AWS EC2 Script Output



*Successful execution and JSON output generation of the custom dynamic AWS EC2 inventory script with mock fallback data.*

### 3. Hybrid Static Inventory Parsing


*Verifying directory contents and parsing the hybrid static inventory source file `inventories/production/static_hosts.ini`.*

### 4. Validation Playbook Execution & Results



*Running `validate_inventory.yml` across local target nodes, displaying successful play recaps and initiating the custom `./debug_inventory.sh` auditing script.*

### 5. Debug Script & Large-Scale Benchmarking


*Completion of the inventory debug connectivity report followed by performance benchmarking (`time`) parsing a 500-node generated large inventory file (`large_inventory.ini`).*

## Conclusion

Lab 2 successfully demonstrated how to architect scalable, flexible inventory systems in Ansible. By combining static INI/YAML configurations, custom and native dynamic cloud inventory sources, automated validation playbooks, and performance benchmarking tools, this project establishes a robust foundation for managing complex, multi-tier enterprise environments.