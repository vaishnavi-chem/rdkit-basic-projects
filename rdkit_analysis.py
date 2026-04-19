from rdkit import Chem
from rdkit.Chem import Descriptors
#Create molecule
mol=Chem.MolFromSmiles("CCO")
mol=Chem.AddHs(mol)
#Count atoms
atom_count={}
for atom in mol.GetAtoms():
  symbol=atom.GetSymbol()
  atom_count[symbol]=atom_count.get(symbol, 0) +1
#Count Hydrogen
count_H=atom_count.get("H", 0)
#Total atoms
total_atoms=mol.GetNumAtoms()
#Molecular weight
mw=Descriptors.MolWt(mol)
#Output
print("Molecular Formula:",atom_count)
print("Total Atoms:", total_atoms)
print("Hydrogen:",count_H)
print("Molecular Weight:", round(mw, 3))
