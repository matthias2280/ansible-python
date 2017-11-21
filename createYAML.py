###################################
#
#  Matthias Buchholz
#  2017
#
###################################

import os
import time
import datetime
import sys
import base64
from sys import argv
from shutil import copyfile
from Crypto.Cipher import AES

# Get password
BLOCK_SIZE = 32
if sys.argv[4]:
        passenrypted='put encrypted password here'
        user='username'

PADDING = '{'
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
temp = user + "," + sys.argv[4] + "1234567890123456789012345678901234567890"

secret = temp[:32]
cipher = AES.new(secret)
decoded = DecodeAES(cipher, passenrypted)
#print decoded

# arguments 
varfile = sys.argv[1]
direction = sys.argv[2]
tracefile = sys.argv[3]

# get timestamp for file name
date = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

# state of objects in .yaml
if direction == "add":
	direct = "present"
if direction == "remove":
	direct = "absent"
if direction == "query":
	direct = "query"

# open and create temp.yml
py = open('temp.yml', 'w+')

# Create and read files
TF = open(tracefile, 'a+')

f = open(varfile, 'r')
fread = f.readlines(),

pounds = "\033[1;36m###################################################################################\033[1;37m"

# get default values to pass to defs
for lines in fread:
	# Tenants
        split0 = lines[0].split(",")
	fv0 = split0[0]
	del split0[0]
	# ANP
	split1 = lines[1].split(",")
        fv1 = split1[0]
        del split1[0]
        # BD
	split2 = lines[2].split(",")
        fv2 = split2[0]
        del split2[0]
        # EPG
	split3 = lines[3].split(",")
        fv3 = split3[0]
        del split3[0]
        # Contract
	split4 = lines[4].split(",")
        fv4 = split4[0]
        del split4[0]
        # Filter
	split5 = lines[5].split(",")
        fv5 = split5[0]
        del split5[0]
        # Filter Entry
	split6 = lines[6].split(",")
        fv6 = split6[0]
        del split6[0]
	# Subject
	split7 = lines[7].split(",")
        fv7 = split7[0]
        del split7[0]
	# SUB2FILTER
	split8 = lines[8].split(",")
        fv8 = split8[0]
        del split8[0]
	# Contract to EPG
	split9 = lines[9].split(",")
        fv9 = split9[0]
        del split9[0]
	# L3OUT
	split10 = lines[10].split(",")
        fv10 = split10[0]
	del split10[0]
	

#raise SystemExit

print "\n\n"+pounds+"\n\n  \033[1;33m  TENANTs BUILT:\n"
for UTnt in split0:
	Tnt = UTnt.rstrip('\n')
	print Tnt
print pounds+"\n\n \033[1;33m  ANPs BUILT:"
for UANP in split1:
	ANP = UANP.rstrip('\n')
	print ANP
print pounds+"\n\n \033[1;33m  BDs BUILT:"
for UBD in split2:
	BD = UBD.rstrip('\n')
	print BD
print pounds+"\n\n \033[1;33m  EPGs BUILT:"
for UEPG in split3:
	EPG = UEPG.rstrip('\n')
	print EPG
print pounds+"\n\n \033[1;33m  Contracts BUILT:"
for UCON in split4:
        CON = UCON.rstrip('\n')
        print CON
print pounds+"\n\n \033[1;33m  Filters BUILT:"
for UFIL in split5:
        FIL = UFIL.rstrip('\n')
        print FIL
print pounds+"\n\n \033[1;33m  Filter definitions BUILT:"
for UFIL_E in split6:
        FIL_E = UFIL_E.rstrip('\n')
        print FIL_E
print pounds+"\n\n \033[1;33m  Subjects BUILT:"
for USUB in split7:
        SUB = USUB.rstrip('\n')
        SSUB = SUB.split(':')
	print SUB
print pounds+"\n\n \033[1;33m  Subjects bound to Filters:"
for USUBFILB in split8:
	SUBFILB = USUBFILB.rstrip('\n')
	SSUBFILB = SUBFILB.split(':')
	print SUBFILB
