from pymol import cmd


def esmpLDDT(selection="atom"):

    cmd.color("red", f"({selection}) and b > 0.9")
    #cmd.color("red", f"({selection}) and b = 0.9")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.7")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.5")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5")
    

cmd.extend("esmpLDDT", esmpLDDT)
cmd.auto_arg[0]["esmpLDDT"] = [cmd.object_sc, "object", ""]

    
def afpLDDT(selection="all"):

    cmd.color("0x0053D6", f"({selection}) and b > 90")
    #cmd.color("red", f"({selection}) and b = 0.9")
    cmd.color("0x65CBF3", f"({selection}) and b < 90 and b > 70")
    cmd.color("0xFFDB13", f"({selection}) and b < 70 and b > 50")
    cmd.color("0xFF7D45", f"({selection}) and b < 50")
    
#

cmd.extend("afpLDDT", afpLDDT)
cmd.auto_arg[0]["afpLDDT"] = [cmd.object_sc, "object", ""]
