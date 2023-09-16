import json
# https://www.genenames.org/data/genegroup/#!/group/639
file = open('mitochondrial oxfos subunit.json').read()

jsonFile = json.loads(file)

for protein in jsonFile:

    #print(protein)
    groupID = protein['groupID']
    groupName = protein['groupName']
    approvedSymbol = protein['approvedSymbol']
    approvedName = protein['approvedName']
    hgncID = protein['hgncID']
    print(str(groupID) + "\t" +  str(groupName) + "\t" + str(approvedName) +"\t" + str(approvedSymbol) + "\t" + str(hgncID))
