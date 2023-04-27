from pymol import cmd


def esm_pLDDT(selection="atom"):

    cmd.color("0x0053D6", f"({selection}) and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.69")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.49")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5")
    #Appears to throw an error if <= is used so thats why there is a slight overlap in quality, rounds up
    #ESMfold predicts per atom pLDDT between 0-1 whereas Alphafold predics per residue values between 0-100
    

cmd.extend("esm_pLDDT", esm_pLDDT)
#cmd.auto_arg[0]["esm_pLDDT"] = [cmd.object_sc, "object", ""]

    
def pLDDT(selection="atom"):

    cmd.color("0x0053D6", f"({selection}) and b > 90")
    cmd.color("0x65CBF3", f"({selection}) and b < 90 and b > 70")
    cmd.color("0xFFDB13", f"({selection}) and b < 70 and b > 50")
    cmd.color("0xFF7D45", f"({selection}) and b < 50")
    cmd.color("0x0053D6", f"({selection}) and b < 1 and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.69")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.49")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5")
    
#

cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
