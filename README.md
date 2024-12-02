# Linux Server Setup Script

This Python script automates the initial setup and security configuration of a new Linux server. It performs essential tasks such as system updates, package installation, firewall configuration, and basic security hardening.

## Features

- System updates and package upgrades
- Installation of essential tools and utilities
- UFW firewall configuration with common rules
- Fail2ban setup for intrusion prevention
- Backup of important configuration files
- Basic security configurations
- Detailed output and error handling

## Prerequisites

- A fresh Linux server (tested on Ubuntu/Debian)
- Python 3.x
- Root/sudo access

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Apc204/linux-server-setup.git
   cd linux-server-setup
   ```

2. Make the script executable:
   ```bash
   chmod +x server_setup.py
   ```

## Usage

Run the script with sudo:
```bash
sudo ./server_setup.py
```

The script will:
1. Update and upgrade all system packages
2. Install essential tools
3. Configure the firewall
4. Set up fail2ban
5. Create configuration backups
6. Apply basic security settings

## Post-Setup Actions

After running the script, consider these additional security measures:

1. Create a new non-root user
2. Configure SSH key-based authentication
3. Update the SSH port
4. Configure the timezone
5. Set up automatic security updates

## Security Note

This script provides basic server setup and security configurations. Depending on your specific needs, you may want to implement additional security measures.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.