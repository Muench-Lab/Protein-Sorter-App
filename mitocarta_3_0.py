import pandas as pd
columns = ["MIM", "MOM", "IMS", "Matrix"]

out_df = pd.DataFrame(columns=columns)

xls = pd.ExcelFile('Human.MitoCarta3.0.xls')
data = pd.read_excel(xls, 'A Human MitoCarta3.0')

subcellularLocal = data['MitoCarta3.0_SubMitoLocalization']
uniprot = data['UniProt']

for i in range(0, len(subcellularLocal)):
    uniprotFinal = uniprot[i]
    if 'MIM' in subcellularLocal[i]:
        print(f'MIM:{uniprotFinal}')
        out_df = out_df.append({'MIM':uniprotFinal}, ignore_index=True)

    if 'MOM' in subcellularLocal[i]:
        print(f'MOM:{uniprotFinal}')
        out_df = out_df.append({'MOM': uniprotFinal}, ignore_index=True)

    if 'IMS' in subcellularLocal[i]:
        print(f'IMS:{uniprotFinal}')
        out_df = out_df.append({'IMS': uniprotFinal}, ignore_index=True)

    if 'Matrix' in subcellularLocal[i]:
        print(f'Matrix:{uniprotFinal}')
        out_df = out_df.append({'Matrix': uniprotFinal}, ignore_index=True)

out_df.to_excel(f'mitocartaDeneme.xlsx')