print pounds+"\n\n \033[1;33m  Contracts bound to EPGs:"
for UCON2EPG in split9:
        CON2EPG = UCON2EPG.rstrip('\n')
        SSCON2EPG = CON2EPG.split(':')
	print CON2EPG
print pounds+"\n\n \033[1;33m  L3_out bound to all EPGs:"
for UL3_BD in split10:
        L3_BD = UL3_BD.rstrip('\n')
        print L3_BD
	print pounds+"\n\n\033[1;37m"

#print SUBFILB
#print CON2EPG
#exit()

domain = "vCenter"
domtype = "vmm"
vmprov = "vmware"


# write tmp.yml header
py.write(
	"- hosts: 10.7.132.10\n"
	"  connection: local\n"
        "  gather_facts: no\n\n"
        "  tasks:\n"
	)

#Begin Tracefile
TF.write("\n"+(date).rstrip('\n')+","+direct+",")

def MK_Tenant():
	for DU_Tenant in split0:
		Tenant = DU_Tenant.rstrip('\n')
		py.write(
                "  - name: add an Tenant\n"
                "    aci_tenant:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tenant+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
		TF.write((Tenant).rstrip('\n')+":")
	TF.write(",")

def MK_ANP():
	for DU_ANP in split1:
		ANP = DU_ANP.rstrip('\n')
		py.write(
                "  - name: add an ANP\n"
                "    aci_ap:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      ap: "+ANP+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
		TF.write((ANP).rstrip('\n')+":")
	TF.write(",")

def MK_BD():
        for DU_BD in split2:
		BD = DU_BD.strip('\n')
		py.write(
                "  - name: add an BD\n"
                "    aci_bd:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      bd: "+BD+"\n"
		"      arp_flooding: true\n"
		"      enable_routing: true\n"
		"      limit_ip_learn: false\n"                 
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
		MK_L3_BD(BD)
		TF.write((BD).rstrip('\n')+":")
	TF.write(",")

def MK_EPG():
	for DU_EPG in split3:
		EPG = DU_EPG.rstrip('\n')
                py.write(
		"  - name: add an EPG\n"
                "    aci_epg:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      ap: "+ANP+"\n"
                "      bd: "+BD+"\n"
                "      epg: "+EPG+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
		DOM_EPG(EPG)
		TF.write((EPG).rstrip('\n')+":")
	TF.write (",")

def DOM_EPG(EPG):
	py.write(
        "  - name: add an Domain to EPG\n"
        "    aci_epg_to_domain:\n"
        "      hostname: 10.7.132.10\n"
        "      username: username\n"
        "      password: "+decoded+"\n"
        "      tenant: "+Tnt+"\n"
        "      ap: "+ANP+"\n"
        "      epg: "+EPG+"\n"
	"      domain: "+domain+"\n"
	"      domain_type: "+domtype+"\n"
	"      vm_provider: "+vmprov+"\n"
        "      state: "+direct+"\n"
        "      validate_certs: no\n"
        )

def MK_FIL():
        for DU_FIL in split5:
                FIL = DU_FIL.rstrip('\n')
                py.write(
                "  - name: add a filter\n"
                "    aci_filter:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      filter: "+FIL+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((FIL).rstrip('\n')+":")
        TF.write (",")
def MK_FIL_E():
        for DU_FIL_E in split6:
                FIL_E = DU_FIL_E.rstrip('\n')
                py.write(
                "  - name: add filter entry\n"
                "    aci_filter_entry:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      ether_type: ip\n"
                "      ip_protocol: icmp\n"
                "      filter: "+FIL+"\n"
                "      entry: "+FIL_E+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((FIL_E).rstrip('\n')+":")
        TF.write (",")
def MK_CON():
        for DU_CON in split4:
                CON = DU_CON.rstrip('\n')
                py.write(
                "  - name: add a contract\n"
                "    aci_contract:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      contract: "+CON+"\n"
                "      scope: tenant\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((CON).rstrip('\n')+":")
        TF.write (",")
def MK_SUB():
        for DU_SUB in split7:
                LSUB = DU_SUB.rstrip('\n')
                SUB = LSUB.split(':')
		py.write(
                "  - name: add a subject\n"
                "    aci_contract_subject:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      contract: "+SUB[0]+"\n"
                "      subject: "+SUB[1]+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((SUB[0]).rstrip('\n')+";"+(SUB[1]).rstrip('\n'))
        TF.write (",")
def MK_SUBFILB():
        for DU_SUBFILB in split8:
		SUBFILB = DU_SUBFILB.rstrip('\n')
		SSUBFILB = SUBFILB.split(':')
                py.write(
                "  - name: aci subject filter binding\n"
                "    aci_contract_subject_to_filter:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      contract: "+SSUBFILB[0]+"\n"
                "      subject: "+SSUBFILB[1]+"\n"
                "      filter: "+SSUBFILB[2]+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((SUBFILB).rstrip('\n')+":")
        TF.write (",")
def MK_CON2EPG():
        for DU_CON2EPG in split9:
                SCON2EPG = DU_CON2EPG.rstrip('\n')
                CON2EPG = SCON2EPG.split(':')
                py.write(
                "  - name: add contract to EPG\n"
                "    aci_epg_to_contract:\n"
                "      hostname: 10.7.132.10\n"
                "      username: username\n"
                "      password: "+decoded+"\n"
                "      tenant: "+Tnt+"\n"
                "      ap: "+ANP+"\n"
                "      epg: "+CON2EPG[0]+"\n"
                "      contract: "+CON2EPG[1]+"\n"
                "      contract_type: "+CON2EPG[2]+"\n"
                "      state: "+direct+"\n"
                "      validate_certs: no\n"
                )
                TF.write((CON2EPG[0].rstrip('\n'))+";"+(CON2EPG[1].rstrip('\n'))+";"+(CON2EPG[2].rstrip('\n'))+":")
        TF.write (",")
def MK_L3_BD(BD):
#	global L3_BD
	py.write(
        "  - name: Add L3Out to BD\n"
	"    aci_bd_to_l3out:\n"
        "      hostname: 10.7.132.10\n"
        "      username: username\n"
        "      password: "+decoded+"\n"
        "      tenant: "+Tnt+"\n"
        "      bd: "+BD+"\n"
        "      state: "+direct+"\n"
        "      l3out: "+split10[0].rstrip("\n")+"\n"
        "      validate_certs: no\n"
        )
        TF.write((SUBFILB).rstrip('\n')+":")
TF.write (",")



# create the temp.yml file
if direct == "present": 
	if Tnt:
		MK_Tenant()
	if ANP:
		MK_ANP()
	if BD:
		MK_BD()
	if EPG:
		MK_EPG()
	if CON:
		MK_CON()
	if FIL:
		MK_FIL()
	if FIL_E:
		MK_FIL_E()
	if SUB:
		MK_SUB()
	if SUBFILB:
		MK_SUBFILB()
	if CON2EPG:
		MK_CON2EPG()
	TF.write (":/n")

else:
	if CON2EPG:
		MK_CON2EPG()
	if SUBFILB:
		MK_SUBFILB()
	if SUB:
		MK_SUB()
	if FIL_E:
		MK_FIL_E()
	if FIL:
		MK_FIL()
	if CON:
		MK_CON()
	if EPG:
		MK_EPG()
	if BD:
		MK_BD()
	if ANP:
		MK_ANP()
	if Tnt:
		MK_Tenant()
	TF.write (":/n")


# close files
py.close()
f.close() 
TF.close()

# rename temp playbook to date and move to TRACE directory
copyfile('temp.yml',date)
path = "/home/matthias/ansible/ROLLBACK/"+date
os.makedirs(path, 0755)
copyfile(date, "/home/matthias/ansible/ROLLBACK/"+date+"/"+date+".yml")
copyfile(sys.argv[1], "/home/matthias/ansible/ROLLBACK/"+date+"/VARIABLES")

# run the ansible playbook
os.system("ansible-playbook "+date)

# cleanup files
os.remove(date)
os.remove("temp.yml")

