
   
look_for_data = True
dtg_const = pd.DataFrame([],columns = ['Caso','z','D10','D50','D90','V-med'])
dtg_perfis = pd.DataFrame([],columns = ['Caso','z','diameter','frac-mass','frac_mass_acum'])

inlet = 'dtg z 1'
outlet ='dtg z 369'
inlet_z = 0.001
outlet_z = 0.369

# Obter arquivos na pasta
csv_pastas = [f for f in listdir(entrada) if path.isdir(path.join(entrada, f)) and f.startswith('Caso')]




if look_for_data:
    for p in csv_pastas:
        p_path = path.join(entrada,p)
        csv_files  = [f for f in listdir(p_path) if path.isfile(path.join(p_path, f)) and f.endswith('.csv')]
        Caso = int(re.findall('\d',p)[0])
       
        # Loop sobre cada arquivo para salvar os dados importantes
        for f in csv_files:
            a = open(path.join(p_path, f), mode="r")
            dtg = pd.read_csv(a, sep=',',header = 0,engine='python')
            
            app = pd.DataFrame(
                [[
                    Caso,
                    dtg['z'][0],
                    dtg['D10'][0],
                    dtg['D50'][0],
                    dtg['D90'][0],
                    dtg['V-med'][0]
                 ]], columns=dtg_const.columns)
            
            dtg_const = pd.concat([dtg_const,app],ignore_index=True,axis=0)
        
            if f.startswith(inlet) and dtg.z[0] == inlet_z:
                app = dtg[['z','diameter','frac-mass','frac_mass_acum']]
                app['Caso'] = Caso
                dtg_perfis = pd.concat([dtg_perfis,app],ignore_index=True,axis=0)
                
            if f.startswith(outlet) and dtg.z[0] == outlet_z:
                app = dtg[['z','diameter','frac-mass','frac_mass_acum']]
                app['Caso'] = Caso   #np.tile
                dtg_perfis = pd.concat([dtg_perfis,app],ignore_index=True,axis=0)

            
        print(f'Finalizado Caso {Caso}')
        
      
        
      
        
      
       



# Plot 1
    # Entrada definida e a obtida por sample

# Plot 2
    # Entrada cada caso
    # Saida cada caso
    # x: diameter
    # y: frac-mass


dtg_g_z = dtg_perfis.groupby(dtg_perfis.z)
fig, ax = plt.subplots(tight_layout=True)
threshold = 0.01
i = 0
ls = ['','--','-.',':','-.']
markers = ['x','s','o','*', 'd']

for z in dtg_g_z.groups.keys():
    # z = 0.369
    dtg_z_by_caso = dtg_g_z.get_group(z).groupby(dtg_g_z.get_group(z).Caso)
    casos = dtg_z_by_caso.groups.keys()
    for caso in casos:
        if z == outlet_z:
            if caso == 1:
                pass
                # df = dtg_z_by_caso.get_group(caso)[['diameter','frac-mass']]
                # df = df.drop(df[df['frac-mass'] < threshold].index)
                # ax.plot(1e6*df['diameter'].values,df['frac-mass'].values,
                #         lw=2,
                #         alpha=0.9,
                #         ls=ls[i],
                #         ms=8,
                #         marker="s",
                #         mfc="none",
                #         label =r'$Q$ =   600 L/h, $\rho=5$ cP, $Re$ = 5150',
                #         color = cor[i])
                # i=i+1
            elif caso == 2:
                df = dtg_z_by_caso.get_group(caso)[['diameter','frac-mass']]
                df = df.drop(df[df['frac-mass'] < threshold].index)
                ax.plot(1e6*df['diameter'].values,df['frac-mass'].values,
                        lw=2,
                        alpha=0.9,
                        ls=ls[i],
                        ms=8,
                        marker="o",
                        mfc="none",
                        label =r'$Q$ = 1000 L/h, $\mu=5$ cP, $Re$ = 8590',
                        color = cor[i])
                i=i+1
            elif caso == 3:
                pass
                # df = dtg_z_by_caso.get_group(caso)[['diameter','frac-mass']]
                # df = df.drop(df[df['frac-mass'] < threshold].index)
                # ax.plot(1e6*df['diameter'].values,df['frac-mass'].values,
                #         lw=2,
                #         alpha=0.9,
                #         ls=ls[i],
                #         label =r'$Q$ =   600 L/h, $\rho=7$ cP, $Re$ = 3680',
                #         color = cor[i])
                # i=i+1
            elif caso == 4:
                pass
                # #print(dtg_z_by_caso.get_group(caso)['frac-mass'].values)
                # df = dtg_z_by_caso.get_group(caso)[['diameter','frac-mass']]
                # df = df.drop(df[df['frac-mass'] < threshold].index)
                # ax.plot(1e6*df['diameter'].values,df['frac-mass'].values,
                #         lw=2,
                #         alpha=0.9,
                #         ls=ls[i],
                #         label =r'$Q$ = 1000 L/h, $\rho=7$ cP, $Re$ = 6135',
                #         color = cor[i])
                # i=i+1
        if z == inlet_z and caso == 1:    
                df = dtg_z_by_caso.get_group(caso)[['diameter','frac-mass']]
                df = df.drop(df[df['frac-mass'] < threshold].index)
                ax.plot(1e6*df['diameter'].values,df['frac-mass'].values,
                        ls='-',
                        alpha=1,
                        ms=8,
                        marker="*",
                        mfc=cor[i],
                        label ='Perfil na entrada',
                        color = cor[i])
                i=i+1
        ax.grid()
        ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
        ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.95, 0.75))
        ax.set(ylabel=r"Fração Mássica $Y_g$ > 0,01 [%]", xlabel=r"Diâmetro [$\mu$m]")
        plt.show()
        
    
