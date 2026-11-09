# Automating Apache HTTP Server Installation with Ansible

![Ansible](https://img.shields.io/badge/Ansible-E00A00?style=for-the-badge&logo=ansible&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=Apache&logoColor=white)
![Red Hat Enterprise Linux](https://img.shields.io/badge/RHEL/CentOS_8-EE0000?style=for-the-badge&logo=red-hat&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📌 Executive Summary

This project demonstrates an automated deployment and configuration pipeline for the **Apache HTTP Server (`httpd`)** across Linux environments using **Ansible**. 

The repository provides end-to-end automation for:
- Standardized package installation (`httpd`, `httpd-tools`, `mod_ssl`) and firewall service rules (`http`, `https`).
- Multi-site Virtual Host configuration driven by Ansible inventory variables and Jinja2 templates (`vhost.conf.j2`).
- Custom global error handling for HTTP `404` (Not Found) and `500` (Internal Server Error) status codes using dedicated Jinja2 templates.
- Automated validation and reporting using Ansible's `uri`, `wait_for`, and `systemd` modules to verify web service health and generate an HTML test report (`test-report.html`).

---

## 🛠 Project Structure

All automation code, playbooks, templates, and inventory configurations are structured inside the repository under `scripts/`:

```text
scripts/
├── inventory/
│   └── hosts.yml
├── playbooks/
│   ├── apache-install.yml
│   ├── configure-vhosts.yml
│   └── test-apache.yml
├── templates/
│   ├── vhost.conf.j2
│   ├── test-report.html.j2
│   └── error-pages/
│       ├── 404.html.j2
│       └── 500.html.j2
└── vars/
    └── vhosts.yml
```

---

## ⚙️ Configuration & Execution Workflow

### 1. Inventory & Directory Setup
Verify Ansible installation and inspect the project structure:
```bash
ansible --version
find . -maxdepth 3
```

![Project Structure and Ansible Check](assets/01-project-structure-and-ansible-version.png)

### 2. Base Apache Installation Playbook
Execute `playbooks/apache-install.yml` to install HTTPD, start and enable the systemd service, configure standard HTTP/HTTPS firewall rules, and deploy a basic index landing page:

```bash
ansible-playbook -i inventory/hosts.yml playbooks/apache-install.yml -K
```

![Base Apache Installation Playbook Execution](assets/02-installation-and-test-playbook-recap.png)

### 3. Automated Validation and Health Check Playbook
Execute `playbooks/test-apache.yml` to run continuous integration tests against the deployment. The playbook checks:
- Service status (`active`/`running`) via `systemd`.
- Port 80 availability via `wait_for`.
- Default site & Virtual Host headers via `uri`.
- Custom 404 error routing via `uri`.
- Apache configuration syntax validation (`httpd -t`).
- Automated HTML test report compilation.

```bash
ansible-playbook -i inventory/hosts.yml playbooks/test-apache.yml -K
```

![Test Playbook Execution and Play Recap](assets/03-test-playbook-recap-and-404-curl.png)

---

## 🧪 Validation & Verification

### Custom 404 Error Page Verification
Requesting a non-existent endpoint confirms that Apache serves our custom template (`/error-pages/404.html`) rather than a generic server page:

```bash
curl -s http://localhost/nonexistent-page
```

![Custom 404 Error Page Curl Verification](assets/04-custom-404-and-test-report-curl.png)

### Generated HTML Test Report Verification
Verify that the automated test playbook successfully compiled the `test-report.html` file in `/var/www/html/`:

```bash
curl -s http://localhost/test-report.html | head -n 30
```

![Generated HTML Test Report Output](assets/05-test-report-verification-curl.png)

---

## 🎯 Conclusion

Through this automation project, manual steps required for deploying web server infrastructure were converted into declarative, repeatable Ansible code. 

Key takeaways:
1. **Infrastructure as Code (IaC):** Standardized web server deployment, eliminating configuration drift across instances.
2. **Dynamic Templating:** Leveraged Jinja2 templates (`.j2`) and Ansible variables to generate scalable Virtual Host configurations and uniform error pages.
3. **Automated Testing & Observability:** Implemented automated post-deployment validation and dynamic HTML test reporting directly into the deployment workflow.