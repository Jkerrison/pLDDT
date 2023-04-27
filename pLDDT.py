from pymol import cmd


def pLDDT(selection="atoms"):

    cmd.color("0x0053D6", f"({selection}) and b > 0.9")
    cmd.color("red", f"({selection}) and b = 0.9")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.7")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.5")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5")
    
#

cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
