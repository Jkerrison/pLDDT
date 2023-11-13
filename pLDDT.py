from pymol import cmd

def pLDDT(selection="cartoon"): #atom

    cmd.color("0x0053D6", f"({selection}) and b > 89.9 or b < 1 and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 90 and b > 70")
    cmd.color("0xFFDB13", f"({selection}) and b < 70 and b > 50")
    cmd.color("0xFF7D45", f"({selection}) and b < 50")
    cmd.color("0x0053D6", f"({selection}) and b < 1 and b > 0.89")
    cmd.color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.69")
    cmd.color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.49")
    cmd.color("0xFF7D45", f"({selection}) and b < 0.5") #color
    
cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]


def bFactor(selection="cartoon"): #atom

    cmd.color("0x0053D6", f"({selection}) and b < 11.96")  #Dark Blue
    cmd.color("0x65CBF3", f"({selection}) and b > 11.96 and b < 59.22")
    cmd.color("0xFFDB13", f"({selection}) and b > 59.22 and b < 293.31")
    cmd.color("0xFF7D45", f"({selection}) and b > 293.31")

cmd.extend("bFactor", bFactor)
cmd.auto_arg[0]["bFactor"] = [cmd.object_sc, "object", ""]
