import requests

########## GENERAL VARIABLE

id = ("2fv5")       #CHANGE THIS TO GET THE DIFFERENT RESULTS IN EACH PART

####### PART 1

#First we place a variable to set the ID and we call the API

r = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)

#Next, we get the Json and we save it in a variable (dictionary), then we find our data using "get"

dict_json = r.json()
container_identifiers = dict_json.get("rcsb_entry_container_identifiers")
non_polymer_ids = (container_identifiers.get("non_polymer_entity_ids"))

#for n in non_polymer_ids:
    #print(n)       #OUTPUT 1

####### PART 2

#For this part we need the polymer entries we got in PART 1, so we can get them again

r = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)
dict_json = r.json()
container_identifiers = dict_json.get("rcsb_entry_container_identifiers")
non_polymer_ids = (container_identifiers.get("non_polymer_entity_ids"))

#Now, with the IDs of the non_polymers, we retrive info from the entity service

for entityID in non_polymer_ids:
    r2 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    #print(r2.json())        #OUTPUT 2

####### PART 3

#First we get the data from PART2 again since we need it

r = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)
dict_json = r.json()
container_identifiers = dict_json.get("rcsb_entry_container_identifiers")
non_polymer_ids = (container_identifiers.get("non_polymer_entity_ids"))

#With the data we get from PART 2, we retrieve the info we want, in this case, the comp_id

list_comp_id = []

for entityID in non_polymer_ids:
    r3 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    dict2_json = r3.json()
    container_comp = dict2_json.get("pdbx_entity_nonpoly")
    comp_id = container_comp.get("comp_id")
    list_comp_id.append(comp_id)

list_comp_id.sort()

for c in list_comp_id:
    #print(c)         #OUTPUT 3
    pass

####### PART 4

#First we get the data from PART3 again since we need part of it and the OUTPUT LIST will be useful

r = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)
dict_json = r.json()
container_identifiers = dict_json.get("rcsb_entry_container_identifiers")
non_polymer_ids = (container_identifiers.get("non_polymer_entity_ids"))

list_comp_id = []

for entityID in non_polymer_ids:
    r3 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    dict2_json = r3.json()
    container_comp = dict2_json.get("pdbx_entity_nonpoly")
    comp_id = container_comp.get("comp_id")
    list_comp_id.append(comp_id)

list_comp_id.sort()  #This sorted list will be useful to access the info on the dictionary with the names

# With the data we need to get the WHOLE NAMES, we retrieve the info we want, in this case, the comp_id

dict_comp_id = {}

for entityID in non_polymer_ids:
    r3 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    dict2_json = r3.json()
    container_comp = dict2_json.get("pdbx_entity_nonpoly")
    comp_id = container_comp.get("comp_id")
    name = container_comp.get("name")
    dict_comp_id[comp_id] = name

for c in list_comp_id:
    #print(str(c) + " " + str(dict_comp_id[c]))  # OUTPUT 4
    pass

####### PART 5

# In this part we need to find the binding affinity field. That is located in the ENTRY place, so we need to find and check info from 2 places

r4 = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)
dict3_json = r4.json()
binding_aff = dict3_json.get("rcsb_binding_affinity")

dict_comp_id2 = {}

for entityID in non_polymer_ids:
    r3 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    dict2_json = r3.json()
    container_comp = dict2_json.get("pdbx_entity_nonpoly")
    comp_id = container_comp.get("comp_id")
    name = container_comp.get("name")
    dict_comp_id2[comp_id] = name

dict_affinity_values = {}
counter = 0
list_provenance_codes = []
list_of_keys_used = []

for name in list_comp_id:
    #print(str(name) + " " + str(dict_comp_id2[name]))     # OUTPUT 5
    for dicti in binding_aff:
        if dicti["comp_id"] == name:
            dict_affinity_values[counter] = [str(dicti["comp_id"]), float(dicti["value"]), str(dicti["unit"]), str(dicti["provenance_code"])]
            counter += 1
    for key in dict_affinity_values.keys():
        list_provenance_codes.append(dict_affinity_values[key][3])
    list_provenance_codes.sort()
    for val in list_provenance_codes:
        for key in dict_affinity_values:
            if key not in list_of_keys_used:
                if dict_affinity_values[key][3] == val:
                    #print(str(dict_affinity_values[key][0]) + ": " + str(dict_affinity_values[key][1]) + " " + str(dict_affinity_values[key][2]) + " " + str(dict_affinity_values[key][3]))                # OUTPUT 5         # You can make this output look better rather than "a list" but that is just a tiny detail
                    list_of_keys_used.append(key)
    counter = 0
    ordered_list = []
    dict_affinity_values = {}

####### PART 6

# In this part we need to find the binding affinity field. That is located in the ENTRY place, so we need to find and check info from 2 places. It is similar (almost the same) to PART5, but we need to place the info in a specific way

r4 = requests.get('https://data.rcsb.org/rest/v1/core/entry/' + id)
dict3_json = r4.json()
binding_aff = dict3_json.get("rcsb_binding_affinity")

dict_comp_id2 = {}

for entityID in non_polymer_ids:
    r3 = requests.get("https://data.rcsb.org/rest/v1/core/nonpolymer_entity/" + id + "/" + str(entityID))
    dict2_json = r3.json()
    container_comp = dict2_json.get("pdbx_entity_nonpoly")
    comp_id = container_comp.get("comp_id")
    name = container_comp.get("name")
    dict_comp_id2[comp_id] = name

dict_affinity_values = {}
counter = 0
list_values = []
list_of_keys_used = []

for name in list_comp_id:
    #print(str(name) + " " + str(dict_comp_id2[name]))    # OUTPUT 6
    for dicti in binding_aff:
        if dicti["comp_id"] == name:
            dict_affinity_values[counter] = [str(dicti["type"]), round((float(dicti["value"])), 2), str(dicti["unit"]), str(dicti["provenance_code"])]
            counter += 1
    for key in dict_affinity_values.keys():
        list_values.append(dict_affinity_values[key][1])
    list_values.sort()
    for number in list_values:
        for key in dict_affinity_values:
            if key not in list_of_keys_used:
                if dict_affinity_values[key][1] == number:
                    print(str(dict_affinity_values[key][0]) + ": " + str(dict_affinity_values[key][1]) + " " + str(dict_affinity_values[key][2]) + " " + str(dict_affinity_values[key][3]))                # OUTPUT 6         # You can make this output look better rather than "a list" but that is just a tiny detail
                    list_of_keys_used.append(key)
    counter = 0
    ordered_list = []
    dict_affinity_values = {}
