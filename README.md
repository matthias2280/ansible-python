# ansible-python

This is my attempt to automate a the deployment of a three-tier application in ACI.

I've taken a different approach than normal as I am using Python to create a playbook.yml file which is then executed and stored for recordkeeping. sys.args are passed when the python script is ran which sets the State of the info passed in the modules (add or remove)

I'm told that this approach is a bit odd but manipulating data in python is easier for me than malipulating variables in files in directories in Ansible.

The syntax is:
