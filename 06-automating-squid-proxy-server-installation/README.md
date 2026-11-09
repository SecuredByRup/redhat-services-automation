# Lab 6: Automating Squid Proxy Server Installation & Configuration

[![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![Squid Proxy](https://img.shields.io/badge/Squid_Proxy-F05032?style=for-the-badge&logo=squid&logoColor=white)](http://www.squid-cache.org/)
[![RHEL/CentOS](https://img.shields.io/badge/RHEL%2FCentOS-CC0000?style=for-the-badge&logo=red-hat&logoColor=white)](https://www.redhat.com/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

---

## 📖 Overview
This repository contains automated Infrastructure as Code (IaC) scripts and playbooks for **Lab 6: Automating Squid Proxy Server Installation**. Using **Ansible**, this project automates the end-to-end deployment, configuration, secure templating, access control list (ACL) enforcement, and functional validation of a production-grade **Squid Proxy Server** running locally on CentOS/RHEL 8.

---

## 📂 Project Directory Structure
All configuration files, playbooks, inventories, and templates are structured modularly within the local working directory:

```text
scripts/
├── inventory/
│   └── hosts.yml
├── playbooks/
│   ├── install-squid.yml
│   ├── configure-squid.yml
│   ├── test-squid.yml
│   ├── client-test.yml
│   └── monitor-squid.yml
├── templates/
│   ├── squid.conf.j2
│   └── blocked_domains.j2
└── vars/
```

---

## 🚀 Execution Guide & Workflow

### 1. Local Inventory Setup (`inventory/hosts.yml`)
Configured for local container/VM execution (`localhost`, `ansible_connection: local`):
```yaml
all:
  children:
    proxy_servers:
      hosts:
        localhost:
          ansible_connection: local
          ansible_python_interpreter: "{{ ansible_playbook_python }}"
```

### 2. Running the Automation Playbooks
* **Install Squid Proxy Server:**
  ```bash
  ansible-playbook -i inventory/hosts.yml playbooks/install-squid.yml -K
  ```
* **Deploy Advanced Configuration & Jinja2 Templates:**
  ```bash
  ansible-playbook -i inventory/hosts.yml playbooks/configure-squid.yml -K
  ```
* **Execute Server-Side and Client-Side Testing:**
  ```bash
  ansible-playbook -i inventory/hosts.yml playbooks/test-squid.yml -K
  ansible-playbook -i inventory/hosts.yml playbooks/client-test.yml
  ```
* **Run Proxy Performance Monitoring:**
  ```bash
  ansible-playbook -i inventory/hosts.yml playbooks/monitor-squid.yml -K
  ```

---

## 📸 Lab Execution & Validation Screenshots

### 1. Project Directory Structure & Ansible Version
* **Description:** Verifying the local workspace hierarchy and Ansible runtime environment.
* ![Project Structure and Ansible Version](assets/01-project-structure-and-ansible-version.png)

### 2. Squid Installation Playbook Execution
* **Description:** Successful execution of `install-squid.yml` showing clean task execution and `failed=0` play recap.
* ![Squid Installation Playbook Recap](assets/02-squid-installation-playbook-recap.png)

### 3. Advanced Configuration Playbook Deployment
* **Description:** Deploying Jinja2 templates (`squid.conf.j2`, `blocked_domains.j2`), validating syntax, and triggering service handlers.
* ![Advanced Configuration Execution](assets/03-advanced-configuration-playbook-execution.png)

### 4. Proxy Testing & Validation Playbook
* **Description:** Running server-side validation tasks (`test-squid.yml`) confirming port `3128` listening state and cache/access log recording.
* ![Proxy Testing Playbook Execution](assets/04-proxy-testing-playbook-execution.png)

### 5. Manual Curl Testing & Blocked Domain Verification
* **Description:** Testing proxy routing via `curl -x 127.0.0.1:3128`, confirming successful traffic fetch on allowed sites and security enforcement on restricted domains.
* ![Manual Curl Testing and Blocked Domains](assets/05-manual-curl-testing-and-blocked-domains.png)

---

## 🎯 Conclusion
This project successfully demonstrated the implementation of Infrastructure as Code (IaC) principles for enterprise network services. By leveraging **Ansible automation** and **Jinja2 dynamic templating**, the deployment of the **Squid Proxy Server** was streamlined into repeatable, error-free execution workflows. The established configuration successfully enforces strict access control lists (ACLs), caches web content for performance optimization, and secures network gateways against unauthorized domain requests.