# JK PyMol scripts
File > Edit pymolrc
![image alt](https://github.com/Jkerrison/pLDDT/blob/main/pymolrc.png?raw=true)
---
## pLDDT.py
Forked from **cbalbin-bio / pymol-color-alphafold**, modified to use Colours matching Alphafold database and Work with ESMfold Models 

### Run in Pymol command line or add to pymolrc file
run https://raw.githubusercontent.com/Jkerrison/pLDDT/master/pLDDT.py

load Protein.pdb
```pLDDT {Protein}```

![image alt](https://github.com/Jkerrison/pLDDT/blob/main/pLDDT_protein.png?raw=true)
![image alt](https://github.com/Jkerrison/pLDDT/blob/main/pLDDT.png?raw=true)
---

# Conservation

### Run in Pymol command line or add to pymolrc file
run https://raw.githubusercontent.com/Jkerrison/pLDDT/refs/heads/main/conservation_score.py

load Protein.pdb
```conservation('/path/to/aln.fa','Protein') ```


![image alt](https://github.com/Jkerrison/pLDDT/blob/main/conservation.png?raw=true)
---
