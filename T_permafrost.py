#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 09:49:01 2022

@author: jason
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit

iyear=1971 ; fyear=2021
n_years=fyear-iyear+1

# ------------------------------------------------------------------------- T Permafrost
#Russia
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Russian_T_Permafrost.txt'
TpermafrostRU = pd.read_csv(fn, sep='\t')#, delimiter=",")
print(TpermafrostRU.columns)

# AK
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Permafrost temp North Slope Alaska1_updated.xlsx'
dfTpermafrostAK = pd.read_excel(fn)#, sep='\t',decimal=",")
#West Dock	Deadhorse	Franklin Bluffs	Happy Vall	Gailbrath Lake

df=pd.concat([TpermafrostRU,dfTpermafrostAK],axis=1)
cols = list(df)
cols.insert(0, cols.pop(cols.index('Year')))
df = df.loc[:, cols]
df.drop('date', axis=1, inplace=True)

## %%
# CA
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Canadian PF temp for AMAP.xlsx'
# 'Year ', 'T_Norman_Wells_12m', 'T_Wrigley_12m', 'T_Alert_BH1_24m', 'T_Alert_BH2_12m', 'T_Alert_BH5_15m']
dfTpermafrostCA = pd.read_excel(fn)

df = pd.merge(df,dfTpermafrostCA, how='left', on="Year")

fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/NAm Russia PF temp update for AMAP.xlsx'
dfTpermafrostCA2 = pd.read_excel(fn,'Additional Can sites',skiprows=1)
df = pd.merge(df,dfTpermafrostCA2, how='left', on="Year")

##%%
# Nordics
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Nordic PERMAFROST T AMAP Ketil Isaksen.csv'
# 'Year', 'T_Janssonhaugen_P10_20m	T_Tarfalaryggen_P20_20m	T_Iskoras_Is_B2_20m	T_Kapp_Linne_1_20m
dfTpermafrostNO = pd.read_csv(fn, sep=';')
dfTpermafrostNO.columns

df = pd.merge(df,dfTpermafrostNO, how='left', on="Year")
##%%
#Zackenberg
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Zackenberg_soilTemp/annual1.3m.csv'
#year,mean,n
dfTpermafrostZach = pd.read_csv(fn, sep=',', index_col=0,skiprows=1,names=['Year','Zackenberg 1.830 m','n'])
fn='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Re__Arctic_Station_or_Nuuk_ground_temperature_data_series/Zackenberg_1830_cm_T_2012-2020.csv'
dfTpermafrostZach.drop('n', axis=1, inplace=True)
df = pd.merge(df,dfTpermafrostZach, how='left', on="Year")

df.drop(df[df.Year<1978].index, inplace=True)
df.reset_index(drop=True, inplace=True)

#%%

df=df.rename(columns={"West Dock": "West Dock AK"})
df=df.rename(columns={"Deadhorse": "Deadhorse AK"})
df=df.rename(columns={"Franklin Bluffs": "Franklin Bluffs AK"})
df=df.rename(columns={"Happy Vall": "Happy Vall AK"})
df=df.rename(columns={"Gailbrath Lake": "Gailbrath Lake AK"})
df=df.rename(columns={"T_Norman_Wells_12m": "Norman Wells CA"})
df=df.rename(columns={"T_Wrigley_12m": "Wrigley CA"})
df=df.rename(columns={"T_Alert_BH1_24m": "Alert BH1 CA"})
df=df.rename(columns={"T_Alert_BH2_24m": "Alert BH2 CA"})
df=df.rename(columns={"T_Alert_BH5_15m": "Alert BH5 CA"})

df=df.rename(columns={"Wrigley2 Canada 10m": "Wrigley 2 CA"})
df=df.rename(columns={"Pond Inlet Canada 15 m": "Pond Inlet CA"})
df=df.rename(columns={"Pangnirtung Canada 15m": "Pangnirtung CA"})

