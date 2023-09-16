def All(Data, AccessionNum, database):
    MitoSymbol = list(database['Mitochondrial'])
    MIMList = list(database['MIM'])
    IMSList = list(database['IMS'])
    MatrixList = list(database['Matrix'])
    MOMList = list(database['MOM'])
    j = 0

    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MitoSymbol:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'NO'

        if result in MIMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'NO'

        if result in IMSList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'NO'

        if result in MatrixList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'NO'

        if result in MOMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'NO'

        j += 1

    return Data

def All2(Data, AccessionNum, database):
    MitoSymbol = list(database['Mitochondrial'])
    GolgiList = list(database['Golgi'])
    ERList = list(database['ER'])
    KinaseList = list(database['Kinases'])
    proteaseList = list(database['Protease'])
    AutophagyList = list(database['Autophagy'])
    ApoptosisList = list(database['Apoptosis'])

    j = 0

    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MitoSymbol:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'NO'

        if result in GolgiList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Golgi Localization'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Golgi Localization'] = 'NO'

        if result in ERList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'ER Localization'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'ER Localization'] = 'NO'

        if result in KinaseList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Kinases'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Kinases'] = 'NO'

        if result in proteaseList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Proteases'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Proteases'] = 'NO'

        if result in AutophagyList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Autophagy Proteins'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Autophagy Proteins'] = 'NO'

        if result in ApoptosisList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Apoptosis Proteins'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Apoptosis Proteins'] = 'NO'

        j += 1

    return Data

def mito_mouse(Data, AccessionNum, database):
    MitoSymbol = list(database['Mouse_Mitochondrial'])
    j = 0
    k = 1
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MitoSymbol:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'YES'
            k += 1
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'NO'

        j += 1
    #print('[#] Number of mitochondtrial heavy proteins:' + str(k))
    return Data

def mito_human(Data, AccessionNum, database):
    MitoSymbol = list(database['Human_Mitochondrial'])
    j = 0
    k = 1
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MitoSymbol:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'YES'
            k += 1
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mitochondrial Localization'] = 'NO'

        j += 1
    #print('[#] Number of mitochondtrial heavy proteins:' + str(k))
    return Data

def golgi(Data, AccessionNum, database):
    GolgiList = list(database['Golgi'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in GolgiList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Golgi Localization'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Golgi Localization'] = 'NO'

        j += 1
    return Data

def ER(Data, AccessionNum, database):
    ERList = list(database['ER'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in ERList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'ER Localization'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'ER Localization'] = 'NO'

        j += 1

    return Data
    #Data.to_excel(str(outputfilename2) + '-Sorter_Output.xlsx')

def kinase(Data, AccessionNum, database):
    KinaseList = list(database['Kinases'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in KinaseList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Kinases'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Kinases'] = 'NO'

        j += 1
    return Data

def protease(Data, AccessionNum, database):
    proteaseList = list(database['Protease'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in proteaseList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Proteases'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Proteases'] = 'NO'

        j += 1
    return Data

def autophagy(Data, AccessionNum, database):
    AutophagyList = list(database['Autophagy'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in AutophagyList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Autophagy Proteins'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Autophagy Proteins'] = 'NO'

        j += 1
    return Data

def apoptosis(Data, AccessionNum, database):
    ApoptosisList = list(database['Apoptosis'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in ApoptosisList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Apoptosis Proteins'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Apoptosis Proteins'] = 'NO'

        j += 1
    return Data

def MIM(Data, AccessionNum, database):
    MIMList = list(database['MIM'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MIMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'NO'

        j += 1
    return Data

def IMS(Data, AccessionNum, database):
    IMSList = list(database['IMS'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in IMSList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'NO'

        j += 1
    return Data

def MOM(Data, AccessionNum, database):
    MOMList = list(database['MOM'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MOMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'NO'

        j += 1
    return Data

def Matrix(Data, AccessionNum, database):
    MatrixList = list(database['Matrix'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j+=1
            continue

        if result in MatrixList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'NO'

        j += 1
    return Data

def mitochondrialLocationsAll(Data, AccessionNum, database):
    # list obtained from mitocarta 3.0
    #MitoSymbol = list(database['Mitochondrial'])
    MIMList = list(database['MIM'])
    IMSList = list(database['IMS'])
    MatrixList = list(database['Matrix'])
    MOMList = list(database['MOM'])

    j = 0

    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MIMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'NO'

        if result in IMSList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'NO'

        if result in MatrixList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'NO'

        if result in MOMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'NO'

        j += 1

    return Data

def complexSortingAll(Data, AccessionNum, database):
    # list obtained from https://www.genenames.org/data/genegroup/#!/group/639
    # Complex 1	Complex 2	Complex 3	Complex 4	Complex 5
    complex1List = list(database['Complex 1'])
    complex2List = list(database['Complex 2'])
    complex3List = list(database['Complex 3'])
    complex4List = list(database['Complex 4'])
    complex5List = list(database['Complex 5'])

    j = 0

    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in complex1List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 1'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 1'] = 'NO'

        if result in complex2List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 2'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 2'] = 'NO'

        if result in complex3List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 3'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 3'] = 'NO'

        if result in complex4List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 4'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 4'] = 'NO'

        if result in complex5List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 5'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 5'] = 'NO'

        j += 1

    return Data

def AllCompartComplex(Data, AccessionNum, database):
    MIMList = list(database['MIM'])
    IMSList = list(database['IMS'])
    MatrixList = list(database['Matrix'])
    MOMList = list(database['MOM'])
    complex1List = list(database['Complex 1'])
    complex2List = list(database['Complex 2'])
    complex3List = list(database['Complex 3'])
    complex4List = list(database['Complex 4'])
    complex5List = list(database['Complex 5'])

    j = 0

    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j += 1
            continue

        if result in MIMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MIM'] = 'NO'

        if result in IMSList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'IMS'] = 'NO'

        if result in MatrixList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Matrix'] = 'NO'

        if result in MOMList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'MOM'] = 'NO'



        if result in complex1List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 1'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 1'] = 'NO'

        if result in complex2List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 2'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 2'] = 'NO'

        if result in complex3List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 3'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 3'] = 'NO'

        if result in complex4List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 4'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 4'] = 'NO'

        if result in complex5List:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 5'] = 'YES'
        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Complex 5'] = 'NO'

        j += 1

    return Data

def proteinOfInterest(Data, AccessionNum, database):
    proteinOfinterestList = list(database['ProteinOfInterest'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j+=1
            continue

        if result in proteinOfinterestList:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Protein of Interest List'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Protein of Interest List'] = 'NO'

        j += 1
    return Data

def mia40_subs(Data, AccessionNum, database):
    MIA40_targets = list(database['MIA40_targets'])
    j = 0
    for i in AccessionNum:
        try:
            result = i[0:6]
        except:
            j+=1
            continue

        if result in MIA40_targets:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mia40 Substrates'] = 'YES'

        else:
            Data.loc[j, 'Accession new'] = result
            Data.loc[j, 'Mia40 Substrates'] = 'NO'

        j += 1
    return Data