from collections import Counter
from pymol import cmd

def calculate_residue_percentage(alignment_file):
    with open(alignment_file, 'r') as file:
        lines = file.readlines()
        first_sequence = ""
    for line in lines:
        if line.startswith('>'):
            if first_sequence:
                break
            continue
        first_sequence += line.strip()
    
    position_counts = [Counter() for _ in range(len(first_sequence))]
    
    current_sequence = ""
    for line in lines:
        if line.startswith('>'):
            if current_sequence:
                for i, residue in enumerate(current_sequence):
                    position_counts[i][residue] += 1
                current_sequence = ""
            continue
        current_sequence += line.strip()
    
    if current_sequence:
        for i, residue in enumerate(current_sequence):
            position_counts[i][residue] += 1
    
    total_sequences = len([line for line in lines if line.startswith('>')])
    residue_percentages = []
    for i, residue in enumerate(first_sequence):
        if residue == '-':
            continue
        count = position_counts[i][residue]
        percentage = (count / total_sequences) * 100
        residue_percentages.append((residue, percentage))
    
    return residue_percentages

def interpolate_color(percentage):
    if percentage >= 50:
        ratio = (percentage - 50) / 50
        r = int(255)
        g = int(255 * (1 - ratio))
        b = int(255 * (1 - ratio))
    else:
        ratio = percentage / 50
        r = int(255 * ratio)
        g = int(255 * ratio)
        b = int(255)
    
    return f"0x{r:02x}{g:02x}{b:02x}"

def conservation(alignment_file, selection="all"):
    percentages = calculate_residue_percentage(alignment_file)
    
    high_conservation_residues = []
    low_conservation_residues = []
    
    for i, (residue, percentage) in enumerate(percentages):
        color = interpolate_color(percentage)
        cmd.color(color, f"{selection} and resi {i+1}")
        
        if percentage > 75:
            high_conservation_residues.append(str(i+1))
        if percentage < 25:
            low_conservation_residues.append(str(i+1))

    
    if high_conservation_residues:
        cmd.select("conserved sites", f"{selection} and resi {'+'.join(high_conservation_residues)}")
    if low_conservation_residues:
        cmd.select("diverse_sites", f"{selection} and resi {'+'.join(low_conservation_residues)}")

cmd.extend("conservation", conservation)
cmd.auto_arg[0]["conservation"] = [cmd.object_sc, "object", ""]