df=df.rename(columns={"T_Janssonhaugen_P10_20m": "Janssonhaugen SV"})
df=df.rename(columns={"T_Tarfalaryggen_P20_20m": "Tarfalaryggen SV"})
df=df.rename(columns={"T_Iskoras_Is_B2_20m": "Iskoras SV"})
df=df.rename(columns={"T_Kapp_Linne_1_20m": "Kapp Linne SV"})
df=df.rename(columns={"Zackenberg 1.830 m": "Zackenberg 1.83m GL"})
df=df.rename(columns={"Urengoy15-06": "Urengoy15-06 RU"})
df=df.rename(columns={"Urengoy15-10": "Urengoy15-10 RU"})
df=df.rename(columns={"Bolvansky56": "Bolvansky56 RU"})
df=df.rename(columns={"Bolvansky65": "Bolvansky65 RU"})

df.to_csv('/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/T_permafrost_1971-2021_annual.csv')
df.to_excel('/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/T_permafrost_1971-2021_annual.xlsx')

print(df.columns)

# #%%

fs=14 # land ice
# fs=10 # rivers
th=1
# plt.rcParams['font.sans-serif'] = ['Georgia']
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = True
# plt.rcParams['axes.grid'] = False
# plt.rcParams['grid.alpha'] = 0
plt.rcParams['grid.alpha'] = 1
co=0.9; plt.rcParams['grid.color'] = (co,co,co)
plt.rcParams["font.size"] = fs
plt.rcParams['legend.fontsize'] = fs*0.8
plt.rcParams['mathtext.default'] = 'regular'

# df.columns[31:45]
i0=1 ; i1=df.shape[1]
sites=df.columns[i0:i1]
print(sites)

x=df.Year
labels=['Urengoy15-06 RU','Urengoy15-10 RU', 'Bolvansky56 RU', 'Bolvansky65 RU',
        'West Dock AK','Deadhorse AK','Franklin Bluffs AK','Happy Vall AK','Gailbrath Lake AK',
        'Norman Wells CA','Wrigley CA','Alert BH1 CA','Alert BH2 CA','Alert BH5 CA',"Wrigley 2 CA","Pond Inlet CA",'Pangnirtung CA',
        'Janssonhaugen SV','Tarfalaryggen SV','Iskoras SV','Kapp Linne SV',
        'Zackenberg 1.83m GL']

sym0='.'
sym1='x'
sym2='*'
sym3='+'
sym4='1'
sym5='2'
sym6='3'
sym7='4'

sym=[sym0,sym1,sym2,sym3,
     sym0,sym1,sym2,sym3,sym4,
     sym0,sym1,sym2,sym3,sym4,sym5,sym6,sym7,
     sym0,sym1,sym2,sym3,
     sym0]

n_sites=len(sites)
xx=np.arange(n_sites)

rates=[np.nan]*n_sites
means=[np.nan]*n_sites

plt_annual=1
plt_rates=0

plt.close()
fig, ax = plt.subplots(figsize=(6, 12))


cc=0
for i,site in enumerate(labels):
    means[i]=np.nanmean(df[site].astype(float))
    labels[i]=site
    colorx='m'
    if site[-2:]=='GL':
        colorx='g'
    if site[-2:]=='RU':
        colorx='r'
    if site[-2:]=='SV':
        colorx='purple'
    if site[-2:]=='CA':
        colorx='b'
    if site[-2:]=='AK':
        colorx='k'
    if i<103:
        anom=0
        if anom:
    #        v=np.where((x>=1981)&(x<=2010))
            v=np.where((x>=1988)&(x<=2007))
            df.iloc[:,i+i0]=df.iloc[:,i+i0]-np.nanmean(df.iloc[v[0],i+i0])
            ylab='permafrost temperature anomaly, deg. C, relative to 1988-2007'
            # print("permafrost warming relative to 1988-2007 period: ",np.max(df.iloc[:,i+i0]))
        start_year=1978
        start_year=2000
        # start_year=2012
        v=np.where((np.isfinite(df.iloc[:,i+i0]))&(x>=start_year))
        if len(v[0])>1:
            b, m = polyfit(x[v[0]], df.iloc[v[0],i+i0], 1)
            # if plt_annual:
            plt.plot(x[v[0]], b + m * x[v[0]], '--',c=colorx,linewidth=th)
        v=np.where((np.isfinite(df.iloc[:,i+i0]))&(x>=start_year))
        if len(v[0])>1:
            b, m = polyfit(x[v[0]], df.iloc[v[0],i+i0], 1)
            ny=np.max(x[v[0]])-start_year
            # print("rate of T increase since 2000",m,"N years",ny,"change ",ny*m)
            print("T increase since "+str(start_year),site,ny,len(v[0]),"%.2f" %(ny*m))
            rates[i]=m*ny
        if plt_annual:
            # if colors[i]=='deepskyblue':sym[i]='*'
            plt.plot(x,df[site],sym[i],c=colorx,label=site+'\n'+r'$\Delta$'+'T$_{2000-2021}$:'+"%.1f" %(ny*m)+'°C')
            cc+=1
