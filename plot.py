import gemmi
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import requests
import os
import scipy as sp
import scipy.interpolate
import os.path


def structure(model):
    st = gemmi.read_structure(model)
    chain = st[0]['A']
    polymer = chain.get_polymer()
    entity = st.setup_entities()
    ent = st.entities[0]
    seq = gemmi.one_letter_code(ent.full_sequence)
    polymer = chain.get_polymer()
    
    return(polymer,seq,entity,st.name)

def ESMfold(sequence='i'):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
    name = sequence[:3] + sequence[-3:]
    pdb_string = response.content.decode('utf-8')
    with open(f'{Alphafold[:-4]}_ESMfold.pdb', 'w') as f:
        f.write(pdb_string)

def pLDDT(polymer):
    pLDDT_per_res = []
    modelled_res_list= []
    for res in polymer:
        modelled_res_list.append(res.name)
        res_av_b = []
        for atom in res:    
            res_av_b.append(atom.b_iso)
        atom_b_mean=np.mean(res_av_b)  
        pLDDT_per_res.append(atom_b_mean)

    modelled_res_list = [i for i in range(1, len(modelled_res_list)+1)]
    if max(pLDDT_per_res) < 1.1:
        pLDDT_per_res = [i*100 for i in pLDDT_per_res]
    return(modelled_res_list,pLDDT_per_res)

def plot(x, y, x2=None, y2=None, color2='red'):
    new_length = len(x)*100
    x_new = np.linspace(min(x), max(x), new_length)
    y_new = sp.interpolate.interp1d(x, y, kind='cubic')(x_new)
    

    color_list = [(0, '#FF7D45'), (0.45, '#FF7D45'), (0.55, '#FFDB13'), (0.65, '#FFDB13'), (0.75, '#65CBF3'), (0.85, '#65CBF3'), (0.95, '#0053D6'), (1, '#0053D6')]
    cmap = colors.LinearSegmentedColormap.from_list('my_colormap', color_list)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x_new, y_new, color='black',label='Alphafold',linewidth=0.75,alpha=0.5)
    sc = ax.scatter(x_new, y_new, c=y_new, cmap=cmap, vmin=0, vmax=100,s=2)
    if x2 and y2:
        x2_new = np.linspace(min(x2), max(x2), new_length)
        y2_new = sp.interpolate.interp1d(x2, y2, kind='cubic')(x2_new)
        ax.plot(x2_new, y2_new, color=color2,alpha=0.2,linewidth=0.75,label='ESMfold')
        #sc = ax.scatter(x2_new, y2_new, c=y2_new, cmap=cmap, vmin=0, vmax=100,s=1,alpha=0.1)
        plt.legend(loc='lower left')
    
    
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_ticks([0, 25, 50, 75, 100])
    cbar.set_ticklabels(['0', '25', '50', '75', '100'])
    plt.title(f'{Alphafold[:-4]}', fontsize=12)
    plt.xlabel('ResNo', fontsize=12)
    plt.ylabel('pLDDT', fontsize=12)
    
    ax.set_ylim(0,100)
    ax.set_xlim(0,len(x)+1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #plt.savefig(f'{directory}{st.name}.pdf')
    plt.show()
    plt.close()
    return




directory = os.getcwd()
Alphafold = 'AF-L8XZM1-F1-model_v4.pdb'
af_poly, seq, af_entity, name = structure(Alphafold) 
if os.path.isfile(f'{Alphafold[:-4]}_ESMfold.pdb') == False:
    ESMfold(seq)
esm_poly, seq, esm_entity, name = structure(f'{Alphafold[:-4]}_ESMfold.pdb') 
x,y = pLDDT(af_poly)
x2,y2 = pLDDT(esm_poly)
plot(x,y,x2,y2)
#plot(x,y)
