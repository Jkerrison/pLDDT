from pymol import cmd


def pLDDT(selection="all"):

    cmd.color("0x0053D6", f"({selection}) and b > 0.90")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.90 and b > 0.70")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.70 and b > 0.50")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.50")


cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
