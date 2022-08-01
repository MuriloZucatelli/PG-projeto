# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 18:20:27 2022

@author: Murilo
"""

# Fluent Sample to plot


from os import listdir, path
import pandas as pd
import re
import math
import numpy as np
from sys import platform

entrada = r"C:/Users/Murilo/Google Drive/Arquivos PG Murilo/Resultados de simulações/Etapa 4 DPM e UDF"
saida =   r"C:/Users/Murilo/Google Drive/Arquivos PG Murilo/Resultados de simulações/Etapa 4 DPM e UDF"
caso = 1
print('Caso: ',caso)

inlet = 'dtg z 1'
outlet ='dtg z 369'
inlet_z = 0.001
outlet_z = 0.369
plane_normal = 'z'
plane_id = 3
f_based = 'parcel'  
# f_based = 'particula'
d_based = 'percentil'
# d_based = 'interp'
# d_based = 'direto'

dtg_const = pd.DataFrame([],columns = ['caso','z','D10','D50','D90','V_med'])




def fx(N_d, d, res): # f(x) = y(x) - y
    return res(d) - N_d

def g(d,res_deriv): # g(x) = y(x)
    return res_deriv(d)


def fixedPointIteration(D0, N_d, erro, N, res,res_deriv):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(D0,res_deriv) == 0.0:
            print('Divide by zero error!')
            break
        
        D1 = D0 - fx(N_d,D0,res)/g(D0,res_deriv)
        print('Iteration-%d, d = %0.6f and f(p) = %0.6f' % (step, D1, fx(N_d,D1,res)))
        D0 = D1
        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(fx(N_d,D1,res)) > erro

    if flag==1:
        print('\nRequired root is: %0.8f' % D1)
    else:
        print('\nNot Convergent.')
    return D1



def d_statistic(dtg_const,sample,d,z,V):

    
    ## Baseado em frequencia dos parcels
    if f_based == 'parcel':
        N = sample[['diameter','parcel-mass']].groupby(by = ['diameter']).count()
        N = ((N/N.sum()).cumsum())
        N = N['parcel-mass'].values
    
    ## Baseado na frequencia das particulas totais
    if f_based == 'particula':
        N = sample[['diameter','n-in-parcel']].groupby(by = ['diameter']).sum() # Quantidade de particulas por diâmetro
        N = N['n-in-parcel'].cumsum() # Frequencia de particulas acumulada
        N = (N/N.tail(1).values) # Frequencia percentual de particulas acumulada
    
    ## Volumetric
    # dtg['N'] = dtg['n-in-parcel']/dtg['n-in-parcel'].sum()
    # v_acum = dtg['N']*dtg['diameter']**3
    # v_acum = 100*(v_acum/v_acum.sum()).cumsum()
    
    
    D = np.array([])  #holder
    percen = [10,50,90]
    if d_based == 'direto':
        ## D10,D50,D90: METODO 1
        # direto
    
        v_acum = 100*N
        ind = abs(v_acum-10).argmin()
        indm = ind-1 if v_acum[ind]>10 else ind+1
        D[0] = d[indm]+(10-v_acum[indm])*(d[ind]-d[indm])/(v_acum[ind]-v_acum[indm])
        
        ind = abs(v_acum-50).argmin()
        indm = ind-1 if v_acum[ind]>50 else ind+1
        D[1] = d[indm]+(50-v_acum[indm])*(d[ind]-d[indm])/(v_acum[ind]-v_acum[indm])
        
        ind = abs(v_acum-90).argmin()
        indm = ind-1 if v_acum[ind]>90 else ind+1
        D[2] = d[indm]+(90-v_acum[indm])*(d[ind]-d[indm])/(v_acum[ind]-v_acum[indm])
    
    
    if d_based == 'interp':
        ## D10,D50,D90: METODO 2
        #  Ajuste da curva de frequencia acumulada
    
        x = dtg_perfis['diameter']
        res = np.polynomial.Polynomial.fit(x,N,11)
        res_deriv = res.deriv()
        D0 = np.percentile(sample['diameter'],percen)
        erro = 1e-5
        N_iter = 100
        
        # Starting Newton Raphson Method
        for d,n in zip(D0,percen):
            D.append(fixedPointIteration(d,n/100, erro, N_iter,res,res_deriv))

        
    if d_based == 'percentil':
        ## D10,D50,D90: METODO 3
        # percentile da distribuição bruta
        D = np.percentile(sample['diameter'],percen)
            
    if (D > sample['diameter'].max()).any():
        print('Erro:\n Verificar código e resultados gerados')
    
    df = np.concatenate([np.array([caso,z]), D, np.array([V])])
    df = pd.DataFrame([df], columns=dtg_const.columns)
    dtg_const = pd.concat([dtg_const,df],ignore_index=True,axis=0)
    
    return dtg_const    



def dtg_writer(dado,filename):
    
    # Escrevendo no arquivo
    
    # f_w = re.findall('\d+',f)[0] +'_py'
    print(f'Escrevendo Data Frame {filename}')
    dado.to_csv(path.join(saida,filename),index=False)







# Obter arquivos na pasta
dpm_files = [f for f in listdir(entrada) if f.endswith('.dpm')]
print("Executando em: ",platform)
# Loop sobre cada arquivo para salvar os dados importantes
for f in dpm_files:
    
    dtg_perfis = pd.DataFrame([],columns = ['caso','z','diameter','frac_mass','frac_mass_acum'])
    
    print(f'\nAbrindo arquivo: {f}\n')
    a = open(path.join(entrada, f), mode="r")
    
    names = pd.DataFrame([])
    cols = np.array([plane_id, 4, 5, 6, 7, 9, 11])
    if platform == "linux" or platform == "linux2":
        names = pd.read_csv(a, sep='[\(\)\s]+', skiprows=1,usecols=(cols-1),header=None, decimal=",",nrows=1, engine='python', dtype=str)
    elif platform == "darwin":
        # OS X
        pass
    elif platform == "win32":
        # Windows...
        names = pd.read_csv(a, sep='[\(\)\s]+', skiprows=1,usecols=cols,header=None, decimal=",",nrows=1, engine='python', dtype=str)
    
    names = names.values[0].tolist()
    print(f'Dados sendo recolhidos: {names}\n')
    a.close()
    
    # Abrindo para ler todos os dados
    a = open(path.join(entrada, f), mode="r")
    print(f'Lendo dados de {f}\n')
    sample = pd.read_csv(a, sep='[\(\)\s]+',skiprows=2,usecols=cols,names=names, engine='python')
    #sample = pd.read_csv(a, sep='[\(\)\s]+',skiprows=2,usecols=range(1,14),names=names,nrows=10, engine='python')
    print(sample)
    # print('Refinando dados \n')
    # sample.drop(['t','x','y','time','flow-time'], inplace=True, axis = 1)
    
    
    
    # Agrupando   
    dtg = sample[['diameter','parcel-mass','n-in-parcel']].groupby(by = ['diameter']).sum()
    dtg.reset_index(inplace=True)
    
    plane_value = sample[plane_normal].median()
    print('Plano na posição z: ',plane_value)

    dtg_perfis['diameter'] = dtg['diameter']
    dtg_perfis['frac_mass'] = 100*dtg['parcel-mass']/dtg['parcel-mass'].sum()          # Percentual massico para cada diâmetro
    dtg_perfis['frac_mass_acum'] = dtg_perfis['frac_mass'].cumsum()                    # Fração mássica acumulada < d, Y_d
    dtg_perfis['caso'] = caso
    dtg_perfis['z'] = plane_value


    # Velocidade media
    V = ((sample['u']**2+sample['v']**2+sample['w']**2)**0.5).mean()


    
    #   Obtenção das estatisticas da distribuição
    dtg_const = d_statistic(dtg_const,sample,dtg_perfis['diameter'],plane_value,V)
    
    
    dtg_writer(dtg_perfis, f'dtg_perfis z {math.ceil(1000*plane_value)}.csv')  #Escrever dtg_perfis
    a.close()



dtg_const.sort_values(by='z',ascending=True,inplace=True,ignore_index=True)
dtg_writer(dtg_const, f'dtg_const caso {caso}.csv')  #Escrever dtg_perfis





