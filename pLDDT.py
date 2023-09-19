from pymol import cmd

def pLDDT(selection="cartoon"): #atom

    cmd.set cartoon_color("0x0053D6", f"({selection}) and b > 89.9 or b < 1 and b > 0.89")
    cmd.set cartoon_color("0x65CBF3", f"({selection}) and b < 90 and b > 70")
    cmd.set cartoon_color("0xFFDB13", f"({selection}) and b < 70 and b > 50")
    cmd.set cartoon_color("0xFF7D45", f"({selection}) and b < 50")
    cmd.set cartoon_color("0x0053D6", f"({selection}) and b < 1 and b > 0.89")
    cmd.set cartoon_color("0x65CBF3", f"({selection}) and b < 0.9 and b > 0.69")
    cmd.set cartoon_color("0xFFDB13", f"({selection}) and b < 0.7 and b > 0.49")
    cmd.set cartoon_color("0xFF7D45", f"({selection}) and b < 0.5") #color
    
cmd.extend("pLDDT", pLDDT)
cmd.auto_arg[0]["pLDDT"] = [cmd.object_sc, "object", ""]
