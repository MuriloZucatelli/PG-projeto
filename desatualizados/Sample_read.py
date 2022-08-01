# def velocidade(Q):
#     return (Q/3600)/(186.3357/1000*1000)


# print(velocidade(0.629))

from os import listdir, path
import pandas as pd
import re
import math

entrada = r"C:/Users/Murilo/Google Drive/Arquivos PG Murilo/Resultados de simulações/Etapa 4 DPM e UDF/Samples quebra sem adesao 28-06-2022"
saida =   r"C:/Users/Murilo/Google Drive/Arquivos PG Murilo/Resultados de simulações/Etapa 4 DPM e UDF/Samples quebra sem adesao 28-06-2022"
caso = 0

# Obter arquivos na pasta
dpm_files = [f for f in listdir(entrada) if f.endswith('.dpm')]

# Loop sobre cada arquivo para salvar os dados importantes
for f in dpm_files:
    print(f'\nAbrindo arquivo: {f}\n')
    a = open(path.join(entrada, f), mode="r")
    names = pd.read_csv(a, sep='[\(\)\s]+', skiprows=1,usecols=range(1,14),header=None, decimal=",",nrows=1, engine='python', dtype=str)
    #Para linux:
    #names = pd.read_csv(a, sep='[\(\)\s]+', skiprows=1,usecols=range(0,13),header=None, decimal=",",nrows=1, engine='python', dtype=str)
    names = names.values[0].tolist()
    print(f'Dados sendo recolhidos: {names}\n')
    a.close()
    
    # Abrindo para ler todos os dados
    a = open(path.join(entrada, f), mode="r")
    print(f'Lendo dados de {f}\n')
    sample = pd.read_csv(a, sep='[\(\)\s]+',skiprows=2,usecols=range(1,14),names=names, engine='python')
    # sample = pd.read_csv(a, sep='[\(\)\s]+',usecols=range(1,14),names=names,nrows=10, engine='python')
    
    print('Refinando dados \n')
    sample.drop(['t','x','y','time','flow-time'], inplace=True, axis = 1)
    
    
    
    # Agrupando
    sample['V'] = (sample['u']**2+sample['v']**2+sample['w']**2)**0.5
    
    # DTG
    # dtg = sample[['diameter','parcel-mass']].groupby(by = ['diameter']).sum()
    
    #Teste novo:
    dtg = sample[['diameter','parcel-mass','n-in-parcel']].groupby(by = ['diameter']).sum()
    
    dtg.reset_index(inplace=True)
    dtg['parcel-acum'] = dtg['parcel-mass'].cumsum()
    
    # Massa acumulada
    dtg['frac-mass'] = 100*dtg['parcel-mass']/dtg['parcel-mass'].sum() #Percentual massico
    
    dtg_acum = 100*dtg['parcel-acum']/dtg['parcel-mass'].sum()
    dtg['frac_mass_acum'] = dtg_acum
    
    
    ## Volumetric
    # dtg['N'] = dtg['n-in-parcel']/dtg['n-in-parcel'].sum()
    # v_acum = dtg['N']*dtg['diameter']**3
    # v_acum = 100*(v_acum/v_acum.sum()).cumsum()
    
    ## Baseado em frequencia
    N = sample[['diameter','parcel-mass']].groupby(by = ['diameter']).count()
    N = ((N/N.sum()).cumsum())
    N = N['parcel-mass'].values
    #N=N[0]

    v_acum = 100*N

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
    dtg['V-med'] = sample['V'].mean()
    z_plane = sample['z'].median()
    dtg['z'] = z_plane
    dtg['Caso'] = caso
    
    
    # Escrevendo no arquivo
    
    f_w = re.findall('\d+',f)[0] +'_py'
    filename = f'dtg z {math.ceil(1000*z_plane)}.csv'
    print(f'Escrevendo Data Frame dtg no arquivo dtg z {filename}')
    
    dtg.to_csv(path.join(saida,filename),index=False)
    a.close()
