# Raspberry GitHub Runner

Welcome to the Raspberry GitHub Runner documentation !

## Overview

Raspberry GitHub Runner is an [Ansible-based](https://docs.ansible.com/) solution that allows you to set up and manage self-hosted GitHub Actions runners on Raspberry Pi devices. This project enables a plug-and-play experience with minimal manual intervention, making it easy to create a fleet of GitHub runners on low-cost hardware.

## Key Features

- **Automated Setup**: Configure runners for multiple repositories with a single playbook
- **Customizable Deployment**: Define labels, repository assignments, and other settings per runner
- **Raspberry Pi Optimized**: Designed specifically for ARM-based Raspberry Pi devices
- **Maintainable Infrastructure**: Manage your runners as code with Ansible

## Documentation Structure

This documentation follows the [Diátaxis](https://diataxis.fr/) framework, organized into four main sections:

- **[Tutorials](./tutorials.md)**: Step-by-step lessons to get you started
- **[How-to Guides](./how-to-guides.md)**: Practical guides for specific tasks
- **[Concepts](./explanation.md)**: Explanations of key concepts and architecture
- **[Reference](./reference.md)**: Technical details and specifications

## Project Structure

This project uses Ansible playbooks to automate the process of:

1. Preparing the environment for each runner
2. Registering multiple runners with different GitHub repositories from a single host
3. Setting up runners as system services that start automatically on boot and recover from failures

## Requirements

- Raspberry Pi hardware (Raspberry 5)
- Ubuntu server 24.04.2 LTS
- Python 3.12
- Ansible

## License

This project is licensed under the [LICENSE](https://github.com/freddo1503/raspberry-github-runner/blob/main/LICENSE) - see the license file for details.