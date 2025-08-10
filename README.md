Project Setup Instructions

Prerequisites

Docker and Docker Compose installed on your system

Access to Cisco DevNet Sandbox

Valid pyATS testbed file configured for your environment

Getting Started

Clone the Repository

git clone [<repository-url>](https://github.com/automateyournetwork/ReACT_AI_Agent_for_Cisco_IOS_XE)
cd ReACT_AI_Agent_for_Cisco_IOS_XE

Start the Application

docker-compose up

Access the Application
Open your browser and visit:

http://localhost:8501

Configuration

Ensure DevNet Sandbox is Active

Confirm that your DevNet sandbox is running and accessible.

Validate Your Testbed File

Check your pyATS testbed file for accuracy and completeness.

pyats validate testbed <path-to-your-testbed-file>

Update the Testbed for Local Device

Modify the testbed file to reflect your local device configurations.

Example snippet:

devices:
  local_device:
    os: iosxe
    type: router
    connections:
      cli:
        protocol: ssh
        ip: 192.168.1.1
        port: 22

Stopping the Application

docker-compose down

Support

For issues, please open an issue in this repository.

