# def velocidade(Q):
#     return (Q/3600)/(186.3357/1000*1000)


# print(velocidade(0.629))

from os import listdir, path
import pandas as pd
import re
import math

caso = 4
entrada = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 4 DPM e UDF\Samples quebra sem adesao 28-06-2022\Caso 4"
saida =   r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 4 DPM e UDF\Samples quebra sem adesao 28-06-2022\Caso 4"


# Obter arquivos na pasta
dpm_files = [f for f in listdir(entrada) if f.endswith('.csv')]

# Loop sobre cada arquivo para salvar os dados importantes
for f in dpm_files:
    a = open(path.join(entrada, f), mode="r")
    dtg = pd.read_csv(a, sep=',',header = 0,usecols=range(0,10),engine='python')
    # sample = pd.read_csv(a, sep='[\(\)\s]+',usecols=range(1,14),names=names,nrows=10, engine='python')
    
    
    
    
    # Agrupando
    # sample['V'] = (sample['u']**2+sample['v']**2+sample['w']**2)**0.5
    
    # DTG
    # dtg = sample[['diameter','parcel-mass']].groupby(by = ['diameter']).sum()
    # dtg.reset_index(inplace=True)
    # dtg['parcel-acum'] = dtg['parcel-mass'].cumsum()
    
    # Massa acumulada
    # dtg['frac-mass'] = 100*dtg['parcel-mass']/dtg['parcel-mass'].sum() #Percentual massico
    # dtg_acum = 100*dtg['parcel-acum']/dtg['parcel-mass'].sum()
    # dtg['frac_mass_acum'] = dtg_acum
    
    v_acum = dtg['frac-mass']*dtg['diameter']**3
    v_acum = 100*(v_acum/v_acum.sum()).cumsum()


    ind = abs(v_acum-10).argmin()
    indm = ind-1 if v_acum[ind]>10 else ind+1
    dtg['D10'] = dtg['diameter'][indm]+(10-v_acum[indm])*(dtg['diameter'][ind]-dtg['diameter'][indm])/(v_acum[ind]-v_acum[indm])
    
    ind = abs(v_acum-50).argmin()
    indm = ind-1 if v_acum[ind]>50 else ind+1
    dtg['D50'] = dtg['diameter'][indm]+(50-v_acum[indm])*(dtg['diameter'][ind]-dtg['diameter'][indm])/(v_acum[ind]-v_acum[indm])
    
    ind = abs(v_acum-90).argmin()
    indm = ind-1 if v_acum[ind]>90 else ind+1
    dtg['D90'] = dtg['diameter'][indm]+(90-v_acum[indm])*(dtg['diameter'][ind]-dtg['diameter'][indm])/(v_acum[ind]-v_acum[indm])

    #Velocidade media
    # dtg['V-med'] = sample['V'].mean()
    z_plane = dtg['z'].median()
    # dtg['z'] = z_plane
    # dtg['Caso'] = caso
    
    # dtg.drop(['D99'], inplace=True, axis = 1)
    # Escrevendo no arquivo
    
    f_w = re.findall('\d+',f)[0] +'_py'
    filename = f'dtg z {math.ceil(1000*z_plane)}.csv'
    print(f'Escrevendo Data Frame dtg no arquivo dtg z {filename}')
    
    # dtg.to_csv(path.join(saida,filename))
    dtg.to_csv(path.join(saida,filename),index=False)
    
    a.close()