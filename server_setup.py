#!/usr/bin/env python3
import subprocess
import os
import sys
import getpass
from datetime import datetime

def print_welcome_message():
    """Display a welcome message with script information"""
    print("""
╔════════════════════════════════════════════╗
║     Linux Server Setup & Security Script    ║
║            Version 1.0 (2024)              ║
╚════════════════════════════════════════════╝

This script will help you set up and secure your Linux server by:
• Updating system packages
• Installing essential tools
• Configuring firewall rules
• Setting up intrusion prevention
• Creating configuration backups
• Applying security hardening

Please make sure you have root/sudo access before proceeding.
""")

def run_command(command):
    """Execute a shell command and return the output"""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        return None

def setup_server():
    # Display welcome message
    print_welcome_message()
    
    # Check if script is run as root
    if os.geteuid() != 0:
        print("This script must be run as root (sudo)!")
        sys.exit(1)

    print("Starting server setup...")
    
    # Update package list and upgrade all packages
    print("\n1. Updating and upgrading packages...")
    run_command("apt update")
    run_command("apt upgrade -y")

    # Install essential packages
    print("\n2. Installing essential packages...")
    essential_packages = [
        "ufw",          # Firewall
        "fail2ban",     # Intrusion prevention
        "vim",          # Text editor
        "htop",         # System monitor
        "tmux",         # Terminal multiplexer
        "git",          # Version control
        "curl",         # Data transfer tool
        "unzip"         # Archive utility
    ]
    run_command(f"apt install -y {' '.join(essential_packages)}")

    # Configure firewall
    print("\n3. Configuring firewall...")
    run_command("ufw default deny incoming")
    run_command("ufw default allow outgoing")
    run_command("ufw allow ssh")
    run_command("ufw allow 80/tcp")  # HTTP
    run_command("ufw allow 443/tcp") # HTTPS
    run_command("ufw --force enable")

    # Configure fail2ban
    print("\n4. Configuring fail2ban...")
    run_command("systemctl enable fail2ban")
    run_command("systemctl start fail2ban")

    # Create a backup of important configuration files
    print("\n5. Creating backup directory for configurations...")
    backup_dir = f"/root/config_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_command(f"mkdir -p {backup_dir}")
    run_command(f"cp /etc/ssh/sshd_config {backup_dir}/")
    run_command(f"cp /etc/passwd {backup_dir}/")
    run_command(f"cp /etc/group {backup_dir}/")

    # Basic security configurations
    print("\n6. Applying basic security configurations...")
    # Disable root SSH login
    run_command("sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")
    # Restart SSH service
    run_command("systemctl restart sshd")

    print("\nServer setup completed!")
    print(f"Configuration backups stored in: {backup_dir}")
    print("\nRemaining recommended actions:")
    print("1. Create a new non-root user if not already done")
    print("2. Configure SSH key-based authentication")
    print("3. Update SSH port if desired")
    print("4. Configure timezone: dpkg-reconfigure tzdata")
    print("5. Configure automatic security updates")

if __name__ == "__main__":
    setup_server()