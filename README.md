# ansible-python

This is my attempt to automate the deployment of a three-tier application in ACI.

I've taken a different approach than normal as I am using Python to create a playbook.yml file which is then executed and stored for recordkeeping. 

sys.args are passed when the python script is ran which sets POST or DELETE in module action.  VARIABLE file stores info for Tenant, ANP, BD, etc and is parsed to write ansible modules into the playbook.  The last argument is the "Seed" for the decryption of your password thats passed when the playbook executes

I'm told that this approach is a bit odd but manipulating data in python is easier for me than malipulating variables in files in directories in Ansible.

The syntax is:
python createYAML.py [variables] [direction] [tracefile] [seed for encrypt pword]
