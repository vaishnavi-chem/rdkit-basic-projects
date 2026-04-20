from rdkit import Chem
from rdkit.Chem import Descriptors

# Create molecule (change SMILES to test different molecules)
mol = Chem.MolFromSmiles("CC(=O)O")  # try also "CC(=O)OC"
mol = Chem.AddHs(mol)

# Count atoms
atom_count = {}
for atom in mol.GetAtoms():
    symbol = atom.GetSymbol()
    atom_count[symbol] = atom_count.get(symbol, 0) + 1

# Count hydrogen
count_H = atom_count.get("H", 0)

# Total atoms
total_atoms = mol.GetNumAtoms()

# Molecular weight
mw = Descriptors.MolWt(mol)

# COOH detection (loose vs strict)
pattern_loose = Chem.MolFromSmarts("C(=O)O")
pattern_strict = Chem.MolFromSmarts("C(=O)[OX2H1]")

has_cooh_loose = mol.HasSubstructMatch(pattern_loose)
has_cooh_strict = mol.HasSubstructMatch(pattern_strict)

# Output
print("Molecular Formula:", atom_count)
print("Total Atoms:", total_atoms)
print("Hydrogen:", count_H)
print("Molecular Weight:", round(mw, 3))

print("COOH (loose):", has_cooh_loose)
print("COOH (strict):", has_cooh_strict)