# Plot 3
    # Entrada cada caso
    # Saida cada caso
    # x: diameter
    # y: frac_mass_acum
    
# Plot 4,5,6,7
    # x: z Distância da entrada z [mm]
    # y: D10, D50, D90


D = 'D90'
fig, ax = plt.subplots(tight_layout=True)
# threshold = 0.01
i = 1
ls = ['-.','--','-.',':','-.']
markers = ['x','s','o','*', 'd']
dfi = dtg_const.groupby(dtg_const['Caso'])
casos = dfi.groups.keys()
for caso in casos:
    if caso == 1:
        
        df = dfi.get_group(caso)[['z',D]]
        df = df.sort_values(by='z')
        ax.plot(1e3*df['z'],1e6*df[D].values,
                lw=2,
                alpha=0.9,
                ls=ls[i],
                ms=8,
                marker="s",
                mfc="none",
                label =r'$Q$ =   600 L/h, $\rho=5$ cP, $Re$ = 5150',
                color = cor[i])
        i=i+1
    elif caso == 2:
        df = dfi.get_group(caso)[['z',D]]
        df = df.sort_values(by='z')
        df = df.drop(df[(df['z'] < 0.25)*(df['z'] > 0.19)].index)
        ax.plot(1e3*df['z'],1e6*df[D].values,
                lw=2,
                alpha=0.9,
                ls=ls[i],
                ms=8,
                marker="o",
                mfc="none",
                label =r'$Q$ = 1000 L/h, $\mu=5$ cP, $Re$ = 8590',
                color = cor[i])
        i=i+1
    elif caso == 3:
        
        df = dfi.get_group(caso)[['z',D]]
        df = df.sort_values(by='z')
        ax.plot(1e3*df['z'].values,1e6*df[D].values,
                lw=2,
                alpha=0.9,
                ls=ls[i],
                label =r'$Q$ =   600 L/h, $\rho=7$ cP, $Re$ = 3680',
                color = cor[i])
        i=i+1
    elif caso == 4:
        
        df = dfi.get_group(caso)[['z',D]]
        df = df.sort_values(by='z')
        df = df.drop(df[(df['z'] < 0.25)*(df['z'] > 0.19)].index)
        ax.plot(1e3*df['z'].values,1e6*df[D].values,
                lw=2,
                alpha=0.9,
                ls=ls[i],
                label =r'$Q$ = 1000 L/h, $\mu=7$ cP, $Re$ = 6135',
                color = cor[i])
        i=i+1
    

    
    ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
    ax.legend(loc="lower left", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.05, 0.1))
    ax.set(ylabel=r"Diâmetro $D_{90}$ [$\mu$m]", xlabel=r"Z [mm]")
    ax.grid()
    




