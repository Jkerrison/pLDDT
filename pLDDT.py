from pymol import cmd

def pLDDT(selection="atom"):

    cmd.color("0x0053D6", f"({selection}) and b > 89.9 or b < 1 and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 90 and b > 70")
    cmd.color("0xFFDB13", f"({selection}) and b < 70 and b > 50")
    cmd.color("0xFF7D45", f"({selection}) and b < 50")
    cmd.color("0x0053D6", f"({selection}) and b < 1 and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.69")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.49")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5")
    
cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