print('n sites',cc)
# plt.title('Arctic permafrost temperatures')
plt.axhline(y=0,c='gray',linewidth=0.5)
ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))        
plt.ylabel('Arctic permafrost temperatures, °C')
mult=0.9
figsubpath='Tpermafrost' ; source='Smith, Romanovsky, Isaksen, Christensen' ; 
props = dict(boxstyle='round', facecolor='w', alpha=0.5,edgecolor='w')
ax.text(1.01,0.01, 'Arctic Monitoring and Assessment Program (AMAP), '+source+', Box', transform=ax.transAxes, fontsize=fs*mult,
        verticalalignment='top',rotation=90,color='grey', rotation_mode="anchor")

fig_path='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/Permafrost T/Figs/'

ly='p'
figname='T_permafrost_AMAP_multisite_timeseries'
if ly=='p':
    DPI=200
    plt.savefig(fig_path+figname+'.png', bbox_inches='tight', dpi=DPI, facecolor='w', edgecolor='k')
    # plt.savefig(fig_path+figname+'.eps', bbox_inches='tight', facecolor='w', edgecolor='k')

#%%
# s=np.argsort(rates)
# s=np.flip(s)
# s=np.argsort(means)

# labelss = np.array(labels)[s.astype(int)]
# # labels2=labels[s2]
# for ii,varname in enumerate(sites):
# i=s[ii]
# print(ii,labelss[ii],means[i],rates[i])
# if plt_rates:
#     plt.bar(xx[ii], rates[i], width=0.8,color=colors[i],zorder=20)
#     plt.text(xx[ii], rates[i]+0.05,str('%.1f'%means[i]), color=colors[i],fontsize=fs*0.7,ha='center',zorder=20)
#     if ii==1: plt.text(xx[ii]+0.5, rates[i]+0.04,' ° C = 2000 to 2019 average', color=colors[i],fontsize=fs*0.7,ha='left',zorder=20)

#     plt.ylabel('Permafrost temperature change since '+str(start_year)+', ° C')
#     # plt.xlabel(sites)
#     plt.xticks(np.arange(min(xx), max(xx)+1, 1.0),rotation=45, rotation_mode="anchor",ha='right',va='center_baseline')
#     ax.set_xticklabels(labelss,rotation=90)

#     # plt.legend()
# if plt_annual:
#     plt.ylabel(ylab)
#     plt.xlabel('year')
#     plt.xticks(np.arange(min(x), max(x)+1, 2.0),rotation=45, rotation_mode="anchor",ha='right')
#     plt.legend()
#     ax.legend(loc='center left', bbox_to_anchor=(1.03, 0.5))
# mult=0.6
# legend_text_size=8.6
# #%%
# plt.close()
# # fs=20
# x=np.array(means) ; y=np.array(rates)
# plt.scatter(x,y)
# for i,varname in enumerate(sites):
#     plt.text(x[i], y[i],varname[13:],fontsize=fs*0.6,ha='left',zorder=20,rotation=45)

# plt.ylabel('permafrost temperature change after '+str(start_year)+', ° C',fontsize=fs)
# plt.xlabel('average permafrost temperature after '+str(start_year)+', ° C',fontsize=fs)
#     # b, m = polyfit(x[v[0]], df.iloc[v[0],i+i0], 1)
# coefs = np.polyfit(x, y, 2)  # quadratic
# x=np.arange(-15,1)
# fit=coefs[0]*x**2+coefs[1]*x+coefs[2]
# # plt.plot(x,fit)

# print(str('%.1f'%np.nanmean(rates))+'±'+str('%.1f'%np.nanstd(rates)))