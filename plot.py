import gemmi
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import glob

#st = gemmi.read_structure('/Users/jkerrison/Dropbox/XHPi/XH-Pi_SHIRT/best_structures_plddt_90/A0A0B4RZP0_98-191_relaxed_rank_1_model_2.pdb')

list_of_files = (glob.glob("/Users/jkerrison/Dropbox/XHPi/XH-Pi_SHIRT/best_structures_plddt_90/*.pdb"))
list_of_files = [val for val in list_of_files if not val.endswith("_H.pdb")]

for i in list_of_files:
    st = gemmi.read_structure(i)



    chain = st[0]['A']
    polymer = chain.get_polymer()

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

    x = modelled_res_list
    y = pLDDT_per_res

    color_list = [(0, '#FF7D45'), (0.45, '#FF7D45'), (0.55, '#FFDB13'), (0.65, '#FFDB13'), (0.75, '#65CBF3'), (0.85, '#65CBF3'), (0.95, '#0053D6'), (1, '#0053D6')]
    cmap = colors.LinearSegmentedColormap.from_list('my_colormap', color_list)

    fig, ax = plt.subplots()

    ax.plot(x, y, color='black')

    sc = ax.scatter(x, y, c=y, cmap=cmap, vmin=50, vmax=100)

    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_ticks([0, 25, 50, 75, 100])
    cbar.set_ticklabels(['0', '25', '50', '75', '100'])

    plt.title(f'{st.name}', fontsize=16)
    plt.xlabel('ResNo', fontsize=12)
    plt.ylabel('pLDDT', fontsize=12)

    ax.set_ylim(0,100)
    ax.set_xlim(0,len(x)+1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.show()
