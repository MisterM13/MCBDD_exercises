#!/bin/bash
from chembl_webresource_client.new_client import new_client
import json

molecule = new_client.molecule
approved_drugs = molecule.filter(max_phase=4).order_by('first_approval').order_by('pref_name')#.only(['first_approval', 'pref_name'])
print(type(approved_drugs))
print(len(approved_drugs))
#print(approved_drugs)

res = approved_drugs.filter(first_approval__gte=2012)
#print(res)
target = new_client.target
targets = target.filter(pref_name__iexact=res.only(['pref_name']))
#print(type(targets))
#print(len(targets))
#print(targets)