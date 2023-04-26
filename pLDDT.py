from pymol import cmd


def pLDDT(selection="all"):

    cmd.color("0x0053D6", f"({selection}) and b > 0.900")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.899 and b > 0.700")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.699 and b >= 0.500")
    cmd.color("pink", f"({selection}) and b < 0.499")
    
#0xFF7D45

cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
